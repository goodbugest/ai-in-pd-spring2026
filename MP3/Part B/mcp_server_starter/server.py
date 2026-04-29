"""MiniClaw MCP server — STARTER (FastMCP).

This is a minimal working MCP server that exposes the MiniClaw RAG as a
single tool, ``query_miniclaw_rag``. Copy this file into your own
``MP3/Part B/mcp_server/`` directory, edit the import path on line 26,
and you're running. Every tool invocation is logged to ``logs/server.log``.

Run from the repo root (for testing):

    python "MP3/Part B/mcp_server_starter/server.py"

For real use, point your AI host at this script — see ``host_configs/``
for example configs (Claude Desktop, VS Code Copilot agent mode, Cursor).
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime
from pathlib import Path

# ── Make the starter RAG importable ──────────────────────────────────────
_HERE = Path(__file__).resolve().parent
_RAG_DIR = _HERE.parent / "miniclaw_starter_rag"
sys.path.insert(0, str(_RAG_DIR))

from query_miniclaw_rag import query_miniclaw_rag as _rag_query  # noqa: E402

# ── Logging ─────────────────────────────────────────────────────────────
LOG_DIR = _HERE / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_PATH = LOG_DIR / "server.log"

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
# FastMCP pings PyPI for version info via httpx on startup; mute that noise
# so the log only contains MiniClaw tool calls.
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger("miniclaw-mcp")

# ── MCP server ──────────────────────────────────────────────────────────
# fastmcp ships its own FastMCP class; mcp.server.fastmcp also re-exports
# one. Try both so the starter works against either install.
try:
    from fastmcp import FastMCP  # preferred (standalone fastmcp package)
except ImportError:  # pragma: no cover
    from mcp.server.fastmcp import FastMCP  # bundled with mcp

mcp = FastMCP("miniclaw-knowledge")


@mcp.tool()
def query_miniclaw_rag(question: str, n_results: int = 3) -> dict:
    """Search the MiniClaw / ACME project knowledge base.

    Searches ACME Robotics' internal knowledge base for the MiniClaw
    project — manufacturing capabilities (Prusa MK4S print shop, achievable
    tolerances, FilaTech PolyPro PLA test data), previous product history
    (WidgetBot 2.0 gear test report, GripperBot specs, BigClaw teardown
    notes), engineering design standards, vendor information, and project
    status. Use this whenever the user asks about the MiniClaw project,
    ACME's capabilities, or company-specific data.

    Args:
        question: Natural-language question about the MiniClaw project,
            ACME's standards, BigClaw reference data, vendor info, or print
            shop capabilities.
        n_results: Number of chunks to retrieve (1-10, default 3).
    """
    logger.info(
        "TOOL_CALL | query_miniclaw_rag | question=%r n_results=%s",
        question, n_results,
    )
    try:
        result = _rag_query(question, n_results=n_results)
    except Exception as e:  # noqa: BLE001
        logger.exception("TOOL_ERROR | query_miniclaw_rag")
        return {"error": f"{type(e).__name__}: {e}", "chunks": [], "summary": ""}

    logger.info(
        "TOOL_RESULT | query_miniclaw_rag | chunks=%d top=%s",
        len(result.get("chunks", [])),
        result["chunks"][0]["doc_id"] if result.get("chunks") else "(none)",
    )
    return result


if __name__ == "__main__":
    logger.info("Starting MiniClaw MCP server (pid=%s) at %s", __import__("os").getpid(),
                datetime.now().isoformat(timespec="seconds"))
    mcp.run()
