# MP3 Part B — Grading Rubric

**Total:** 50 points
**Due:** Monday, May 11, 2026 at 11:59 PM

This rubric matches the reduced-scope assignment in
`MP3_The_Engineering_Stack.docx`. The grading philosophy is **substance
over format**: a working stack with logs and screenshots that prove the
AI used the student's tools beats a polished README with no evidence.

### How partial credit works

Each pillar's score is the **sum** of its component criteria. Every
criterion is independently checkable — the grader awards the listed
points per item, and the pillar total is whatever they add up to.
Item points may be fractional (0.5 increments) when the criterion has
clearly partial states.

> **Soft cap:** if `mcp_server/logs/server.log` does not exist or shows
> zero tool invocations, the **Tools & Integration** pillar is capped at
> 50% regardless of supporting work. Logs are the visibility evidence
> that the stack actually ran.

### Pillar weights

Per the course rubric, MP3's pillar weights are:

| Pillar | Weight | Points |
|--------|--------|--------|
| Tools & Integration | ★★★ | 20 |
| Centaur Engineering | ★★ | 10 |
| Evaluation & Trust | ★★ | 10 |
| Goal & Direction | ★★ | 5 |
| Context Management | ★★ | 5 |
| **Total** | | **50** |

The deliverables (Skill / MCP server / CAD interaction / Reflection)
contribute to multiple pillars — the rubric below is organized by pillar
because that's how the grade adds up, but each row tells you which
deliverable it pulls evidence from.

---

## Tools & Integration ★★★ (20 pts)

Largest pillar. The MCP server + skill are the productized engineering
work; this is what's being graded.

### MCP server (12 pts)

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| T.1 | **2.0** | `mcp_server/server.py` exists, runs without raising on import, and exposes at least one `@mcp.tool`-decorated function. Half credit (1.0) if the file exists but won't import (missing dep, syntax error). | `mcp_server/server.py` |
| T.2 | **2.0** | The exposed tool's `description` is **specific to MiniClaw** — names the corpus content (print shop, FilaTech PLA, BigClaw teardown, gear standards). Half credit (1.0) if the description is the unmodified starter description. | docstring in `server.py` |
| T.3 | **2.0** | Tool is backed by working RAG — student's MP2 RAG OR the provided `miniclaw_starter_rag/`. Verified by a successful query on the bench. Half credit (1.0) if the RAG path resolves but returns empty chunks. | `query_miniclaw_rag.py` import + smoke test |
| T.4 | **3.0** | Server log shows **≥ 3 real tool invocations** with non-trivial questions (not "test", not "hi"). Award `1.0` per qualifying invocation up to 3. | `mcp_server/logs/server.log` |
| T.5 | **2.0** | At least one **screenshot** from the host UI showing a tool call happening in context — the host's "calling tool: query_miniclaw_rag" indicator visible alongside an engineering question. Half credit (1.0) if the screenshot exists but the tool-call indicator is not visible / cropped out. | `mcp_server/screenshots/` |
| T.6 | **1.0** | A copied/exported exchange (markdown or text) showing the AI consulting the tool to answer one real engineering question end-to-end. | `mcp_server/conversation_export.md` or equivalent |

### Skill quality (8 pts)

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| T.7 | **1.0** | One markdown skill file exists in `MP3/Part B/skills/`. | `skills/*.md` |
| T.8 | **1.0** | YAML front matter present with `name` + `description`. The description is concrete enough that another AI session could decide when to invoke the skill. | front matter |
| T.9 | **1.5** | "When to use this skill" section names trigger conditions specific to MiniClaw work, not generic engineering review language. | skill body |
| T.10 | **2.0** | Workflow steps (3–7 numbered) describe an actual procedure with MiniClaw-specific anchors (e.g., "consult ACME-ENG-001 for module / tooth limits", "compare to BigClaw teardown reference"). Half credit (1.0) if steps are present but generic. | skill body |
| T.11 | **1.5** | "What to flag" section names ≥ 2 specific patterns the skill should catch (PLA interlayer stress under-spec, tolerance tighter than the print shop can hold, etc.). | skill body |
| T.12 | **1.0** | "What NOT to do" includes ≥ 1 substantive anti-pattern. Half credit (0.5) for trivial anti-patterns. | skill body |

---

## Centaur Engineering ★★ (10 pts)

