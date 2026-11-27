# Complex Roots, Euler Integrals and Complex Differentiation

> Source: Panopto session 68591702-cc38-4b9b-a095-b4b40179ebed, automatic English subtitles, 59:56.

## 0. What this lecture is about

Four things, in order: finish the roots business with a second worked example, then use Euler's formula as an integration machine, then connect the hyperbolic and trigonometric functions through imaginary angles, and finally define what a derivative of a complex function even means.

## 1. Roots and the $2\pi k$ bookkeeping

For $z^n=w$, write $w=re^{i\theta}$ and take

$$z_k=r^{1/n}\exp\!\left(i\,\frac{\theta+2\pi k}{n}\right),\qquad k=0,1,\dots,n-1$$

The modulus $r^{1/n}$ is the same for every root — that is why the roots sit on one circle — and only the angle changes, step $2\pi/n$. A modulus such as $2^{1/8}$ stays in that exact form; do not round it to a decimal, because rounding changes which circle the answers live on.

The bookkeeping is the part that costs marks. If the question asks for all roots, you must list $n$ of them; if it asks for one value, you still need the general expression first and then substitute.

### Example 1. Solve $z^3=8$ completely

$$8=8e^{i(0+2\pi k)}$$

The angle is zero because $8$ lies on the positive real axis.

$$z_k=8^{1/3}e^{i2\pi k/3}=2e^{i2\pi k/3}$$

$$z_0=2,\qquad z_1=2e^{i2\pi/3},\qquad z_2=2e^{i4\pi/3}$$

$$z\in\left\{2,\;2e^{i2\pi/3},\;2e^{i4\pi/3}\right\}$$

## 2. Euler's formula as an integration machine

Integrals such as $\int e^{ax}\cos bx\,dx$ are painful by parts because each integration flips the trig function. The exponential form removes the flipping: write $\cos bx$ as the real part of $e^{ibx}$, integrate a single exponential, and take the real part at the end.

$$\int e^{(a+ib)x}\,dx=\frac{e^{(a+ib)x}}{a+ib}$$

$$\int e^{ax}\cos bx\,dx=\operatorname{Re}\!\left(\frac{e^{(a+ib)x}}{a+ib}\right)=\frac{e^{ax}(a\cos bx+b\sin bx)}{a^2+b^2}$$

The lecturer's warning is worth repeating: two minus signs appear when you differentiate $u$ in $\int u\,dv$ — one from the integral of the exponential, one from the chain rule on the exponent. Write them both, or the answer flips sign silently.

### Example 2. $\int_0^{\pi/2}e^{-x}\sin x\,dx$

$$\int_0^{\pi/2}e^{-x}\sin x\,dx=\operatorname{Im}\int_0^{\pi/2}e^{(-1+i)x}\,dx$$

$$\int e^{(-1+i)x}\,dx=\frac{e^{(-1+i)x}}{-1+i}$$

$$\left[\frac{e^{-x}(-\sin x-\cos x)}{2}\right]_0^{\pi/2}=\frac{1}{2}\left(e^{-\pi/2}\cdot(-1)-(-1)\right)=\frac{1-e^{-\pi/2}}{2}$$

$$\int_0^{\pi/2}e^{-x}\sin x\,dx=\frac{1-e^{-\pi/2}}{2}\approx0.396$$

## 3. Imaginary angles connect sinh and sin

Substituting $\theta=i\phi$ into Euler's formula gives the bridge between the two families:

$$\sin(i\phi)=i\sinh\phi,\qquad \cos(i\phi)=\cosh\phi$$

The practical consequence: any trigonometric identity has a hyperbolic twin, obtained by flipping the sign of every $\sin^2$ term. That is the fastest way to recall $\cosh^2\phi-\sinh^2\phi=1$ — it is the twin of $\cos^2\theta+\sin^2\theta=1$.

## 4. What it means to differentiate a complex function

The definition looks identical to the real one:

$$f'(z)=\lim_{\delta z\to0}\frac{f(z+\delta z)-f(z)}{\delta z}$$

But $\delta z$ can approach zero along any path in the plane. For the derivative to exist, every path must give the same limit. The lecture's operational version: check **two independent paths** (for example horizontal and vertical); if they disagree, the function has no derivative there, even though it looks smooth.

This is the reason complex analysis is stricter than real analysis: “smooth as a picture” is not the same as “differentiable as a complex function”.

## 5. Pitfalls, memory hooks and self-check

|---|---|---|
| Too few roots | Missing values | An $n$-th root has exactly $n$ values |
| Rounding the modulus | Answers on the wrong circle | Keep $2^{1/8}$ exact |
| Re instead of Im | Wrong trig function in the answer | $\cos\to\operatorname{Re}$, $\sin\to\operatorname{Im}$ |
| One path for $\delta z$ | Calls a non-differentiable function differentiable | Test two independent paths |

### Self-check

1. Solve $z^2=-4$. Answer: $z=\pm2i$.
2. Compute $\int e^{2x}\cos3x\,dx$. Answer: $\dfrac{e^{2x}(2\cos3x+3\sin3x)}{13}+C$.
3. Write $\sin(2i)$ in terms of sinh. Answer: $i\sinh 2$.
4. Why does $f(z)=|z|^2$ fail to be differentiable at points other than the origin? Answer: the horizontal and vertical difference quotients disagree, so the two paths give different limits.

## 6. Open items

- The second root example used in class was reconstructed from the transcript; the slide's exact numbers were not captured.
- The lecturer said the exam date will be confirmed by email next term (announced in the 2026-11-27 computing lecture); this note does not state a date.
