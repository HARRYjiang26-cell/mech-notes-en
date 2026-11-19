# MECH40008 — Maths Master Cheat Sheet

> **Purpose**: one pass through everything in the last 10 minutes before the exam. For each lecture, one section, formulas plus a one-line note on how to use them.
> **Updates**: appended lecture by lecture as the course runs; currently covers 2026-11-11 (Ch 7–8), 2026-11-12 (Ch 7–9) and 2026-11-13 (Ch 6 programming class: NumPy + Matplotlib).
> **Full versions**: see the individual lecture notes ([11-11 visual version](./MECH40008_Ch7-8_2026-11-11_Remainder_Leibniz_RatioTest_v2_visual.md) / [11-12 full version](./MECH40008_Ch7-9_2026-11-12_Leibniz_Taylor_BouncingBall_Binomial_Partial.md) / [11-13 programming class Ch 6](../MECH40008%20Computing%201/MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib.md)).

---

## Lecture 11-11 (Ch 7–8): remainder · Leibniz · ratio test

### Remainder (error budget)

$$R_n=\frac{h^{n+1}}{(n+1)!}\,f^{(n+1)}(a+\theta h),\qquad 0\le\theta\le 1.$$

- How to use it: write the next term → take the worst upper bound of the derivative → compare with the tolerance → check the rounding against the bound.

**One word of advice:** an upper bound can only be pushed upwards; and you may only claim "accurate to 4 digits" after the rounding check.

### Leibniz rule

$$D^{n}(uv)=\sum_{r=0}^{n}\binom{n}{r}D^{r}u\,D^{n-r}v.$$

- Trick: a polynomial factor kills every row with $r>m$, leaving just $m+1$ surviving terms.

**One word of advice:** find the polynomial factor first, then list the surviving rows.

### $\arcsin x$ recurrence

$$(1-x^{2})y''-xy'=0\quad(\text{starting point}),$$

$$y^{(n+2)}(0)=n^{2}\,y^{(n)}(0)\quad(\text{put }x=0\text{ to get the recurrence}),$$

$$\arcsin x=x+\frac{x^{3}}{6}+\frac{3x^{5}}{40}+\frac{5x^{7}}{112}+\cdots$$

- The even chain is always zero (starting point $y(0)=0$).

### Ratio test

$$L=\lim_{r\to\infty}\left|\frac{a_{r+1}}{a_r}\right|$$

| $L$ | conclusion |
|---|---|
| $L<1$ | absolutely convergent |
| $L>1$ | divergent |
| $L=1$ | cannot decide (change method) |

**One word of advice:** $L=1$ is not an answer; write inconclusive.

---

## Numbers to remember from this lecture

- $\sin 46^\circ$ three-term approximation $=0.7193404$; remainder bound $|R_2|\le 8.9\times 10^{-7}$ (tolerance $5\times10^{-5}$, so 56 times smaller).
- $D^{n}(x^{2}e^{x})=(x^{2}+2nx+n(n-1))e^{x}$; for $n=4$ it gives $=(x^{2}+8x+12)e^{x}$.
- $\arcsin$ derivative chain: $y'(0)=1,\ y'''(0)=9,\ y^{(5)}(0)=225$ (the whole even chain is 0).
- Ratio for the sine series: $L=\dfrac{x^{2}}{(2r+2)(2r+3)}\to 0$ (absolutely convergent on the whole real axis).
- Harmonic series $\sum \dfrac{1}{r}$: the ratio test gives $L=1$ and fails; the series actually diverges.

---

## Lecture 11-12 (Ch 7–9): Leibniz applications · bouncing ball · binomial series · first look at partial derivatives

### Bouncing ball (geometric series)

$$D_N=h+2rh+2r^{2}h+\cdots+2r^{N}h=h(1+r^{N})+2h\sum_{n=1}^{N}r^{n},$$

$$\sum_{n\ge 0}x^{n}=\frac{1}{1-x}\quad(|x|<1,\ \text{taken as known}),$$

$$D=h+2h\cdot\frac{r}{1-r}=h\,\frac{1+r}{1-r}.$$

- Numbers: $h=1.5\ \text{m},\ r=0.7\ \Rightarrow\ D=8.5\ \text{m}$.

**One word of advice:** $r$ is the coefficient of restitution, not the number of bounces; at $r=1$ the total diverges.

### Ratio test (final verdict)

