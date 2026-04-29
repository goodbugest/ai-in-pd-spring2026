# MP3 Part B — Grading Rubric

**Total:** 50 points
**Due:** Monday, May 11, 2026 at 11:59 PM

Rubric is organized by deliverable to match the assignment structure:

| Deliverable | Points |
|---|---|
| 1. One Polished Skill | 15 |
| 2. MCP Server with RAG Integration | 15 |
| 3. CAD Interaction Documentation | 15 |
| 4. Reflection | 5 |
| **Total** | **50** |

### How partial credit works

Each criterion is independently checkable. Item points may be fractional (0.5 increments) when a criterion has clearly partial states. Each deliverable's score is the sum of its component criteria.

> **Soft cap:** If `mcp_server/logs/server.log` does not exist or shows zero tool invocations, the MCP Server deliverable is capped at 50% (7.5 pts) regardless of supporting work. Logs are the visibility evidence that the stack actually ran.

### Pillar mapping (for course-level grade record)

The pillar weights for MP3 are: Tools & Integration ★★★, Centaur Engineering ★★, Evaluation & Trust ★★, Goal & Direction ★★, Context Management ★★. The deliverable-based rubric below maps naturally to these pillars — Skills and MCP server primarily address Tools & Integration and Context Management; CAD interaction primarily addresses Centaur Engineering; Reflection primarily addresses Evaluation & Trust and Goal & Direction. The deliverable score is the grade of record.

---

## 1. One Polished Skill (15 pts)

Evidence path for all criteria: `MP3/Part B/skills/*.md`

| # | Pts | Criterion |
|---|-----|-----------|
| S.1 | **1.0** | A markdown skill file exists in `MP3/Part B/skills/`. Zero if only `skills_starter/` content is present, unmodified. |
| S.2 | **1.0** | YAML front matter present with `name` + `description`. Half credit (0.5) if front matter exists but is incomplete. |
| S.3 | **2.0** | "When to use this skill" section names trigger conditions specific to MiniClaw work — not generic engineering review language. Half credit (1.0) if present but generic. |
| S.4 | **3.0** | Workflow steps (3–7 numbered) describe an actual procedure with MiniClaw-specific anchors (e.g., "consult ACME-ENG-001 for module / tooth limits", "compare to BigClaw teardown reference"). Half credit (1.5) if steps are present but generic. |
| S.5 | **2.0** | "What to flag" section names ≥ 2 specific patterns the skill should catch (e.g., PLA interlayer stress under-spec, tolerance tighter than print shop can hold). Half credit (1.0) if patterns are listed but not specific to MiniClaw. |
| S.6 | **1.5** | "What NOT to do" includes ≥ 1 substantive anti-pattern. Half credit (0.75) for trivial anti-patterns (e.g., "don't guess"). |
| S.7 | **2.0** | Skill `description` in YAML reads as a clear statement of *intent* (what the skill is for, who/when it triggers — not a description of its structure). Half credit (1.0) if the description is structural rather than purposive. |
| S.8 | **2.5** | At least one skill refers to the project corpus **by name** at least once — cites a doc ID, an ACME standard (e.g., `ACME-ENG-001`), or a named project (WidgetBot 2.0, BigClaw). Half credit (1.25) if a corpus reference exists but is vague ("our internal docs"). |

---

## 2. MCP Server with RAG Integration (15 pts)

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| M.1 | **2.0** | `mcp_server/server.py` exists, runs without raising on import, and exposes at least one `@mcp.tool`-decorated function. Half credit (1.0) if the file exists but won't import (missing dep, syntax error). | `mcp_server/server.py` |
| M.2 | **2.0** | The exposed tool's `description` is specific to MiniClaw — names the corpus content (print shop, FilaTech PLA, BigClaw teardown, gear standards). Half credit (1.0) if the description is the unmodified starter description. | docstring in `server.py` |
| M.3 | **2.0** | Tool is backed by working RAG — student's MP2 RAG or the provided `miniclaw_starter_rag/`. Verified by a successful query on the bench. Half credit (1.0) if the RAG path resolves but returns empty chunks. | `query_miniclaw_rag.py` import + smoke test |
| M.4 | **3.0** | Server log shows **≥ 3 real tool invocations** with non-trivial questions (not "test", not "hi"). Award 1.0 per qualifying invocation up to 3. | `mcp_server/logs/server.log` |
| M.5 | **2.0** | At least one screenshot from the host UI showing a tool call happening in context — the host's "calling tool: query_miniclaw_rag" indicator visible alongside an engineering question. Half credit (1.0) if the screenshot exists but the tool-call indicator is not visible or cropped out. | `mcp_server/screenshots/` |
| M.6 | **1.0** | A copied/exported exchange (markdown or text) showing the AI consulting the tool to answer one real engineering question end-to-end. | `mcp_server/conversation_export.md` or equivalent |
| M.7 | **1.5** | The MCP tool returns chunks from the actual MiniClaw / ACME corpus — `doc_id` values like `ACME-ENG-001`, `ACME-MFG-002`, etc. appear in the server log or conversation export. | `server.log` + conversation export |
| M.8 | **1.5** | At least one host conversation shows the AI using a retrieved chunk to answer a question it could not have answered from training alone (a MiniClaw-specific number, vendor name, or internal standard). Half credit (0.75) if the AI consulted the tool but the answer wasn't grounded in the chunk. | conversation export + `server.log` |

