# MECH40005 Stress Analysis — Notes Index

> **Course**: MECH40005 Stress Analysis (2026-27)
> **Coverage so far**:
> - **2026-11-17 recording**: three-dimensional strains; stress and components of pressure vessels; 3D stress-strain relations and thermal effects; strains in cylindrical and spherical shells; volumetric strain; load sharing in composite rod-tube systems; the statically indeterminate tie-rod cylinder
> - Earlier notes: 3D generalised Hooke's law, Lecture 6 stress analysis (see the table below)
> **Chapter map**: The slides run from strain to stress to the 3D relations to pressure vessels; the handout contents page puts bending in Chapter 5, which is not the slide order. Chapter numbers in the notes in this folder always follow the slides, and the handout is used only to check wording and section names.
> **Structure**: One md file per lecture, English and Chinese in paired paragraphs; each worked example follows the eight-step pattern plus a poster, and posters live in `figures/`.

---

## Notes

| Chapter | Date | Topic | Note |
|---|---|---|---|
| **Strain and stress (recording)** | 2026-11-17 | Recording notes: $\varepsilon_z=\frac{\Delta L}{L}$, $\varepsilon_\theta=\frac{\Delta R}{R}$; thin wall $\sigma_\theta=\frac{PR}{t}$, $\sigma_z=\frac{PR}{2t}$; 3D Hooke's law with $\alpha\Delta T$; $\varepsilon_v=2\varepsilon_\theta+\varepsilon_z$; indeterminacy handled with equilibrium plus compatibility; four tie-rod cylinder $\sigma_{rod}=29.6$, $\sigma_z=89.6$, $\sigma_\theta=200$ MPa. Two eight-step examples plus 2 posters | [MECH40005_Ch5-6_2026-11-17_3D_Stress_Pressure_Vessels_Indeterminate.md](./MECH40005_Ch5-6_2026-11-17_3D_Stress_Pressure_Vessels_Indeterminate.md) |
| — | — | 3D generalised Hooke's law | [MECH40005_3D_Hookes_Law.md](./MECH40005_3D_Hookes_Law.md) |
| — | — | Lecture 6 stress analysis | [MECH40005_Lecture6_Stress_Analysis_v2.md](./MECH40005_Lecture6_Stress_Analysis_v2.md) |

---

## Key formulas

**Strain**

$$\varepsilon_z=\frac{\Delta L}{L},\qquad \varepsilon_\theta=\frac{\Delta R}{R}$$

**Thin-wall membrane stresses**

$$\sigma_\theta=\frac{PR_i}{t},\qquad \sigma_z=\frac{PR_i}{2t}$$

**3D stress-strain law**

$$\varepsilon_x=\frac{\sigma_x-\nu(\sigma_y+\sigma_z)}{E}+\alpha\Delta T$$

**Volumetric strain**

$$\frac{\Delta V}{V}\approx2\varepsilon_\theta+\varepsilon_z\quad\text{(cylinder)},\qquad \frac{\Delta V}{V}\approx3\varepsilon_\theta\quad\text{(sphere)}$$

---

## Open items

- At 12:20 the slide writes $\sigma_r=P$, while the worked example frame at 53:00 writes $\sigma_r=-P$; these notes take tension as positive and treat the first expression as a magnitude.
- At 24:10 the middle lines of the cuboid slide appear to repeat the $x$ subscript for the $y$ and $z$ terms.
- The frame at 53:00 gives $29.6$ / $89.6$ MPa, while the extracted handout text gives about $33$ / $93$ MPa; the handout used a different rounding of the wall area.
