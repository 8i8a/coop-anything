# The Legend of Zelda: Ocarina of Time (1998)

| | |
|---|---|
| Engine | Ship of Harkinian (native PC port from the decompilation) |
| Projects | Anchor (Ship of Harkinian co-op, merged upstream 2026); OOT True Co-op (enemy sync fork); Shipwright-Online (host-authority fork with bosses, puzzles, songs) |
| QA level | community-reports (Anchor); none (forks) |
| Last updated | 2026-10-16 |

## Where things stand

Anchor syncs players, inventory and world flags but each player fights their own copy of
the enemies. Shipwright-Online goes further (host authority for enemies, bosses,
switches, boulders, songs) with known bugs listed by its author (docs are in German).
A batch of fixes for its known bugs was written but only checked by code review and
compilation, since no two-client test exists yet.

## Notes for the next agent

- The decompilation means the networking can live in the game code; the hard part is
  deciding authority per actor (host owns enemies and bosses, players own themselves).
- Building on Windows: if `CMAKE_TOOLCHAIN_FILE` points at an Android NDK in your
  environment, unset it before configuring.
- **Not yet proven:** any of the new fixes in a two-client session. Build the two-client
  harness first ([playbook/automated-qa.md](../../playbook/automated-qa.md)).
