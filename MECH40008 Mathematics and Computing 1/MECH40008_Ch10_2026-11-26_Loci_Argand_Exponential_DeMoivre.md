# Complex Numbers on the Argand Diagram

> Source: Panopto session c5372d45-0d1d-41fc-bdd7-b4c200bdbff5, automatic English subtitles, 1:00:00.

## 0. What this lecture is about

This lecture finishes the geometry of complex numbers and then builds the machinery that turns complex numbers into a calculating tool: the exponential form, Euler's formula, complex logarithms and de Moivre's theorem. The last part shows why the roots of a complex number sit evenly spaced around a circle.

## 1. Course arrangements and the progress test

The lecturer first set the record straight about the progress test. It covers everything **up to and including chapter ten**. Fourier series will **not** appear, because the Fourier lectures are in the last week and one of them is timetabled after the test. A formal slide will follow early next week. He also asked students not to hunt for old papers: the point of the test is to show you where you stand, not to be revised for like an exam.

## 2. Loci are constraint sets, not drawings

For example, $|z-z_0|=r$ says “the distance from $z$ to $z_0$ is $r$”, which is a circle of centre $z_0$ and radius $r$. The inequality $|z-z_0|<r$ is the open disc inside it. In the lecture the example was a circle with centre on the imaginary axis, at $y=2$, and radius $3$, so $|z-2i|=3$.

## 3. Reading the argument from the quadrant

$$\arg z=\begin{cases}\arctan\dfrac{y}{x}, & x>0\\[4pt] \arctan\dfrac{y}{x}+\pi, & x<0\end{cases}$$

A safe habit: sketch the point first, decide the quadrant, then use the formula only to get the reference angle. This costs ten seconds and removes the sign error.

## 4. Convert to Cartesian form before you draw

When an equation is given in modulus-argument form and you need its Cartesian shape, expand $z=x+iy$ and compare real and imaginary parts. The lecture's worked example did exactly this: square out $|z-z_0|^2$, collect terms, and only then recognise a circle. Drawing first and algebra later is how mistakes get buried.

### Example 1. From $|z-2i|=3$ to a circle in the plane

$$|x+i(y-2)|=3$$

This step gets rid of $z$ and leaves two real numbers.

$$x^2+(y-2)^2=9$$

Squaring is allowed because both sides are non-negative; the result is the standard circle equation.

$$x^2+(y-2)^2=9$$

## 5. Euler's formula is a series identity

Euler's formula is not a definition to memorise; it falls out of the Taylor series. Expand $\cos\theta$ and $\sin\theta$, attach $i$ to the sine series, and the two together are exactly the series of $e^{i\theta}$:

$$e^{i\theta}=\cos\theta+i\sin\theta$$

That is why $e^{i\pi}=-1$: the point is at angle $\pi$, so it sits at $(-1,0)$. And it is why multiplying complex numbers adds angles.

## 6. Products, quotients and logarithms

In exponential form the rules become one-line statements:

$$|z_1z_2|=|z_1||z_2|,\qquad \arg(z_1z_2)=\arg z_1+\arg z_2$$
$$\left|\frac{z_1}{z_2}\right|=\frac{|z_1|}{|z_2|},\qquad \arg\left(\frac{z_1}{z_2}\right)=\arg z_1-\arg z_2$$

## 7. De Moivre: powers in one step

$$(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$$

This is just “multiply $n$ times means add the angle $n$ times”. The lecture's example was $(1+i)^{10}$: write $1+i=\sqrt2\,e^{i\pi/4}$, raise it to the tenth power, and get $(\sqrt2)^{10}e^{i10\pi/4}=32e^{i5\pi/2}=32i$.

### Example 2. $(1+i)^{10}$ by de Moivre

$$1+i=\sqrt2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)=\sqrt2\,e^{i\pi/4}$$

The modulus is $\sqrt{1^2+1^2}=\sqrt2$; the angle is $\pi/4$ because the point is at $(1,1)$, halfway between the axes.

$$(1+i)^{10}=(\sqrt2)^{10}e^{i10\pi/4}$$

$$(1+i)^{10}=32i$$

## 8. Roots are evenly spaced points

The $n$-th roots of a complex number all have the same modulus, and their arguments differ by $2\pi/n$. For the cube roots of $1$: $1$, $e^{2\pi i/3}$ and $e^{4\pi i/3}$, three points $120^\circ$ apart on the unit circle, and they add up to zero.

The lecture's closing warning is worth writing down: when $n$ is an integer, adding $2\pi k$ changes nothing; when $n$ is a fraction, the $2\pi k$ is exactly what produces the extra roots. A root is a point; a locus is a curve. Mixing the two up is the usual source of lost marks.

## 9. Pitfalls, memory hooks and self-check

|---|---|---|
| Using $\arctan(y/x)$ alone | Wrong quadrant, angle off by $\pi$ | Sketch first, then pick the branch |
| Radius not squared | $x^2+(y-2)^2=3$ | Right-hand side is $r^2$ |
| Forgetting $2\pi k$ | Too few roots | Count: an $n$-th root has $n$ values |
| Not reducing the angle | Cannot read direction | Reduce modulo $2\pi$ |

### Self-check

1. Write $|z+3i|=2$ as a Cartesian circle. Answer: $x^2+(y+3)^2=4$.
2. Compute $\arg(-1+i)$. Answer: $3\pi/4$ (second quadrant).
3. Compute $(1-i)^6$. Answer: $(\sqrt2)^6e^{-i6\pi/4}=8e^{-i3\pi/2}=-8i$.
4. How many values does the fourth root of $16$ have, and how far apart are they? Answer: four values, $\pi/2$ apart.

## 10. Open items

- The formal progress-test slide had not been shown yet; the chapter limit is from the spoken statement only.
- The lecture's second worked example (the circle with centre at $y=2$) was checked from the transcript; the exact numbers on the slide were not captured.