Pulled from the CAD interaction documentation — does the evidence show
genuine human-AI collaboration on a real artifact, with iteration?

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| C.1 | **1.5** | Subassembly chosen and named (gear, jaw arm, housing, base). CAD tool used is documented. | `cad_review/cad_interaction.md` |
| C.2 | **2.0** | **Checkpoint 1 screenshot** committed and shows real CAD work (not a stock image, not a sketch traced from elsewhere). | `cad_review/*.png` |
| C.3 | **2.0** | **Checkpoint 2 screenshot** committed and shows a substantive change from Checkpoint 1 (parameter swept, feature added/removed, geometry altered) — not just a different camera angle. | `cad_review/*.png` |
| C.4 | **2.0** | At each checkpoint: a documented exchange with the AI host showing prompt sent (with the screenshot in context) and response captured. Award `1.0` per checkpoint that has both. | `cad_review/cad_interaction.md` |
| C.5 | **1.5** | The writeup names **what changed** between checkpoints and explicitly attributes the change to AI feedback or names the human reason for overruling the AI. | `cad_review/cad_interaction.md` |
| C.6 | **1.0** | Skill loaded **and** MCP server connected during the CAD review (visible in screenshots or stated in writeup with a corresponding log entry). Half credit (0.5) if only one of the two is documented. | screenshots + `server.log` |

---

## Evaluation & Trust ★★ (10 pts)

Pulled from the reflection + the trust ledger + honest accounting in
the CAD review.

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| E.1 | **1.0** | `reflection.md` exists at `MP3/Part B/reflection.md`. | `reflection.md` |
| E.2 | **2.0** | "What did you productize?" — names specific work (a particular check, a particular query) that used to require the student and now runs through the stack. Half credit (1.0) for generic claims. | `reflection.md` |
| E.3 | **2.0** | "Where does your stack break?" — names ≥ 1 concrete failure mode with an example query that exposes it. Half credit (1.0) if the limitations are listed but no example is given. | `reflection.md` |
| E.4 | **3.0** | **Trust ledger**: one place the skill helped the AI succeed (1.5 pts) and one place the AI did something wrong that the skill didn't catch (1.5 pts). Both must reference specific moments — a transcript, a CAD checkpoint, a logged query — not hypotheticals. | `reflection.md` |
| E.5 | **2.0** | The CAD-review writeup contains at least one moment where the student **disagreed with or overrode the AI** and explained why. This is the centaur signal — graded here as Eval & Trust evidence. | `cad_review/cad_interaction.md` |

---

## Goal & Direction ★★ (5 pts)

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| G.1 | **1.5** | Skill front matter `description` reads as a clear statement of *intent* (what the skill is for, who/when it triggers). Half credit (0.75) if the description is descriptive of structure rather than purpose. | skill front matter |
| G.2 | **1.5** | "What's the obvious next move for MP4?" answer in `reflection.md` names a specific next deliverable, not a vague aspiration. | `reflection.md` |
| G.3 | **2.0** | The CAD-review writeup states the goal of the iteration up front (what the student set out to do) before the checkpoints, so the AI's contribution is gradeable against intent. Half credit (1.0) if the goal is implied but not stated. | `cad_review/cad_interaction.md` |

---

## Context Management ★★ (5 pts)

| # | Pts | Criterion | Evidence path |
|---|-----|-----------|---------------|
| X.1 | **1.5** | The MCP tool returns chunks from the actual MiniClaw / ACME corpus (verified by inspecting the log or the conversation export — `doc_id` values like `ACME-ENG-001`, `ACME-MFG-002`, etc. appear in the AI's answers). | `server.log` + conversation export |
| X.2 | **1.5** | Skill text refers to the project corpus **by name** at least once (cites a doc ID, an ACME standard, or a named project like WidgetBot 2.0 / GripperBot / BigClaw). | skill body |
| X.3 | **2.0** | At least one host conversation in the evidence shows the AI using a retrieved chunk to answer a question it could not have answered from training (a MiniClaw-specific number, vendor name, or internal standard). Half credit (1.0) if the AI consulted the tool but the answer wasn't actually grounded in the chunk. | conversation export + `server.log` |

---

## Stack hygiene (silent prerequisite — not separately graded)

These don't earn points but missing them caps the relevant pillar:

- `mcp_server/server.py` and `mcp_server/requirements.txt` are committed
- `mcp_server/logs/server.log` is committed (it has to be in the repo for
  the grader to read it)
- `mcp_server/README.md` documents the chosen host with a copyable
  config snippet
- `cad_review/cad_interaction.md` exists and references the screenshots
  by relative path
- `skills/` contains the skill markdown file (not just `skills_starter/`)

If `server.log` is missing or empty, the Tools & Integration pillar is
capped at 10/20.

---

## "Be an Engineer" tiebreaker

When two students sit on the boundary between scores, the deciding
question is the one from the assignment doc:

> If you cannot tell the grader exactly what your AI did during a
> session and how you know, you have not finished the assignment.

The student who can walk the grader through their `server.log`,
identify which tool call corresponds to which screenshot, and explain
why a particular AI response was trusted or overridden is the student
who earns the higher score.
