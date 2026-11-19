# Tools for these notes

Small scripts that keep the note tree consistent. All of them run with plain Python 3 and only touch their own output; none of them edits note text.

| File | What it does | How to run |
|---|---|---|
| `make_catalogue.py` | Scans the note tree for `.md` files and rebuilds the catalogue index at the repository root | `python _tools/make_catalogue.py` (add `--check` to inspect without writing) |
| `check_math_style.py` | Style gate for maths notes: every formula must be Markdown math ($...$ inline, $$...$$ display), never plain text or a backtick block. Prints `RESULT PASS` or a list of violations | `python _tools/check_math_style.py` |
| `check_example_depth.py` | Checks that every worked example follows the eight-part template and links its poster figure | `python _tools/check_example_depth.py` |
| `check_note_links.py` | Verifies that every image reference and local file link in the notes resolves to a real file | `python _tools/check_note_links.py` |
| `gen_example_posters.py` | Renders one poster per worked example (six-step flow plus key points) from `example_posters.json`, using `math_render.py` and headless Chrome | `python _tools/gen_example_posters.py` |
| `math_render.py` | Minimal offline LaTeX-subset to HTML renderer: real fraction bars, radicals, limits and super/subscripts, so posters contain typeset maths rather than ASCII approximations | imported by the poster scripts |
| `gen_d12_figs.py` | Builds the chapter and section figures for the Chapter 9 notes | `python _tools/gen_d12_figs.py` |
| `gen_set2_figs.py` | Builds the eight diagrams for the thermodynamics tutorial sheet, Pillow only | `python _tools/gen_set2_figs.py` |
| `example_posters.json` | Content of the example posters: title, panel text and formulas per example | edit, then rerun `gen_example_posters.py` |

## Notes on running them

- Paths inside the scripts are resolved from the location of the script file, so the tree can be cloned anywhere.
- The poster scripts need a local Chrome or Edge build for screenshots; the figure scripts need Pillow.
- The three `check_*.py` scripts exit non-zero when they find a problem, which makes them usable as a pre-commit gate.
