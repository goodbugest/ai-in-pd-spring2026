# MP3 Part A — Grading Rubric

**Notebook:** `MP3_PartA_Tools_Skills_Conductor.ipynb`
**Total:** 50 points
**Due:** Monday, May 11, 2026 at 11:59 PM

This rubric matches the reduced-scope assignment in
`MP3_The_Engineering_Stack.docx`. The grading philosophy is **substance
over format**: a transcript that shows the AI thinking with your tools
beats a polished writeup with no evidence.

### How partial credit works

Each section's score is the **sum** of its component criteria. Every
criterion is independently checkable — the grader awards the listed
points per item, and the section total is whatever they add up to. A
score of 7/11 in a section means "earned 4 of the listed items." Item
points may be fractional (0.5 increments) when the criterion has
clearly partial states (e.g., "transcript shows the AI called the tool
but did not use the result").

> **Soft cap:** if no `[TOOL CALL]` line appears anywhere in committed
> cell output for a section that requires tool use, the section is
> capped at 50% regardless of supporting work.

---

## Section 1 — Function Calling (7 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 1.1 | **1.0** | `convert_units` function is defined and works correctly for ≥ 2 unit pairs (verified by reading the function or by transcript output). |
| 1.2 | **1.0** | Tool schema (`convert_units_tool`) is well-formed (valid JSON schema, `name` / `description` / `parameters` / `required` all present) and printed via `pretty_print_tool_schema()`. The `description` field is specific to engineering unit conversion, not generic ("converts things"). |
| 1.3 | **1.5** | Query A transcript: shows `[TOOL CALL] convert_units` with sensible args; AI's final response uses the converted value. Half credit (0.75) if the tool was called but the AI ignored the result. |
| 1.4 | **1.5** | Query B transcript: shows **no** `[TOOL CALL]` line — AI answers from training. Half credit (0.75) if the tool was called but the answer is still substantively correct (the AI made a defensible choice). |
| 1.5 | **1.0** | Summary table is printed in cell output, comparing `tool_calls_made` against expected behavior for both queries. |
| 1.6 | **1.0** | Observation paragraph (2–3 sentences) references at least one specific moment from a transcript. Half credit (0.5) if generic ("the AI used the tool when needed"). |

---

## Section 2 — Anatomy of a Skill (8 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 2.1 | **1.0** | `skills/unit_check_skill.md` exists at the correct path (or `MP3/Part A/skills/...`) and is printed in cell output via `Path.read_text()`. |
| 2.2 | **0.5** | YAML front matter present with `name` and `description` fields. |
| 2.3 | **0.5** | "When to use this skill" section names the trigger conditions concretely. |
| 2.4 | **1.0** | "Steps" section: 3–5 numbered workflow steps that describe an actual procedure, not platitudes. |
| 2.5 | **1.0** | "What to flag" section names ≥ 2 specific patterns (e.g., "kg used as a force", "MPa where psi was expected"). Half credit (0.5) for one pattern or vague flags. |
| 2.6 | **1.0** | "What NOT to do" includes ≥ 1 substantive anti-pattern. Half credit (0.5) for a trivial anti-pattern ("don't make mistakes"). |
| 2.7 | **2.0** | Test transcript shows the skill loaded as `system=` and the AI **catching the unit error** in the test message ("12 inches" diameter for 50 N·m torque). Half credit (1.0) if the AI flags the math but misses the unit issue specifically. |
| 2.8 | **1.0** | Observation paragraph (2–3 sentences) contrasts skill vs. prompt-every-time with a specific reason, not a restated definition. |

---

## Section 3 — Wrap Your RAG as a Tool (11 pts) *centerpiece*

| # | Pts | Criterion |
|---|-----|-----------|
| 3.1 | **1.5** | Tool schema for `query_ridgeline_rag` printed via `pretty_print_tool_schema()`. The `description` field is sharp and specific (mentions Ridgeline / project history / billing rates / standards explicitly). Half credit (0.75) if the schema is valid but the description is generic. |
| 3.2 | **2.0** | **Q1 transcript** (Millbrook bridge) shows `[TOOL CALL] query_ridgeline_rag` with a sensible question argument; AI's final answer cites the retrieved chunk content. Half credit (1.0) if tool was called but the AI hallucinated the rating-factor value instead of using the chunk. |
| 3.3 | **1.5** | **Q2 transcript** (cast vs. ductile iron) shows **no** `[TOOL CALL]` line — AI answers from training. Half credit (0.75) if the tool was called but the AI ignored the irrelevant chunks and answered correctly anyway. |
| 3.4 | **2.0** | **Q3 transcript** (FEA mesh + industry) shows the tool being called and the AI synthesizing across retrieved content + training knowledge in a single response. Half credit (1.0) if only one of the two halves is addressed. |
| 3.5 | **2.0** | **Q1-vague transcript** with the deliberately vague tool description, run on the same query as Q1. Half credit (1.0) if the run exists but the comparison is not visible in cell output. |
| 3.6 | **1.0** | Summary table compares `tool_called` vs. expected behavior for all four runs (Q1 good, Q1 vague, Q2, Q3). Half credit (0.5) if the table is present but missing the vague-description row. |
| 3.7 | **1.0** | Observation (3 sentences) explicitly names the description-quality contrast and what it implies for writing tools in engineering settings. |

---

## Section 4 — Vision in the Loop (6 pts)

Graded from notebook markdown + committed screenshots, not from
`run_with_logging()` transcripts.

| # | Pts | Criterion |
|---|-----|-----------|
| 4.1 | **0.5** | Host name (Copilot Chat, Claude.ai, Claude Desktop, Cursor, ChatGPT) is documented somewhere in the section. |
| 4.2 | **2.0** | **Image exchange**: prompt copied as markdown, screenshot committed under `section4_screenshots/` and referenced from the notebook, response text copied back as markdown. Award `1.0 + 0.5 + 0.5` for those three pieces individually. |
| 4.3 | **2.0** | **Text-only baseline exchange**: same three pieces (prompt, screenshot, response). Award `1.0 + 0.5 + 0.5`. |
| 4.4 | **0.5** | Ground-truth issue list has ≥ 3 items the student identified themselves (not just the AI's list). |
| 4.5 | **0.5** | Comparison table is filled in with caught/missed counts for both exchanges. |
| 4.6 | **0.5** | Observation (3 sentences) identifies a specific vision-review limitation. |

---

## Section 5 — Composition Capstone (11 pts)

| # | Pts | Criterion |
|---|-----|-----------|
| 5.1 | **2.0** | `skills/engineering_question_with_context.md` exists and is printed in cell output. The skill names both tools (RAG and converter) and gives an explicit "when to call which" rule. Half credit (1.0) if the skill is present but doesn't mention either tool by name. |
| 5.2 | **3.0** | **WITH-skill transcript**: composite query is run with the skill loaded as system prompt and both tools available. The transcript shows the RAG tool being called **and** the converter being called. Award `1.5` per tool actually invoked. |
| 5.3 | **2.0** | The WITH-skill run's final response **synthesizes** retrieved context with the unit-converted value into one engineering answer. Half credit (1.0) if retrieved chunks are pasted without integration. |
| 5.4 | **2.0** | **WITHOUT-skill transcript** of the same query, same tools, no system prompt. Used as a controlled comparison. Half credit (1.0) if the run exists but the query was modified between runs. |
| 5.5 | **1.0** | Summary table compares `rag_called` and `converter_called` across the two runs. |
| 5.6 | **1.0** | Observation (3 sentences) names both what the skill added and one limit of what skills can do. Half credit (0.5) for naming only one. |

---

## Section 6 — Reflections (7 pts)

Two reflections, student picks the two prompts most relevant to their
work. Each reflection is independently scored on three axes.

| # | Pts | Criterion |
|---|-----|-----------|
| 6.1 | **3.5** | **First reflection**: 3–4 sentences (1.0). References at least one concrete moment from this notebook — a transcript, a tool call, an observed AI limitation (1.5). Takes a position rather than restating the prompt (1.0). |
| 6.2 | **3.5** | **Second reflection**: same three axes, scored independently. |

---

## Notebook hygiene (silent prerequisite — not separately graded)

These don't earn points but **missing them caps the section above**:

- All cells in Sections 1, 2, 3, 5 have run end-to-end without errors
- The `transcripts/` directory contains the JSON files written by
  `run_with_logging()` (these are committed automatically)
- The notebook itself is committed and pushed — the grader reads what's
  in GitHub, not what's in the student's Codespace

If the grader cannot see `[TOOL CALL]` lines in committed cell output
for a section that requires them, the section is capped at 50%
regardless of supporting work.
