# Monte Carlo Methods, Random Numbers and High-Dimensional Integration

> Source: Panopto session 79dd5cff-fdf8-4178-b244-b4e200dea211, automatic English subtitles, 59:59.

## 0. What this lecture is about

Why engineers need random sampling at all, how the dart-board estimate of $\pi$ works, what a random number generator actually is in Python, and why the method survives in 27 dimensions where a grid cannot.

## 1. Course arrangements: the exam date has moved

The final exam has **moved from 19 March to the summer term**. The reason given is the clash with all Design and Manufacture deadlines on 19 March; the exact date is still being negotiated and will be sent by email **next term**. A two-page computing data sheet will be provided for every exam, and it will be posted on Canvas.

## 2. Why we need Monte Carlo

The method was born on the Manhattan Project, where physicists needed integrals no formula could solve in closed form. The usual calculus approach is fine in one dimension. The trouble is dimension: a grid with $10$ points per axis needs $10^{d}$ points in $d$ dimensions — $10^{27}$ in 27 dimensions. Monte Carlo replaces the grid by random points, and its error shrinks like $1/\sqrt n$ **regardless of dimension**, so it becomes the only feasible option.

## 3. Estimating $\pi$ by throwing darts

Take the unit square $[0,1]\times[0,1]$ and the quarter disc $x^2+y^2\le1$ inside it. Its area is $\pi/4$. Throw $n$ random points uniformly; if $N_{in}$ land inside the quarter disc,

$$\frac{N_{in}}{n}\approx\frac{\pi}{4}\qquad\Longrightarrow\qquad \pi\approx\frac{4N_{in}}{n}$$

The sampling error of this estimator is about $1.64/\sqrt n$ — the lecture's number for a 95% interval. To gain one more decimal place you need roughly 100 times more points.

### Example 1. The estimator in NumPy

```python
import numpy as np

def estimate_pi(n, seed=42):
    rng = np.random.default_rng(seed)
    x = rng.random(n)
    y = rng.random(n)
    inside = (x*x + y*y) <= 1.0
    p = inside.mean()          # fraction inside the quarter disc
    return 4.0*p, 4.0*np.sqrt(p*(1-p)/n)

for n in (10**3, 10**5, 10**6):
    est, err = estimate_pi(n)
    print(f"n={n:>7}  pi~{est:.4f}  +/-{err:.4f}")
```

## 4. What “random” means in Python

The generator is **pseudo-random**: a deterministic algorithm (PCG64 in NumPy's default) produces a sequence that looks random. Give it the same **seed** — the lecture used 42 — and you get the same numbers every time. That is a feature, not a bug: reproducible experiments are how you debug a simulation.

Physical randomness (radioactive decay, thermal noise) really is unpredictable, but it is expensive and unnecessary here; statistical randomness is all the method needs.

## 5. Monte Carlo integration

The darts idea generalises. To compute $\int_\Omega f\,d\Omega$, draw uniform points $U_i$ in the region and average:

$$I=\int_\Omega f\,d\Omega\approx \frac{V_\Omega}{n}\sum_{i=1}^{n}f(U_i),\qquad \text{error}\sim\frac{\sigma_f}{\sqrt n}$$

The estimator is just “sample value times volume”, and its error depends on the **variance of $f$**, not on the number of dimensions.

### Example 2. $\int_0^1 x^2\,dx$ with a variance check

```python
import numpy as np

def mc_integral(n, seed=42):
    rng = np.random.default_rng(seed)
    u = rng.random(n)
    return u*u

for n in (10**3, 10**4, 10**5, 10**6):
    samples = mc_integral(n)
    est = samples.mean()
    se = samples.std(ddof=1)/np.sqrt(n)
    print(f"n={n:>7}  I~{est:.4f}  +/-{se:.4f}")
```

## 6. Where this is used in engineering

Combustion simulation: a turbulent flame needs a chemical state with roughly 27 dimensions (temperature, pressure and many species), where a grid is hopeless and Monte Carlo is standard. Moon landing: trajectory dispersion and Monte Carlo runs of the guidance loop estimate the probability of a safe touchdown, which is exactly a high-dimensional integral.

## 7. Pitfalls, memory hooks and self-check

|---|---|---|
| Thinking more dimensions needs a bigger grid | $10^{27}$ points | Switch to sampling |
| Different seeds each run | Unreproducible results | Fix the seed, record it |
| Reporting one decimal from $10^3$ points | Fake precision | Quote the standard error |
| Confusing accuracy and variance | “Monte Carlo is always slow” | It is $\sigma/\sqrt n$: cut variance, not just add points |

### Self-check

1. Why does the dart estimate of $\pi$ not improve by 10 when you use 10 times more points? Answer: error falls as $1/\sqrt{10}\approx0.32$, i.e. about a factor of 3.
2. What does **default_rng(42)** guarantee? Answer: the same pseudo-random sequence on the same NumPy version, so results are reproducible.
3. Estimate $\int_0^1 e^x dx$ and explain which quantity controls the error. Answer: sample mean of $e^u$; the error is controlled by $\operatorname{Var}(e^U)$, not by the dimension.

## 8. Open items

- The exact summer-term exam date was not announced; only that it will be emailed next term.
- The lecture mentioned a two-page data sheet going on Canvas; it had not been posted at the time this note was written.
- The 27-dimensional combustion example is quoted as the lecturer described it; the underlying model is not part of this module.