---
name: miniclaw_dfm_check
description: >
  Reviews a MiniClaw component or assembly for design-for-manufacturing
  (DFM) issues specific to ACME's Prusa MK4S print shop. Trigger whenever
  the user asks whether a design is printable, whether tolerances are
  achievable, or how to prepare a part for the ACME fab run.
---

<!-- ============================================================
  THIS IS A STARTER TEMPLATE — copy it to MP3/Part B/skills/,
  rename the file and the YAML name field, and rewrite every
  section for your chosen skill topic. The topic here (DFM check)
  is an example. Do NOT submit this file unmodified.
============================================================ -->

# MiniClaw DFM Check Skill

## When to use this skill

Use this skill when the user is asking about whether a MiniClaw
component is manufacturable on ACME's Prusa MK4S print shop. Specific
triggers:

- "Can we print this?" / "Will this work on our printers?"
- Any question about minimum wall thickness, feature size, or
  tolerance on a MiniClaw part
- Any question about press-fit or snap-fit clearances
- Before committing a part design to the CAD release folder
- When reviewing a student's gear or jaw-arm design for fab readiness

Do NOT use this skill for questions about gear strength (use the gear
review skill), supplier lead times (look up the vendor doc directly),
or design aesthetics.

## Workflow

1. **Identify the part type.** Is this a gear, jaw arm, housing, pin,
   or other printed part? The constraints differ.

2. **Check minimum wall thickness.** Per `ACME-MFG-001`, the print shop
   minimum is 1.2 mm for structural walls, 0.8 mm for cosmetic features.
   Flag anything thinner.

3. **Check pin and bore diameters.** Minimum pin diameter for structural
   use is 3.0 mm. Bores that receive pins need +0.15 mm clearance over
   nominal for FDM tolerance. Bores designed for press fits need
   -0.05 mm (slightly undersized — they loosen during print).

4. **Check print orientation.** Gears should print flat (teeth
   in-plane) so the interlayer adhesion argument holds — per
   `ACME-MFG-002`. Jaw arms should print vertically to put layer lines
   parallel to the bending load.

5. **Check support requirements.** The print shop avoids supports
   (slows the 500-unit run). Flag any overhang greater than 45 degrees.
   Suggest a chamfer or design split if needed.

6. **Verify against tolerance analysis.** Consult `ACME-ENG-003` for
   the MiniClaw printed-assembly tolerance stack. Flag any interface
   where the stack-up could cause interference or excessive slop.

7. **Summarize findings.** List: PASS / FLAG / FAIL for each check.
   Explain what needs to change on any flagged item.

## What to flag

- **Wall thickness below 1.2 mm structural / 0.8 mm cosmetic** —
  cite `ACME-MFG-001`
- **Bores without FDM clearance allowance** — cite `ACME-ENG-003`
- **Overhang angles above 45 degrees** — note support requirement
  and fab impact at 500-unit scale
- **Gears designed to print on-edge** — interlayer failure mode per
  `ACME-MFG-002` WidgetBot 2.0 test report

## What NOT to do

- **Do not approve a design without checking the tolerance stack.**
  Individual features can look fine in isolation but cause assembly
  issues at the interface. Always run through `ACME-ENG-003`.
- **Do not recommend support structures as a fix** without flagging
  the production impact — 500 units times 2 min support removal is
  not trivial.
- **Do not guess at filament properties.** Use the `ACME-MFG-002`
  FilaTech PolyPro PLA Technical Summary for specific values. The
  bulk tensile strength is not the same as the interlayer tensile
  strength (which is the number that matters for printed gears).