---

## 3. CAD Interaction Documentation (15 pts)

Evidence path for all criteria: `MP3/Part B/cad_review/cad_interaction.md` + `cad_review/*.png`

| # | Pts | Criterion |
|---|-----|-----------|
| A.1 | **1.5** | Subassembly chosen and named (gear, jaw arm, housing, base). CAD tool used is documented. |
| A.2 | **2.0** | **Checkpoint 1 screenshot** committed and shows real CAD work (not a stock image, not a sketch traced from elsewhere). |
| A.3 | **2.0** | **Checkpoint 2 screenshot** committed and shows a substantive change from Checkpoint 1 (parameter swept, feature added/removed, geometry altered) — not just a different camera angle. |
| A.4 | **2.0** | At each checkpoint: a documented exchange with the AI host showing prompt sent (with the screenshot in context) and response captured. Award 1.0 per checkpoint that has both. |
| A.5 | **1.5** | The writeup names **what changed** between checkpoints and explicitly attributes the change to AI feedback, or names the human reason for overruling the AI. |
| A.6 | **1.5** | Skill loaded **and** MCP server connected during the CAD review (visible in screenshots or stated in writeup with a corresponding log entry). Half credit (0.75) if only one of the two is documented. |
| A.7 | **2.0** | The CAD-review writeup states the goal of the iteration up front (what the student set out to do) before the checkpoints, so the AI's contribution is gradeable against intent. Half credit (1.0) if the goal is implied but not stated. |
| A.8 | **2.5** | The writeup contains at least one moment where the student **disagreed with or overrode the AI** and explained why. This is the centaur signal — human judgment applied to AI output. Half credit (1.25) if an override is present but no explanation is given. |

---

## 4. Reflection (5 pts)

Evidence path: `MP3/Part B/reflection.md`

| # | Pts | Criterion |
|---|-----|-----------|
| R.1 | **0.5** | `reflection.md` exists at `MP3/Part B/reflection.md`. |
| R.2 | **1.0** | "What did you productize?" names specific work (a particular check, a particular query) that used to require the student and now runs through the stack. Half credit (0.5) for generic claims. |
| R.3 | **1.5** | "Where does your stack break?" names ≥ 1 concrete failure mode **with an example query** that exposes it. Half credit (0.75) if limitations are listed but no example is given. |
| R.4 | **2.0** | **Trust ledger:** one place the skill helped the AI succeed (1.0 pt) and one place the AI did something wrong that the skill didn't catch (1.0 pt). Both must reference specific moments — a transcript, a CAD checkpoint, or a logged query — not hypotheticals. |

---

## Stack hygiene (silent prerequisite — not separately graded)

These don't earn points but missing them triggers the caps above:

- `mcp_server/server.py` and `mcp_server/requirements.txt` committed
- `mcp_server/logs/server.log` committed (grader must be able to read it)
- `mcp_server/README.md` documents the chosen host with a copyable config snippet
- `cad_review/cad_interaction.md` exists and references screenshots by relative path
- `skills/` contains student skill markdown files (not just the unmodified `skills_starter/`)

---

## "Be an Engineer" tiebreaker

When two students sit on the boundary between scores, the deciding question is:

> If you cannot tell the grader exactly what your AI did during a session and how you know, you have not finished the assignment.

The student who can walk the grader through their `server.log`, identify which tool call corresponds to which screenshot, and explain why a particular AI response was trusted or overridden is the student who earns the higher score.
