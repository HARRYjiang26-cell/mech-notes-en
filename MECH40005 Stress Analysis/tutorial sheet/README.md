# Tutorial Sheet 4 — Stress and strain: key ideas, formulas, answers and full working

> **Course**: MECH40005 Stress Analysis 1 (2026–27)
> **Source**: Lambda Feedback → *Tutorial sheet 4: Stress and strain* (Set 4: 4.1 has a single part; 4.2–4.5 each have parts (a) and (b))
> **Contents**: for each problem → the original question, key points, answer at a glance, key ideas, formulas, full working part by part, common mistakes, and the matching lecture material
> **Convention**: every answer here is derived independently and checked numerically; where the platform demands a particular unit or number of significant figures, the "platform entry" line takes precedence.

---

## 1. All answers

| Problem | Part | Quantity | Answer |
|---|---|---|---|
| 4.1 | — | Bolt tension | **$F\approx6.94\ \text{kN}$** ($\sigma=138\ \text{MPa}$) |
| 4.2 | (a) | Total volume change of the cylinder | **$0.101\ \text{m}^3$** (≈101 L) |
| 4.2 | (b) | Volume change of the spherical tank | **$0.100\ \text{m}^3$** (≈100 L) |
| 4.3 | (a) | $\sigma_y$ needed to restore the $y$ dimension | **$-21.54\ \text{MPa}$** (compression) |
| 4.3 | (b) | Volume change of the block | **$+2.90\times10^{-7}\ \text{m}^3$** ($+290\ \text{mm}^3$) |
| 4.4 | (a) | Four-face constraint: $\Delta L$, $E_{\text{app}}$, lateral pressure | **$-0.157\ \text{mm}$, $138\ \text{GPa}$, $48\ \text{MPa}$** |
| 4.4 | (b) | Two-face constraint: $\Delta L$, $E_{\text{app}}$, lateral pressure | **$-0.176\ \text{mm}$, $122.7\ \text{GPa}$, $36\ \text{MPa}$** |
| 4.5 | (a) | Hemisphere wall thickness $t'$ | **$0.4t$** ($=2t/5$) |
| 4.5 | (b) | Volume change of the whole vessel | **$\dfrac{32}{3}\pi\dfrac{PR^{4}}{tE}$** |

---

## 2. Index

| Problem | Topic | Key formulas | File |
|---|---|---|---|
| 4.1 | Bolt tightening (single part) | $k=\dfrac{EA}{L}$, $\delta=\dfrac{p}{6}$, $F=k\delta$ | [Q4.1](Q4.1-bolt-tightening.md) |
| 4.2 | Thin cylinder / spherical tank: internal pressure + heating | $\sigma_\theta=\dfrac{pR}{t}$, $\sigma_z=\dfrac{pR}{2t}$, $\dfrac{\Delta V}{V}=2\varepsilon_\theta+\varepsilon_z+3\alpha\Delta T$ | [Q4.2](Q4.2-cylinder-pressure-thermal-volume.md) |
| 4.3 | Constrained block: restore $y$, then find $\Delta V$ | $\sigma_y=\nu(\sigma_x+\sigma_z)-E\alpha\Delta T$; $\Delta V/V=\varepsilon_x+\varepsilon_y+\varepsilon_z$ | [Q4.3](Q4.3-constrained-3d-hooke-thermal.md) |
| 4.4 | Cast-iron block: four-face / two-face lateral constraint | $E_{\text{app}}=\dfrac{E(1-\nu)}{1-\nu-2\nu^2}$ or $\dfrac{E}{1-\nu^2}$ | [Q4.4](Q4.4-cast-iron-apparent-modulus.md) |
| 4.5 | Cylinder + hemispheres: equal hoop strain, whole-vessel $\Delta V$ | $t'=\dfrac{t(1-\nu)}{2-\nu}$, $\Delta V=\dfrac{32}{3}\pi\dfrac{PR^{4}}{tE}$ | [Q4.5](Q4.5-cylinder-hemisphere-equal-hoop-strain.md) |

