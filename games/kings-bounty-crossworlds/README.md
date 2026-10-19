# King's Bounty: Crossworlds (2010)

| | |
|---|---|
| Engine | TheEngine |
| Versions tested | Steam App 63910, manifest build ID 7254336; executable version string unknown |
| Projects | None found in the searches listed below |
| QA level | none |
| Last updated | 2026-10-20 |

## Where things stand

There is no ready-to-use co-op campaign project in the sources searched so far, and the Steam listing describes Crossworlds as single-player. Friends cannot currently join a shared campaign through the stock game or a co-op mod from this research. The executable contains TCP and Lua network APIs, but the only configured endpoint found is named `debug_server`; this is not evidence of a playable multiplayer mode.

## Existing work

- No Crossworlds co-op project surfaced in bounded searches of GitHub, ModDB, Nexus, Steam, the Co-op Anything directory, and the official Fulqrum forum index.
- [nPwka Engine Extension](https://www.nexusmods.com/kingsbountycrossworlds/mods/38) adds a leaderboard and engine/modder features, but does not advertise co-op or campaign synchronization. Its author requires permission for public mods that depend on or build on its features.
- [Fantasy Wars](https://www.pcgamingwiki.com/wiki/Fantasy_Wars) and [Elven Legacy](https://www.pcgamingwiki.com/wiki/Elven_Legacy_Collection) are same-engine multiplayer comparison targets, not Crossworlds co-op mods.
- The open claim and research task is [issue #61](https://github.com/cranebeaker/coop-anything/issues/61).

## How the game works (for co-op)

Crossworlds combines real-time overworld exploration with turn-based tactical battles. The installed Steam copy has script files inside ZIP-readable `.kfs` session archives and includes `LuaIDE.dll`. A bounded search of text-like session scripts did not find network or multiplayer terms.

Static inspection of `kb.exe` found Winsock imports and calls, Lua globals named `NetListen`, `NetConnect`, `NetSend`, and `NetConnected`, and engine server/client symbols. The inspected `data/app.ini` sets `~debug_server` to `TCP:0.0.0.0:51515`; no listener was started and no port was exposed. The endpoint and API have not been traced far enough to show how a game client could join, whether Lua can receive messages, or whether campaign state is replicated. Treat this as engine/debug networking until proven otherwise.

The release uses TheEngine, also used by Fantasy Wars and Elven Legacy. Their multiplayer modes may help explain the engine networking layer, but no source or matching local multiplayer build was available for comparison.

## What we changed

Research notes only. No game files were modified, no mod was installed, and no code or game assets were committed.

## QA

No co-op client or gameplay test exists yet. The QA level is `none`.

## How to play

There is no co-op package to install, host, or join yet. Do not expose the configured `debug_server` port as a multiplayer workaround; its protocol and purpose have not been audited.

## Known issues

The game has no confirmed shared campaign, player joining, synchronized battles, or shared save support. The presence of TCP symbols alone does not provide those features.

## Next steps

Continue reverse engineering the Lua TCP API and its relationship to the `debug_server` configuration, then compare with a same-engine multiplayer game if an authorized install is available. Map campaign state and save/load before choosing a co-op design. Track findings in [NOTES.md](NOTES.md) and [issue #61](https://github.com/cranebeaker/coop-anything/issues/61).

