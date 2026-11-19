# Engineering Lecture Notes — English Edition

Study notes for first-year mechanical engineering courses, rewritten in English so they can be shared with anyone. Every note here is a working document: derivations written out step by step, worked examples with the arithmetic shown, the mistakes that are easy to make, and figures drawn for each idea.

These are personal study notes, not official course material. They were written while following the recorded lectures and handouts; where a note disagrees with the handout, the handout wins.

## What is inside

| Course | Folder | Contents |
|---|---|---|
| MECH40003 Thermodynamics 1 | `MECH40003 Thermodynamics 1/` | Enthalpy, specific heats and the perfect-gas approximation (Ch 4) |
| MECH40004 Mechatronics 1 | `MECH40004 Mechatronics 1/` | Electromagnets and brushed DC machines (Ch 3–4) |
| MECH40005 Stress Analysis | `MECH40005 Stress Analysis/` | 3D stress and strain, pressure vessels, indeterminate systems, 3D Hooke's law, plus worked tutorial sets |
| MECH40001 Professional Engineering Skills 1 | `MECH40001 Professional Engineering Skills 1/` | Using AI tools honestly: LLM limits, purpose framing, verification and prompt engineering |
| MECH40002 Fluid Mechanics 1 | `MECH40002 Fluid Mechanics 1/` | Shear deformation and strain rate, flow classification, hydrostatics, manometers (Ch 1) |
| MECH40006 Materials 1 | `material/` | Lectures 4–7: material selection, atomic bonding, bond energy and crystal structures |
| MECH40008 Mathematics and Computing 1 | `MECH40008 Mathematics and Computing 1/` | Taylor remainders, Leibniz rule, ratio test, binomial series, partial differentiation, total derivatives, two-variable Taylor series, plus a master formula sheet |
| MECH40008 Computing 1 | `MECH40008 Computing 1/` | NumPy arrays versus lists, vectorisation, Matplotlib (Ch 6) |
| MECH40009 Mechanics | `MECH40009 Mechanics/` | Moments about an axis, work, friction (Ch 2–3) |
| ME1 Thermodynamics | `ME1 Thermodynamics/` | Tutorial set: system versus control volume, quasi-equilibrium, properties and cycles |
| ME1 PEN | `ME1 PEN/` | Fairground lab briefing and report checklist |

Each course folder has its own `README.md` index. Every folder keeps its figures in a local `figures/` directory, and notes link to them with relative paths, so the tree works offline after a clone.

## How to read these notes

- Open any `.md` file on GitHub: mathematics renders as typeset formulas. In a local editor, use one that supports Markdown math (VS Code with a Markdown-math extension, Obsidian, Typora, or Pandoc).
- Display formulas use `$$ ... $$` and inline formulas use `$ ... $`. Formulas are never hidden in code blocks.
- Figures are PNG files under each course's `figures/` folder. Example posters follow a six-step flow with the key points collected at the bottom.

## Conventions used throughout

1. One lecture, one note file. Nothing is split into versions; visual material lives inside the same file as the text.
2. Worked examples follow the same eight-part shape: what is asked, why this route, step-by-step with the formula and what it yields, where each constant comes from, a sanity check, the final answer in its own block, the likely mistake, and the figure.
3. Every new symbol is defined where it first appears; nothing is left as "obviously".
4. Figures are drawn with Matplotlib and rendered to PNG; the maths inside a poster is typeset, not typed as ASCII.

## Repository layout

```text
.
├── MECH40003 Thermodynamics 1/
├── MECH40004 Mechatronics 1/
├── MECH40005 Stress Analysis/
├── MECH40008 Computing 1/
├── MECH40008 Mathematics and Computing 1/
├── MECH40009 Mechanics/
├── ME1 Thermodynamics/
├── ME1 PEN/
├── material/
├── _tools/          helper scripts: catalogue, style and link checks, poster rendering
└── README.md
```

## Checks you can run

```text
python _tools/check_math_style.py     # formulas must be Markdown math
python _tools/check_example_depth.py  # worked examples keep the eight-part shape
python _tools/check_note_links.py     # every image and local link resolves
python _tools/make_catalogue.py       # rebuild the catalogue index
```

All four take no arguments and resolve paths from their own location, so the repository can be cloned anywhere.

## What is deliberately not here

- Lecture handouts and PDFs from the course: they are the department's material, not mine to redistribute.
- Recorded lecture video: large and not mine either.
- Anything personal: no machine paths, no accounts, no contact details.

## Using this

Read it, learn from it, point out mistakes. If you reuse a figure or a chunk of text, link back to this repository. No warranty: I am a student, and errors survive in here in spite of the checks above.
