# Progress Test, Gas Demonstrations and the Vapour Dome

> Source: Panopto session 45087616-bb49-4946-b977-b4d300d49e6b, automatic English subtitles, 59:58.

## 0. What this lecture is about

The lecture opens with the progress test rules, then uses two live demonstrations to make gas behaviour physical, and spends the second half on the step that trips most students: what happens when a liquid boils inside a piston, why the isotherm goes flat, and how to compute with a mixture of liquid and vapour.

## 1. Course arrangements: the progress test

The lecturer confirmed that this year's progress test is **the same paper as last year**. It is formally **not counted** — in the past it carried 5%, which he called a rounding error at the end of a degree. He asked students **not to hunt out and solve old papers**: the test exists to tell you early whether your study method is working, and he is happy to hand back annotated scripts with full solutions in January.

## 2. Exam administration you must know

It is a **pen-and-paper test in this room**, run like a real exam. Bring a **simple scientific calculator** — no graphing capability, no data book (data are supplied). Do not use pencil or correction fluid; cross out with one line and write beside it. Do not open or flip the paper before the invigilator says so. A large clock is projected. Graduate teaching assistants with engineering degrees mark the scripts and write where things started to go wrong.

## 3. Demonstration 1: expanding gas cools, compressing gas heats

A compressed-gas cylinder discharged into the room feels cold on the valve; a bicycle pump gets warm when you compress quickly. Both are the same physics seen from two sides: $T$ falls when a gas expands and does work quickly enough that heat cannot flow in, and rises when work is done on it quickly enough that heat cannot flow out.

The diesel demonstration pushes it further: compress air hard enough and the temperature rise ignites fuel without a spark. That is why a diesel engine has no spark plug.

## 4. Demo 2: boiling in a piston, and the shape it draws

Start with **liquid** at state 1 $(p_1,v_1,T_1)$ in a piston-cylinder. Add heat at constant pressure. The liquid expands slightly, then begins to boil: now **two phases** coexist, liquid and vapour, and the temperature **stops rising** while the mixture absorbs latent heat. Continue until the last droplet becomes vapour, at state 2.

## 5. Why pressure and temperature are not independent inside the dome

Inside the dome, fixing $T$ fixes $p$ (it is the saturation pressure), so the two are not independent. You need a third property to pin down the state, and the convenient one is **quality $x$**. That is the whole reason the dome matters: it changes how many independent properties you must specify.

## 6. Quality and the mixture rule

$$x=\frac{m_g}{m_f+m_g},\qquad 0\le x\le1$$

Every specific property of the mixture is a straight-line interpolation between the saturated liquid value $f$ and the saturated vapour value $g$:

$$v=v_f+x\,v_{fg},\qquad v_{fg}=v_g-v_f$$

$$u=u_f+x\,u_{fg},\qquad h=h_f+x\,h_{fg},\qquad s=s_f+x\,s_{fg}$$

### Example 1. Heating a gas at constant pressure

$$W=p\Delta V=4.0\times10^5\times4.49\times10^{-5}=18.0\ \mathrm{J}$$

$$Q=\frac{1.4}{0.4}\times18.0=3.5\times18.0=62.9\ \mathrm{J}$$

$$W=18.0\ \mathrm{J},\qquad Q=62.9\ \mathrm{J}$$

### Example 2. Wet steam with quality

$$v_{fg}=0.4625-0.0010836=0.4614\ \mathrm{m^3/kg}$$

$$v_2=v_f+0.9\,v_{fg}=0.0010836+0.4153=0.6069\ \mathrm{m^3/kg}$$

$$v_2=0.6069\ \mathrm{m^3/kg}\quad\text{and the state is outside the dome}$$

## 7. Pitfalls, memory hooks and self-check

|---|---|---|
| Treating $p$ and $T$ as independent inside the dome | Over-specified or inconsistent state | Use $T$ (or $p$) plus $x$ |
| Using quality outside the dome | Nonsense volume | Compare with $v_g$ first |
| Confusing $Q$ and $W$ | $Q=18$ J instead of $62.9$ J | At constant $p$, $Q/W=c_p/R$ |
| Forgetting the liquid term | $v\approx0.415$ instead of $0.607$ | Add $v_f$ |

### Self-check

1. At $4$ bar, $v_f=0.001084$, $v_g=0.4625$. Find $v$ for $x=0.5$. Answer: $0.2318\ \mathrm{m^3/kg}$.
2. Why does the isotherm stay flat while boiling? Answer: the heat goes into latent heat at constant $T$ and $p$.
3. A gas expands at constant pressure by $18.0$ J of work; what is the heat with $\gamma=1.4$? Answer: $62.9$ J.

## 8. Open items

- Example 2 stops at $v_2$; the class did not finish $Q_{12}$ in the recording, so no value is claimed here.
- The exact progress-test date was not stated in this lecture (Canvas and other modules give 9 December for the Computing paper).
