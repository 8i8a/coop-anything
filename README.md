# coop-anything

**Crowd-sourcing co-op for every single-player classic, one AI agent at a time.**

Most loved single-player games already have a co-op attempt somewhere: an alpha from
2019, a Discord full of bug reports, a fork that synced the bosses but not the
cutscenes. They are *so close*. What's missing is the boring last 20%: fixing the bugs,
testing every level, making it easy to install.

That last 20% is exactly what coding agents are good at, if they know where to look.
This repo is the shared playbook and the shared map:

- **[AGENTS.md](AGENTS.md)**: instructions written *for your AI agent* (Claude Code,
  Codex, Gemini CLI, Cursor, anything). Point it at this repo and a game you own, and it
  follows the same playbook: research what exists, set up a safe test copy, reverse
  engineer, fix, **test with bots**, ship.
- **[DIRECTORY.md](DIRECTORY.md)**: every co-op mod, fork and port we know of for
  single-player games, with what it really syncs and how well it's been tested. Plus the
  open gaps.
- **[playbook/](playbook/)**: the techniques that worked, from real projects: finding
  abandoned mods, mining a mod's Discord for bugs, decompiling with Ghidra, reusing
  co-op work from games on the same engine, Steam relay networking without port
  forwarding, and automated QA with real game clients.

Inspired by the way [photo-frame-dashboard](https://github.com/wesbos/photo-frame-dashboard)
turned owners' agents into contributors: everyone's agent does the work on their own
machine and sends the notes back as a pull request, so the next person starts further
ahead.

[![Support me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cranebeaker)

## Use it

1. Own the game. Install it normally.
2. Clone this repo and open it with your coding agent.
3. Tell it something like: *"Read AGENTS.md. I want to play Vampire: Bloodlines in
   co-op. Start with triage and research, and ask me before installing anything."*
4. When it learns something, it updates the directory and writes up the game in
   `games/`. You check the diff and open a pull request.

You don't need to finish a whole game. A corrected directory entry, a bug list mined
from a mod's Discord, or one new test is a useful PR.

## The QA flag is the point

Anyone can claim a mod "works". Here every entry carries a **QA level**:

| QA | Meaning |
|---|---|
| untested | only the author's claims |
| player reports | people say they played it |
| **automated tests** | a script drove real game clients and checked shared state |
| **verified playthrough** | someone finished the campaign in co-op and wrote it up |

The playbook's rule is that agents prove things with bots inside the game, not by asking
you to playtest. See [playbook/automated-qa.md](playbook/automated-qa.md).

## Games worked on with this playbook so far

| Game | What was done | Write-up |
|---|---|---|
| Deus Ex (2000) | Revived the HX co-op mod: fix package, Steam relay, automated test suite | [games/deus-ex](games/deus-ex/README.md) |
| Dungeon Keeper (1997) | Shared-keeper co-op on KeeperFX, Steam relay networking | [games/dungeon-keeper](games/dungeon-keeper/README.md) |
| S.T.A.L.K.E.R. Shadow of Chernobyl / Clear Sky | Fix patch for Shadow of COOP, plan to finish Clear COOP | [games/stalker](games/stalker/README.md) |
| Fallout: New Vegas | Quest sync layer on top of NV:MP, in progress | [games/fallout-new-vegas](games/fallout-new-vegas/README.md) |
| Zelda: Ocarina of Time | Fixes for a fully synced Ship of Harkinian co-op fork | [games/ocarina-of-time](games/ocarina-of-time/README.md) |

Add yours.

## Rules

- You must own the games. No game files, cracks or decompiled closed source in this repo.
- No personal info in PRs. No tokens, no private Discord content beyond bug summaries.
- Credit the people whose mods you build on, and give fixes back to their projects.
- Single-player and co-op only: nothing that cheats in other people's multiplayer games.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The directory is generated from
`data/directory.yaml` by `tools/build_directory.py`, and CI checks every PR.

License: MIT.