| series | $L$ | conclusion |
|---|---|---|
| $\sum r^{n}$ | $r$ | convergent for $r<1$ |
| $\sin x,\ \cos x,\ e^{x}$ | $0$ | convergent for every finite $x$ |
| $(1+x)^{n}$ | $|x|$ | convergent for $|x|<1$, radius $1$, nothing said at $|x|=1$ |

**One word of advice:** write inconclusive when $L=1$, never treat it as a verdict.

### Binomial series

$$(1+x)^{n}=1+nx+\frac{n(n-1)}{2!}x^{2}+\frac{n(n-1)(n-2)}{3!}x^{3}+\cdots$$

$$\sqrt{51}=7\left(1+\frac{2}{49}\right)^{1/2}\approx 7.1414\qquad\left(\text{requires }|2/49|<1\right)$$

**One word of advice:** first put the number into the form $(1+\varepsilon)^{n}$ (that $\varepsilon$ is the small quantity), then expand.

### Partial derivatives

- For $z=f(x,y)$: freeze $y=y_0$ and $z$ becomes a function of $x$ alone.

$$\left.\frac{\partial f}{\partial x}\right|_{(x_0,y_0)}=\lim_{\delta x\to 0}\frac{f(x_0+\delta x,\,y_0)-f(x_0,y_0)}{\delta x}=f_x\qquad(\text{Eq. }9.1)$$

$$f=x^{2}y+\sin y\ \Rightarrow\ f_x=2xy,\quad f_y=x^{2}+\cos y.$$

**One word of advice:** $f_x$ is still a function of both variables after you compute it; the freezing lasts only for that one step.

---

## Lecture 11-13 (Ch 6): NumPy and Matplotlib

### Array initialisation

$$\text{np.zeros}(n),\quad \text{np.ones}(n),\quad \text{np.zeros}((m,n)),\quad \text{np.linspace}(a,b,n),\quad \text{np.logspace}(a,b,n)$$

- $\text{linspace}(a,b,n)$ takes $n$ equally spaced points on $[a,b]$, **both ends included**, with step $\dfrac{b-a}{n-1}$.

**One word of advice:** $\text{linspace}(0,2\pi,200)$ has $199$ intervals and step $\dfrac{2\pi}{199}\approx 0.03157$, not $\dfrac{2\pi}{200}$; $\text{range}$ excludes the right end, so the two must not be confused.

### Indexing and reductions

$$x[i]\ (\text{0-based}),\quad x[-1]\ (\text{last}),\quad x[1{:}4],\quad x[{:}{:}2],\quad x[x<65],\quad \text{np.sum}(x[x<65])$$

- A Boolean comparison returns a True/False array of the same shape and **does not modify the original array**; mask indexing also returns a new array.

**One word of advice:** $x[x<65]$ is already the filtered array, so wrapping $\text{np.sum}$ around it gives the conditional sum; no loop is needed.

### Element-wise versus matrix product

$$A*B\ \text{(element-wise)},\qquad A@B\ \text{(matrix product)}$$

- With $A=\begin{pmatrix}2&1\\1&3\end{pmatrix}$ and $B=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $A*B=\begin{pmatrix}2&0\\2&3\end{pmatrix}$, while $A@B=\begin{pmatrix}4&1\\7&3\end{pmatrix}$.

**One word of advice:** $*$ on 2D arrays is not a matrix product; a matrix product must be written $@$.

### Linear algebra

$$\det A,\qquad A^{-1},\qquad A\,x=b\ \Rightarrow\ x=\text{np.linalg.solve}(A,b)$$

- Numerically, do not hand-compute $A^{-1}b$; call $\text{solve}$ directly, because the former does one extra inversion and carries more error.

### Matplotlib

$$\text{import matplotlib.pyplot as plt},\qquad \text{fig},\ \text{ax}=\text{plt.subplots}()$$

- Six plot types, each for one kind of data: $\text{plot}$ (line) · $\text{scatter}$ (points) · $\text{bar}$ (bars) · $\text{hist(bins=...)}$ (histogram) · $\text{errorbar(yerr=...)}$ (error bars) · $\text{fill\_between}$ (uncertainty band).
- Field plots: $\text{np.meshgrid}(x,y)$ builds the grid, then $\text{ax.contourf}(X,Y,Z,\text{levels}=20)$.

**One word of advice:** $\text{ax.plot}$ always joins the points with a line, so use $\text{scatter}$ for points; importing $\text{import matplotlib}$ without importing $\text{pyplot}$ is the most common source of error messages.

---

## (Further lectures are appended here)
