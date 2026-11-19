# MECH40008 Mathematics and Computing 1 - Notes Index

> **Course.** MECH40008 Mathematics and Computing 1 (2026-27)
> **Coverage.** Lecture on 2026-11-11 (Taylor remainders, Leibniz's rule, ratio test). Lecture on 2026-11-12 (applications of Leibniz's rule, bouncing-ball series, binomial series, introduction to partial differentiation). Notes compiled on 2026-11-13 for **Ch 9 §9.1-9.4** (partial derivatives, higher and mixed partials, small changes and the total differential, total derivatives and the chain rule). **Recording on 2026-11-17 for Ch 9 §9.4-9.5** (three cases for total derivatives, implicit differentiation, change of variables, polar coordinates, why partial derivatives cannot be inverted one at a time, and two proofs). Programming class on 2026-11-13, **Lecture 6 NumPy + Matplotlib** (Ch 6 §6.1-6.3, in the separate folder `MECH40008 Computing 1/`).
> **Chapter map.** Ch 7 covers single-variable differentiation (derivative definition, Eq 7.1). Ch 8 covers series (Taylor, geometric and binomial series and the ratio test). Ch 9 covers partial differentiation (Eq 9.1). The chapter numbers come from the equation numbers printed in the lecture materials.
> **Structure.** Each lecture has one Markdown file with derivations, worked examples, common pitfalls, self-checks, a formula card and a glossary. Illustrations are in `figures/`. Formulas use Markdown maths, with `$...$` for inline maths and `$$...$$` for display maths.

---

## Notes

| Chapter | Date | Topic | Notes |
|---|---|---|---|
| **Ch 6 (6.1-6.3)** | 2026-11-13 | Programming class (Lecture 6) covering NumPy arrays and lists, initialisation, slicing, masks and reductions, 2D arrays and matrix operations with `*` and `@`, vectorisation, and six types of Matplotlib plots plus log axes, meshgrid and contourf. **Now in `../MECH40008 Computing 1/`.** | [MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib.md](../MECH40008%20Computing%201/MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib.md) |
| **Ch 9 (9.4-9.5)** | 2026-11-17 | Notes from the recording (bilingual source). Covers the three cases for total derivatives (Case 2 $y=y(x)$ / Case 3 $z=C$), inverse tangent and implicit differentiation, change of variables and polar coordinates, why partial derivatives cannot be inverted one at a time, and two proofs. Includes eight worked examples with eight parts each and accompanying posters. | [MECH40008_Ch9-9_2026-11-17_Total_Derivative_Change_of_Variables.md](./MECH40008_Ch9-9_2026-11-17_Total_Derivative_Change_of_Variables.md) |
| **Ch 9 (9.1-9.4)** | 2026-11-13 | Partial differentiation notes covering definitions and geometry, higher and mixed partials, small changes and signed relative error, and total derivatives (9.4.1 / 9.4.2 / 9.4.3). | [MECH40008_Ch9-9_2026-11-13_Partial_Differentiation.md](./MECH40008_Ch9-9_2026-11-13_Partial_Differentiation.md) |
| **Ch 7-9** | 2026-11-12 | Lecture notes spanning three chapters. Covers applications of Leibniz's rule, Maclaurin series, bouncing-ball series, binomial series and an introduction to partial differentiation. For detailed Chapter 9 notes, see the row above. | [MECH40008_Ch7-9_2026-11-12_Leibniz_Taylor_BouncingBall_Binomial_Partial.md](./MECH40008_Ch7-9_2026-11-12_Leibniz_Taylor_BouncingBall_Binomial_Partial.md) |
| **Ch 7-8** | 2026-11-11 | Taylor remainders, Leibniz's rule and the ratio test. | [MECH40008_Ch7-8_2026-11-11_Remainder_Leibniz_RatioTest_v2_visual.md](./MECH40008_Ch7-8_2026-11-11_Remainder_Leibniz_RatioTest_v2_visual.md) |
| - | - | **Combined formula sheet for exam revision** | [CHEATSHEET.md](./CHEATSHEET.md) |

---

## Key formulas

**Taylor remainder**

$$R_n=\frac{h^{n+1}}{(n+1)!}\,f^{(n+1)}(a+\theta h),\qquad 0\le\theta\le 1$$

**Leibniz's rule**

$$D^{n}(uv)=\sum_{r=0}^{n}\binom{n}{r}D^{r}u\,D^{n-r}v$$

**Recurrence and series for $\arcsin$**

$$y^{(n+2)}(0)=n^{2}y^{(n)}(0),\qquad \arcsin x=x+\frac{x^{3}}{6}+\frac{3x^{5}}{40}+\frac{5x^{7}}{112}+\cdots$$

**Ratio test**

$$L=\lim_{r\to\infty}\left|\frac{a_{r+1}}{a_{r}}\right|,\qquad L<1\ \text{absolutely convergent},\quad L>1\ \text{divergent},\quad L=1\ \text{inconclusive}$$

A result of $L<1$ means absolute convergence, $L>1$ means divergence, and $L=1$ is inconclusive. In the last case, use another test.

---

## Top three pitfalls

1. **Remainder.** Even when the bound is below the tolerance, add and subtract it and check whether either result rounds differently. Always round the bound upwards.
2. **Leibniz's rule.** A polynomial factor makes the sum collapse. When both factors are non-polynomial, take care to include every term.
3. **Ratio test.** When $L=1$, write "inconclusive" and use a different test.

---

## To do

- [ ] Complete the v1/v2 notes for later lectures (11-18, 11-25 and following).
- [x] Keep one Markdown file per lecture. The v1 and v2 notes have been merged, with the visual notes included in the full version.
- [ ] Add the original handouts in the `material` format once the PDFs are available.
- [x] Combine the formula references from all lectures into one pre-exam sheet. [CHEATSHEET.md](./CHEATSHEET.md) is in place and will grow with subsequent lectures.
