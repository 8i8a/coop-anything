"""Rule-based pull request check for coop-anything. No AI, nothing to trick.

    python tools/pr_check.py <diff file> <files.json> <account_created ISO date> > comment.md

files.json: the PR's file list as `gh pr view --json files` prints it ({"files": [...]}).
Prints a Markdown comment with findings and a verdict. Never runs PR code.
"""
import datetime
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
diff_path, files_path, created = sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ""
diff = open(diff_path, encoding="utf-8", errors="replace").read()
files = json.load(open(files_path, encoding="utf-8")).get("files", [])
paths = [f["path"] for f in files]
added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]

block, look, ok = [], [], []

# Files
BINARY = re.compile(r"\.(exe|dll|so|dylib|bin|pak|ucas|utoc|uasset|u|umx|uax|utx|dx|unr|esm|esp|bsa|ba2|db|z64|n64|iso|rom|7z|rar|zip|msi|jar)$", re.I)
SENSITIVE = (".github/", "tools/", ".mcp.json", ".agents/", ".claude/", "AGENTS.md", "CLAUDE.md")
bins = [p for p in paths if BINARY.search(p)]
if bins:
    block.append("Binary or game-data files added: " + ", ".join(f"`{p}`" for p in bins))
sens = [p for p in paths if p.startswith(SENSITIVE) or p in SENSITIVE]
if sens:
    look.append("Touches code, workflows or agent rules (needs a careful human read): " + ", ".join(f"`{p}`" for p in sens))
CODE = re.compile(r"(\.(c|cc|cpp|h|hpp|cs|py|js|ts|lua|ps1|psm1|bat|cmd|sh|uc|java|rs|go|asm|s)$|(^|/)(Makefile|CMakeLists\.txt|[^/]*\.mk)$)", re.I)
code = [p for p in paths if CODE.search(p) and not (p.startswith(SENSITIVE) or p in SENSITIVE)]
if code:
    look.append(f"Adds or changes code ({len(code)} file(s), e.g. `{code[0]}`): read it before anyone builds or runs it")
OFF_TREE = [p for p in paths if not p.startswith(("games/", "data/", "playbook/", "templates/", "research/")) and p not in ("DIRECTORY.md", "README.md", "CONTRIBUTING.md")]
OFF_TREE = [p for p in OFF_TREE if not (p.startswith(SENSITIVE) or p in SENSITIVE)]
if OFF_TREE:
    look.append("Files outside the usual folders (games/, data/, playbook/): " + ", ".join(f"`{p}`" for p in OFF_TREE[:4]))
if not sens and not bins and not code and not OFF_TREE:
    ok.append("Only docs and data files changed")

# Content of added lines
PATTERNS = [
    ("block", r"(?i)(ghp_|gho_|github_pat_|xox[bpa]-|AKIA[0-9A-Z]{12,}|-----BEGIN [A-Z ]*PRIVATE KEY)", "Looks like a token or private key"),
    ("block", r"(?i)\b(curl|wget|iwr|invoke-webrequest)\b[^\n|]*\|\s*(sh|bash|iex|powershell)", "Pipes a download straight into a shell"),
    ("look", r"[A-Za-z]:\\Users\\[^\\<%\s]+|/home/[a-z_][a-z0-9_-]+/|/Users/[A-Za-z0-9_-]+/", "Local path with a username"),
    ("look", r"[A-Za-z0-9._%+-]+@(?!users\.noreply\.github\.com)[A-Za-z0-9.-]+\.[a-z]{2,}", "Email address"),
    ("look", r"(?i)discord(app)?\.(gg|com/invite)/", "Discord invite link"),
    ("look", r"(?i)\b(crack(ed)?|keygen|warez|torrent|no-?cd|drm[- ]?(free|remov|bypass)|anti-?cheat bypass)\b", "Piracy or DRM wording"),
    ("look", r"(?i)(ignore (all|any|previous) (instructions|rules)|you are (an? )?(ai|assistant|agent)\b|system prompt)", "Text aimed at AI agents"),
    ("look", r"—", "Em dash (house style says no)"),
]
for level, pat, label in PATTERNS:
    hits = [l.strip()[:100] for l in added if re.search(pat, l)]
    if hits:
        (block if level == "block" else look).append(f"{label} ({len(hits)}x), e.g. `{hits[0]}`")

# Directory
if any(p == "data/directory.yaml" for p in paths):
    if "DIRECTORY.md" in paths:
        ok.append("`data/directory.yaml` changed and `DIRECTORY.md` was regenerated")
    else:
        look.append("`data/directory.yaml` changed but `DIRECTORY.md` was not regenerated")
    if re.search(r"^\+\s*qa:\s*(automated|verified-playthrough)", diff, re.M):
        look.append("Claims QA level `automated` or `verified-playthrough`: check the evidence in the description")

# Account age
if created:
    try:
        age = (datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))).days
        if age < 7:
            look.append(f"Author's GitHub account is {age} day(s) old")
    except ValueError:
        pass

verdict = "do not merge" if block else ("needs a human look" if look else "looks safe to merge")
icon = {"do not merge": "🛑", "needs a human look": "👀", "looks safe to merge": "✅"}[verdict]
out = ["<!-- pr-check -->", f"### Automated PR check: {icon} {verdict}", ""]
for title, items in (("Blocking", block), ("Worth a look", look), ("Fine", ok)):
    if items:
        out.append(f"**{title}**")
        out += [f"- {i}" for i in items]
        out.append("")
out.append(f"{len(paths)} file(s), +{sum(f.get('additions', 0) for f in files)}/-{sum(f.get('deletions', 0) for f in files)}. "
           "The directory itself is validated by the `directory` check. _Rules only, no AI; a maintainer merges._")
print("\n".join(out))
