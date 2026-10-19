# King's Bounty: Crossworlds research notes

Status: research in progress. Static inspection was done on an isolated copy of the owner's Steam install; the original install and saves were not modified. No mod was installed or run. No game files or assets are included here.

## Observations

- Steam identifies App 63910 as King's Bounty: Crossworlds, released 2010-09-17. The store page lists Single-player and describes the Armored Princess campaign plus the Champion of the Arena and Defender of the Crown mini-campaigns. Source: https://store.steampowered.com/app/63910/
- Co-op Anything's current `DIRECTORY.md` and `games/` folder have no King's Bounty / Crossworlds entry.
- The inspected Steam installation's manifest reports build ID `7254336`. The executable has no FileVersion or ProductVersion string; treat the manifest ID as a Steam depot build identifier, not as the in-game version. The exact executable identity is recorded privately in ignored `local/identity.md`.
- Static PE import inspection of that `kb.exe` found Winsock imports for initialization/cleanup and TCP socket operations, including `socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`, and `select` (several are imported by ordinal). A direct x86 call-site scan found calls to multiple imported socket functions, including socket creation, bind/listen/accept, connect and send. The binary also registers Lua globals `NetListen`, `NetSend`, `NetConnect`, and `NetConnected`, and contains engine client/server classes (`serv_server_tcp_c`, `serv_client_tcp_c`, `ModuleLogicServer_c`) and game-logic commands (`SPAWN_CLIENT`, `cmd_server_addclient_c`). The inspected `data/app.ini` sets `~debug_server` to `TCP:0.0.0.0:51515`; a GOG forum post shows the same setting in a Crossworlds app.ini. This points to a debug service as one likely consumer of the TCP layer, not a user-facing multiplayer mode. No remote listener was started or port exposed. Sources: https://www.gog.com/forum/kings_bounty_series/cant_install_update_for_crossworlds_goty/post2 and https://learn.microsoft.com/en-us/windows/win32/winsock/winsock-functions
- The quick search across text-like `.lua`, `.lu`, and `.script` entries in the installed `.kfs` archives found no network/multiplayer terms. It did find Lua scripts in `sessions/addon/ses.kfs` (221), `sessions/orcs/orcs.kfs` (63), `sessions/champion/champion.kfs` (30), and `sessions/defender/defender.kfs` (17). This is a bounded token search, not a full script/API analysis.
- The install contains `LuaIDE.dll`, and the session archives are ZIP-readable `.kfs` containers. No archives were modified or extracted into the public repository.
- The Nexus listing for nPwka Engine Extension describes a DLL extension with a Hardcore mode, online leaderboard, reserve slots, speed controls, screenshot changes and Lua/modder additions. It does not advertise co-op or player/state synchronization. It requires Crossworlds 1.3.1 (build 6171), supports English and Russian builds, and says public mods depending on or building on its features require the author's permission; private development/testing is allowed. Source: https://www.nexusmods.com/kingsbountycrossworlds/mods/38
- ModDB lists multiple Crossworlds content/mod projects but no co-op project surfaced in its mods listing. Bounded search only. Source: https://www.moddb.com/games/kings-bounty-crossworlds/mods
- TheEngine is identified as the engine for both Fantasy Wars and Elven Legacy. PCGamingWiki lists multiplayer for Fantasy Wars and lists LAN and hot-seat play for Elven Legacy; the latter's official internet service is shut down. Neither source establishes co-op campaign support in Crossworlds. Sources: https://www.pcgamingwiki.com/wiki/Fantasy_Wars and https://www.pcgamingwiki.com/wiki/Elven_Legacy_Collection
- A contemporary Elven Legacy preview reports that its multiplayer included LAN, Internet and hot-seat, and allowed custom multiplayer maps. This is an adjacent-engine research lead, not a claim that its multiplayer was co-op or that its code can be reused directly. Source: https://forumcontent.paradoxplaza.com/public/14648/PARADOX_DPAD10.pdf

## Derived

- No ready-to-use Crossworlds co-op solution surfaced in the searches listed below. The executable has a Lua-facing TCP API, but its configured endpoint is explicitly named `debug_server`. That API may be useful as a transport only after its receiver/callback semantics and relationship to the game session are traced; the imports and symbols alone do not prove campaign replication.
- The same-engine multiplayer games provide a practical comparison target for their client/server startup, state replication and network setup. Their multiplayer modes are not evidence that Crossworlds includes a playable multiplayer menu or shared campaign.
- The game is a real-time overworld plus turn-based tactical battles; any campaign co-op design must decide turn/control ownership and synchronize hero, battle, quest, inventory, and save state. This is design analysis, not an implementation finding.
- nPwka Engine Extension may help explain the native hook and script-extension surface, but its published features are not multiplayer. Respect the author's public derivative/dependency restrictions.

## Guesses

- None recorded.

## Unknown

- Whether Crossworlds' Lua TCP API can receive messages/callbacks in ordinary gameplay, and whether the debug server or game session can create remote game clients in this build.
- Whether those classes replicate hero, army, battle, quest and overworld state, or are only generic engine infrastructure.
- Whether any unpublished, non-default-branch, or private Crossworlds co-op attempt exists.
- How campaign and combat state are represented, which Lua/native APIs own them, and how save/load interacts with networked clients.
- Whether nPwka's extension source is available; its Nexus page presents a binary distribution, not a source repository.
- Feasible player count, network transport, join timing, save ownership, desync handling, and compatibility with existing gameplay mods.

## Searches completed

- Co-op Anything `DIRECTORY.md` and `games/` on `main`: no match for King's Bounty or Crossworlds.
- Web queries: `King's Bounty: Crossworlds co-op mod`, `multiplayer mod`, `coop campaign`, plus Russian spellings `Перекрёстки миров` and `мультиплеер кооператив`.
- GitHub web search queries for Crossworlds + multiplayer/co-op, and authenticated repository issue/PR searches for King's Bounty: no matching work surfaced. Public branch listing for the upstream repository showed only `main`.
- ModDB Crossworlds mods/downloads pages and the official Fulqrum Crossworlds forum index: searched for multiplayer/co-op; results surfaced content mods and campaign/modding discussions, not a co-op attempt.
- Steam Crossworlds store/community search: store listing says Single-player; general community results did not surface a co-op project.
- Static PE import/string inspection, a bounded x86 call-site scan for Winsock imports, and a bounded token scan of text-like scripts were run on the owner's isolated Steam copy. No game runtime test has been done, and the socket call paths have not yet been tied to the `debug_server` config or to campaign logic.
- Research searches for TheEngine sibling games found Fantasy Wars and Elven Legacy, both listed with multiplayer in PCGamingWiki; Elven Legacy LAN/hot-seat is a documented lead, while its online service is shut down.
- Required claim issue posted: https://github.com/cranebeaker/coop-anything/issues/61. Owner's fork and branch are https://github.com/8i8a/coop-anything/tree/game/kings-bounty-crossworlds. No pull request has been opened yet.

## Next steps

1. Trace `NetListen`/`NetConnect` to the `debug_server` config and determine their argument, receive/callback and lifecycle semantics; then check whether any game-session code can create a remote game client.
2. Compare the exposed script/API and session initialization paths with a same-engine multiplayer game (Fantasy Wars or Elven Legacy) if an authorized local copy is available.
3. Map campaign save/load, session transitions, and hero/battle state ownership before selecting a network model.
4. Continue searching project forks, branches, releases, archives, Steam discussions and Russian-language community sources for prior work.
5. Once a research phase is reviewable, prepare the game write-up/directory change, show the owner the diff, and open a draft PR as required by `AGENTS.md`.


