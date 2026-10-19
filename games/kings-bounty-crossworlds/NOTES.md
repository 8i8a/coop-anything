# King's Bounty: Crossworlds research notes

Status: initial public triage only. No game install was inspected, no files were downloaded from game/mod sites, and no mod was installed or run.

## Observations

- Steam identifies App 63910 as King's Bounty: Crossworlds, released 2010-09-17. The store page lists Single-player and describes the Armored Princess campaign plus the Champion of the Arena and Defender of the Crown mini-campaigns. Source: https://store.steampowered.com/app/63910/
- Co-op Anything's current `DIRECTORY.md` and `games/` folder have no King's Bounty / Crossworlds entry.
- The Nexus listing for nPwka Engine Extension describes a DLL engine extension for Crossworlds with a Hardcore mode, online leaderboard, reserve slots, speed controls, PNG screenshots and Lua/modder additions. It explicitly describes the online component as a ladder; it does not advertise co-op or player/state synchronization. It requires Crossworlds 1.3.1 (build 6171), supports English and Russian builds, and says public mods depending on or building on its features require the author's permission. Private development/testing is allowed. Source: https://www.nexusmods.com/kingsbountycrossworlds/mods/38
- ModDB lists multiple active content/mod projects (including Hirao's A New Phase and Undead Resurrection) but no co-op project appeared in the Crossworlds mods listing. This is a bounded search, not proof none exists. Source: https://www.moddb.com/games/kings-bounty-crossworlds/mods
- ModDB identifies the engine as Custom. PCGamingWiki's engine page identifies Crossworlds as using TheEngine. The user's installed executable has not been inspected, so engine identity for this particular build remains unverified.

## Derived

- No ready-to-use online co-op solution surfaced in this initial search. If no hidden project or usable branch is found, this is likely a build-from-zero path rather than a revive path.
- The game is a real-time overworld plus turn-based tactical battles; a useful co-op design must define turn/control ownership and synchronize hero, battle, quest, inventory, and save state. This is design analysis, not an implementation finding.
- nPwka Engine Extension may be a useful research lead for understanding the native hook and script-extension surface, but its current published features are not multiplayer. Public dependency/derivative restrictions need to be respected.

## Guesses

- None recorded.

## Unknown

- Exact installed store/build, executable hash, and whether it matches 1.3.1 (build 6171).
- Whether any unpublished, non-default-branch, or private co-op attempt exists.
- Whether the game binary contains any unused network or multiplayer code.
- How campaign and combat state are represented in the installed build, and whether scripts are directly modifiable without a native extension.
- Whether nPwka's extension source is available; the Nexus page presents a binary distribution, not a source repository.
- Feasible player count, network transport, join timing, save ownership, desync handling, and compatibility with existing gameplay mods.

## Searches completed

- Co-op Anything `DIRECTORY.md` and `games/` on the repository's current `main` branch: no match for King's Bounty or Crossworlds.
- Web queries: `King's Bounty: Crossworlds co-op mod`, `multiplayer mod`, `coop campaign`, plus Russian spellings `Перекрёстки миров` and `мультиплеер кооператив`.
- GitHub web search queries for Crossworlds + multiplayer/co-op, and repository issue/PR query pages for King's Bounty: no matching work surfaced. Authenticated `gh issue list` / `gh pr list` were not run because AGENTS.md requires owner approval before using GitHub accounts.
- After the owner authorized account use, GitHub connector searches for `repo:cranebeaker/coop-anything King's Bounty` returned no issues or PRs; public branch listing returned only `main`. The repository's issue template specifies the `in-progress` label.
- The required claim issue has not yet been posted. The available GitHub connector cannot create issues in this repository (403, resource not accessible by integration), and the in-app GitHub page redirects to sign-in. No credentials were entered or exposed. A local branch `game/kings-bounty-crossworlds` exists; a fork has not been created.
- Follow-up: the owner authorized GitHub account use; claim issue [#61](https://github.com/cranebeaker/coop-anything/issues/61) was created through the signed-in GitHub web session, and the owner's fork is now created. GitHub CLI is not installed; authenticated connector write was denied, so fork branch publication is being done with the signed-in Git remote instead.
- ModDB Crossworlds mods/downloads pages and the official Fulqrum Crossworlds forum index: searched for multiplayer/co-op; results surfaced content mods and campaign/modding discussions, not a co-op attempt.
- Steam Crossworlds store/community search: the store lists Single-player; general community results did not surface a co-op project.

## Next steps, pending owner authorization

1. Push this branch to the personal fork; then update the claim issue with the fork branch URL.
2. Inspect the user's own game install only after they provide/identify it; record store/build and executable SHA-256 without modifying the install or saves.
3. Search GitHub repositories, forks, branches, releases, and historical/community sources more deeply; check same-engine sibling games and modding/tooling.
4. If no usable co-op is found, inspect a separate test copy and map the script/archive/save/level-loading systems before choosing a network model.

