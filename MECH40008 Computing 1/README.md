# MECH40008 Computing 1 — Notes Index

> **Course** MECH40008 Mathematics and Computing 1 (2026–27), programming component.
> **Why this folder exists** The course has two components. **Mathematics** (Ch 7–9) covers calculus and series. **Programming** covers practical Python with NumPy and Matplotlib. The mathematics notes are in `MECH40008 Mathematics and Computing 1/`, and the programming notes are here.
> **Structure** Each lecture has one Markdown file with derivations, worked examples, common pitfalls, self-checks, a formula card and a glossary. Figures are in `figures/`. Formulas use Markdown maths (`$...$` / `$$...$$`), and code uses Python code blocks.

---

## Notes

| Lecture | Date | Topics | Notes |
|---|---|---|---|
| **Lecture 6 (§6.1–6.3)** | 2026-11-13 | NumPy arrays vs lists · contiguous memory · timing experiment · initialisation · slicing and masked reductions · 2D arrays and matrices, `*` vs `@` · vectorisation · six Matplotlib plot types, log axes, meshgrid and contourf | [MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib.md](./MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib.md) |

---

## Key formulas

**Timing experiment**

$$t_{\text{list}} = 0.0910\ \text{s},\qquad t_{\text{np}} = 0.0099\ \text{s},\qquad \text{speedup} = \frac{t_{\text{list}}}{t_{\text{np}}}\approx 9.2$$

The lecturer rounded the timing and speedup to "0.01 seconds, about 10 times". The notes retain the original precision.

**Array initialisation**

$$\text{np.linspace}(a,b,n):\quad \text{step}=\frac{b-a}{n-1}$$

Both endpoints are **included**. This is the main difference from $\text{range}$.

**Element-wise vs matrix product**

$$A*B\ \text{(element-wise)},\qquad A@B\ \text{(matrix product)}$$

**Vectorisation**

$$\text{9 rounds of Python overhead}\ \longrightarrow\ \text{1 round}$$

---

## Three common pitfalls

1. **$\text{linspace}$ includes both endpoints, while $\text{range}$ excludes the right endpoint.** $\text{linspace}(0,2\pi,200)$ has $199$ intervals. Its step is $\dfrac{2\pi}{199}$, not $\dfrac{2\pi}{200}$.
2. **$*$ on 2D arrays.** Use $*$ for element-wise multiplication and $@$ for matrix multiplication.
3. **$\text{plt.plot}$ joins the points with line segments.** Use $\text{plt.scatter}$ for a scatter plot to avoid joining observations into a zigzag.

---

## Self-check

```
rem run these from the repository root
python _tools\check_math_style.py
python _tools\check_example_depth.py
python _tools\check_note_links.py
```

All three commands should print `RESULT PASS`.

---

## Related

- Mathematics component (Ch 7–9) — [`../MECH40008 Mathematics and Computing 1/README.md`](../MECH40008%20Mathematics%20and%20Computing%201/README.md)
- Overall reference card — [`../MECH40008 Mathematics and Computing 1/CHEATSHEET.md`](../MECH40008%20Mathematics%20and%20Computing%201/CHEATSHEET.md)
- Source material — Panopto "ME Computing 1", 2026-11-13 (59:59). Quotations are taken from the lecture caption track and the slide screenshots.
