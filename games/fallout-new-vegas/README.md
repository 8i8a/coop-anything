# Fallout: New Vegas (2010)

| | |
|---|---|
| Engine | Gamebryo (xNVSE plugins for native hooks) |
| Projects | NV:MP (multiplayer: players, NPC motion, combat; closed netcode); a story sync layer in progress |
| QA level | automated (sync layer components); none (full co-op) |
| Last updated | 2026-10-16 |

## Where things stand

NV:MP lets people play in the same world, but quests are client-side and quest actors
are deliberately not synced. A separate, host-authoritative quest and story sync layer
(an xNVSE plugin) is being built to run next to NV:MP. First milestone passed in game:
a quest stage set on the host is applied on a client through the sync layer.

## How the game works (for co-op)

- Quest logic runs as stage result scripts in the ESM. Sync captures the effects of a
  stage on the host as one transaction and applies it on clients without re-running the
  scripts.
- NV:MP's story server has no quest sync; its client marks quest actors as local.

## QA

- A JSON-RPC bridge plugin inside the game (`exec`, `waitFor`, `state`) lets tests drive
  real game copies; world snapshots split into shared and per-player state are diffed.
- Stage sweep: for each quest stage, expected effects (parsed from the ESM), captured
  effects and observed state are compared.
- Running two copies on one PC needs the single-instance checks handled (named mutex,
  FindWindow on the game's window class), done in-process.
