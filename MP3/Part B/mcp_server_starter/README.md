# MCP Server Starter — MiniClaw Knowledge

A working MCP server you can copy as a starting point for the Part B
deliverable. Wraps `query_miniclaw_rag` from the starter RAG package and
logs every invocation to `logs/server.log`.

## What you do

1. **Copy** this whole directory to `MP3/Part B/mcp_server/` (drop the
   `_starter` suffix). The grader expects to find your working server at
   the un-suffixed path.
2. **Build the RAG index** if you haven't already:
   ```bash
   python "MP3/Part B/miniclaw_starter_rag/build_index.py"
   ```
3. **Install dependencies:**
   ```bash
   pip install -r "MP3/Part B/mcp_server/requirements.txt"
   ```
4. **Smoke-test the server runs:**
   ```bash
   python "MP3/Part B/mcp_server/server.py"
   ```
   It will sit listening on stdio. Kill with `Ctrl+C`. Check
   `MP3/Part B/mcp_server/logs/server.log` — you should see a "Starting
   MiniClaw MCP server" line.
5. **Wire it into your AI host.** See `host_configs/` for examples.
6. **Drive it from your host.** Ask MiniClaw-flavored questions ("what's
   the ACME print-shop tolerance on press fits?") and confirm the host
   shows `query_miniclaw_rag` being called.

## Required deliverables

The graded evidence is in three files:

| Evidence | Where it lives |
|----------|---------------|
| Server log with ≥3 tool invocations | `mcp_server/logs/server.log` |
| 2–3 host UI screenshots showing tool calls | `mcp_server/screenshots/` |
| Markdown export of one full host conversation | `mcp_server/conversation_export.md` |

If any of those is missing, the deliverable is incomplete.

## Picking a host

| Host | Status as of April 2026 | Notes |
|------|-------------------------|-------|
| **GitHub Copilot agent mode (VS Code)** | Recommended — already in your stack | MCP support is stabilizing; verify the current `.vscode/mcp.json` format |
| **Claude Desktop** | Most stable MCP support | Easiest if Copilot agent mode is giving you trouble |
| **Cursor** | Good MCP support | Free tier is limited; works fine for the assignment |
| **Continue.dev** | Open-source, accepted | Use if you prefer a fully local setup |

You may use **any one** of these. Document which you used in your
reflection so the grader knows what to expect in the screenshots.

## Stretch — add a second tool

Worth credit toward the 15-pt MCP rubric. Examples:

- `render_scad(code: str) -> dict` — runs OpenSCAD CLI on the code and
  returns a base64 PNG. Lets the AI generate-and-look at parametric
  geometry.
- `check_lewis_stress(...)` — wraps your gear stress calculator from MP1
  Part B. Lets the AI verify a tooth design without leaving the host.

If you add a second tool, make sure your `server.log` shows the AI
choosing between tools on different questions.
