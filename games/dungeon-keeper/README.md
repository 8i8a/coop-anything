# Dungeon Keeper (1997)

| | |
|---|---|
| Engine | KeeperFX (open source C rewrite, GPLv2), lockstep netcode |
| Versions tested | KeeperFX alpha 1.4 builds with original GOG game data |
| Projects | KeeperFX "Archon mode" (upstream, several players per keeper); shared-keeper co-op branch built on it; Dungeon Keeper 2 has a separate project, dk2-coop |
| QA level | automated |
| Last updated | 2026-10-16 |

## Where things stand

Two players share one keeper (one dungeon, one hand each) through the campaign. A test
bot inside the exe plays levels and the campaign flow with two real game processes; runs
pass with 0 desyncs. Not yet played by people on separate PCs.

## Existing work

- Upstream KeeperFX is building "Archon mode" (multiple users controlling one player)
  through a series of UserState refactor PRs in 2026. Build on it rather than forking
  around it.
- Dungeon Keeper 2: dk2-coop (https://ciphercom.github.io/dk2-coop/).

## What we changed

- Ported the remaining per-player state (possession, hand, spell state, room placement,
  camera) to per-user state for archon co-op.
- Shared campaign flow: map, briefing, level, stats, back to the map, loss and retry.
- Steam networking provider on the Steamworks flat API (AppID 480), so players join by
  Steam invite or friends list. See [playbook/networking-steam-spacewar.md](../../playbook/networking-steam-spacewar.md).

## QA

- `-archontest` / `-archonflow` bot inside the game writes the same input packets a
  human would, asserts results and logs PASS/FAIL. Oracle: per-turn checksums on both
  sides must match (0 desyncs).
- Covered: in-level play, levels 1 to 4, loss and retry, menu path, clean quit and hard
  kill disconnects, Steam invite paths (on a mock `steam_api.dll`).