---

## 3. Three threads

1. **Constitutive**: 3D Hooke's law + thermal strain
   $$\varepsilon_x=\frac{\sigma_x-\nu(\sigma_y+\sigma_z)}{E}+\alpha\Delta T,\quad \text{(cycled for y, z)}$$
2. **Equilibrium / membrane**: the stress in a thin-walled vessel depends only on pressure and geometry
   $$\sigma_\theta=\frac{pR}{t},\qquad \sigma_z=\frac{pR}{2t}\ (\text{closed cylinder}),\qquad \sigma=\frac{pR}{2t}\ (\text{spherical shell})$$
3. **Geometry / compatibility**: the extra condition supplied by a constraint or a junction
   - Bolt: the clamped parts are rigid ⇒ the whole advance of the nut becomes bolt extension (4.1)
   - Block: $\varepsilon_y=0$ (4.3), $\varepsilon_x=\varepsilon_z=0$ or $\varepsilon_x=0$ (4.4)
   - Junction: the hoop strain of the cylinder equals that of the sphere (4.5)

**Working order**: first see what is constrained, then choose the constitutive law, and finally substitute the geometric condition.

---

## 4. Notation

| Symbol | Meaning | Usual unit |
|---|---|---|
| $\sigma$ | Normal stress (tension positive) | Pa / MPa |
| $\varepsilon$ | Normal strain | – |
| $E$ | Young's modulus | GPa |
| $\nu$ | Poisson's ratio | – |
| $\alpha$ | Coefficient of linear expansion | K$^{-1}$ |
| $p$ / $P$ | Internal pressure | MPa |
| $R$, $R_m$ | Radius / mean radius | m, mm |
| $t$, $t'$ | Cylinder wall thickness / hemisphere wall thickness | mm |
| $L$ | Length, clamped length | m |
| $A$ | Cross-sectional area | mm$^2$, m$^2$ |
| $F$ | Axial force | N, kN |
| $\Delta T$ | Temperature rise | K or °C |
| $V$ | Volume | m$^3$ |

**Unit conversions**: $1\ \text{GPa}=10^{3}\ \text{MPa}=10^{9}\ \text{Pa}$; $1\ \text{MPa}=1\ \text{N/mm}^2$; $1\ \text{mm}^3=10^{-9}\ \text{m}^3$.

---

## 5. Platform notes

- 4.2, 4.3(b): give the volume answer with units ($\text{m}^3$ or L / mm³).
- 4.3(a): the negative sign means compressive stress; if the platform wants magnitude only, enter $21.5\ \text{MPa}$.
- 4.4: length in mm (or in m, watch the $10^{-4}$); modulus in GPa; lateral pressure in MPa.
- 4.5(b): give the power form in $R^4$ as the question hints (the platform states it uses the R**4 notation).

---

## 6. Cross-references

- [MECH40005 Lecture 6 — constrained blocks, apparent modulus, thin-walled pressure vessels](../MECH40005_Lecture6_Stress_Analysis_v2.md)
  - §2 Bolted hemispherical vessel (same idea as 4.1), §3 Constrained blocks and apparent modulus, §5 Shell strain, §6 3D Hooke applied to shells, §8 Volumetric strain of a cylindrical shell, §9 Quick-reference formulas
- [MECH40005 — 3D Hooke's Law](../MECH40005_3D_Hookes_Law.md)
  - §3 The three strain equations, §5 Thermal strain on heating, §6 Hydrostatic stress and volumetric strain, §9 Quick-reference formulas
- Course notes: Ch. 3.2 (thin-walled vessels), Ch. 4.4–4.7 (3D Hooke, thermal strain, volumetric strain)

---

*Answers derived under the assumptions stated in the questions (thin-walled, linear elastic, small deformation; 4.2(b) uses the same loading as the cylinder; 4.5(b) uses $t'=0.4t$ from part (a) and neglects bending at the junction).*
