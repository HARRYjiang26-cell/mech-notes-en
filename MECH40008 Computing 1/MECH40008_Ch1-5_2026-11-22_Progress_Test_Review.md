# MECH40008 Computing 1 — Progress Test Review (Lectures 1–5)

> **Course**: MECH40008 Mathematics and Computing 1, programming stream (Python).
> **Scope**: the first five lectures of the term = notes Ch1–Ch5 (types and floating point, variables and functions, control flow, data structures, algorithms and complexity).
> **Test**: 9 December, about 45 minutes. Roughly half gym material and half problem-set-style questions; starred challenge questions are normally not examined.
> **Date**: 2026-11-22. **Sources**: the Imperial course notes (printed pages 1–80). Lecture recordings confirm the scope; the notes govern the technical content.
> **Structure**: §0 how to use this → §1–§5 one chapter each (idea / mechanisms / code / worked example / 8 multiple-choice questions / traps) → §6 twelve mixed questions → §7 one-page revision sheet → §8 answer key → §9 coverage table → §10 glossary.

## Contents

- §0 How to use this review
- §1 Types and floating point
- §2 Variables and functions
- §3 Control flow
- §4 Data structures
- §5 Algorithms and complexity
- §6 Twelve mixed questions
- §7 One-page revision sheet
- §8 Answer key
- §9 Coverage table
- §10 Glossary

## 0 How to use this review

### 0.1 Where the scope comes from

In the 13 November lecture the lecturer said the 9 December progress test **covers the first five lectures of this term** and takes about 45 minutes. Half of it is gym material, half is problem-set-style work, and starred challenge questions are normally not examined. The final exam is on 19 March at 09:30 and runs for 90 minutes with a similar structure.

So the boundary of this review is exactly five chapters:

$$\text{Ch1} \to \text{Ch2} \to \text{Ch3} \to \text{Ch4} \to \text{Ch5}$$

NumPy and Matplotlib (Ch6), scientific Python in the wild (Ch7) and Monte Carlo (Ch8) belong to lectures 6–8 and are outside this test.

### 0.2 Spending forty-five minutes

| Stage | Time | What to do |
| --- | --- | --- |
| First pass | 25 min | Work down the paper, bank the predict-the-output and find-the-bug questions |
| Second pass | 12 min | Come back for concept discrimination and complexity questions |
| Finish | 8 min | Check boundaries: half-open ranges, $\ge$ versus $>$, $\text{None}$ versus empty |

Predict-the-output questions must be done on paper. Verify each answer two independent ways: substitute an endpoint, and check the order of magnitude.

### 0.3 Three habits

1. **Name the type before you compute**: a $/$ always returns a float, and $\text{print}$ always returns $\text{None}$.
2. **Name the structure before you discuss the algorithm**: "is this a list, a dictionary or a set" is worth more marks than "how do I write the loop".
3. **Count the innermost statement**: every complexity answer comes from how many times that one line runs.

### 0.4 What past papers exist

I checked the shared Mechnet archive: its root (ME1、ME2、ME3-4), the Year 1 Mathematics folder, and the thirty-five module folders under Year 3/4. It holds Fluid Mechanics, Materials, Mechanics, Mechatronics, Stress Analysis, Thermodynamics, Mathematics and the Year 3/4 modules, but there is no Computing or programming folder anywhere, and the Year 1 papers filed under Mathematics are twelve pure-mathematics questions with no Python in them. This review therefore cites no past-paper year and no question number, and every practice question in it is labelled as a simulated question written to the lecture scope.

---

## Question-type map / what each prompt wants

Every question on a forty-five-minute paper is one of about twenty shapes. Read the prompt, recognise the shape, and write the first stroke in the third column; if a question does not fit any row, it is two rows stacked, so split it and answer each half with its own route.

| Ch | Shape | What the prompt looks like | What to write first | Trap |
| --- | --- | --- | --- | --- |
| 1 | Floats are not exact | why $0.1+0.2 \ne 0.3$ | a binary fraction has finitely many bits, so $0.1$ is stored as a neighbour | saying precision is lost without saying why |
| 1 | Integer range and wrap | does a 16-bit register hold 35000 | $2^{15}-1=32767$ is the ceiling, one more wraps negative | taking $2^{15}$ as the ceiling |
| 1 | Division and rounding | what are `7/2`, `7//2`, `-7//2` | `/` always returns a float, `//` floors | flooring a negative the wrong way |
| 1 | Type mismatch | what does `"3" + 3` do | it raises `TypeError`, convert with `int` or `str` first | assuming Python converts for you |
| 2 | Return values | what does a function without `return` give | `None`, and `print` produces no value either | treating `print` as `return` |
| 2 | Scope | can a function change an outer name | assignment inside builds a local, use `global` to change the outer one | believing the global changed |
| 2 | Mutable default | why the default list keeps growing | the default is built once at definition, then shared | believing it is rebuilt per call |
| 2 | Argument passing | does mutating a list inside the function show outside | the reference travels, an in-place change is visible | believing a copy is passed |
| 3 | Branch order | does reordering the `elif` change the output | put the narrowest condition first | a broad condition swallows the rest |
| 3 | Loop bounds | how many times does `range(1, 5)` run | the stop value is excluded, four passes | counting five |
| 3 | break and continue | what is printed here | a line per pass, including skipped passes | treating a skip as an exit |
| 3 | Short-circuit | is `x != 0 and 1/x > 1` safe | `and` stops when the left side is false | believing both sides run |
| 4 | Aliasing and copying | why does changing `b` change `a` | count the objects first, then the names | treating a slice as a deep copy |
| 4 | Lists and tuples | why can the list inside a tuple change | slots cannot be rebound, the object still can mutate | saying a tuple is immutable through and through |
| 4 | Dictionary keys | can a list be a key | keys must be hashable, a list is not, a tuple is | using a list as a key |
| 5 | Complexity | what is a nested loop | count the innermost statement | reporting $n+n$ instead of $n^{2}$ |
| 5 | Binary search precondition | why sort first | each step halves, $O(\log n)$ | searching an unsorted list |
| 5 | Sort stability | what does stable mean | equal keys keep their relative order | confusing it with speed |
| 5 | Comparing growth | is $n\log n$ always faster than $n^{2}$ | constants decide below the crossover | ignoring the constants |

Three habits make the table usable under time pressure. Name the chapter before you answer, because the wording of the question is set by the chapter, not by the numbers. Write the first stroke before you write the answer, because the first stroke is worth method marks on its own. And when two rows fit, answer the narrower row first, since the marker is looking for the specific mechanism and the broad row never scores it.


## 1 Types and floating point: why 0.1 + 0.2 is not 0.3

### 1.1 What this chapter is about

One sentence: **a computer cannot store most decimals, only the nearest value it can represent.**

Type this and you meet the whole chapter at once:

```python
>>> 0.1 + 0.2 == 0.3
False
```

Nothing is broken. The hardware is doing exactly what the standard says. This chapter takes that from "why" to "what to do about it": how numbers are stored, where the error comes from, when it matters, and how to guard against it in code.

![Roadmap: this chapter starts from values; the later lectures build on them](figures/fig_review_map.png)

The first stop on the map is values. The next four lectures all sit on top of them: values are function inputs, conditions, container items and data for algorithms. A measurement rounded at this first stop is still that rounded value when it reaches the fourth stop.

![The floating-point number line: the gap between neighbours doubles at every power of two](figures/fig_review_floatline.png)

The second figure is the core picture: a floating-point number line is a **ruler with uneven marks**. The marks are dense near $1$ and sparse near $10^{100}$, yet both regions carry the same number of significant digits.

**Remember this: floating-point precision is relative, not absolute.**

### 1.2 Mechanisms you must know

**(1) Four basic types.** Every object has a type, and the type decides which operations make sense.

| Type | Example | Used for |
| --- | --- | --- |
| $\text{int}$ | $\text{count} = 10$ | counts, indices |
| $\text{float}$ | $\text{temp} = 98.6$ | measurements, real numbers |
| $\text{str}$ | $\text{name} = \text{"Alice"}$ | text, labels |
| $\text{bool}$ | $\text{done} = \text{False}$ | yes/no conditions |

Inspect it with $\text{type}(x)$. First trap: **the division operator $/$ always returns a float**, even when two integers divide exactly.

$$16 / 2 = 8.0 \quad (\text{float}), \qquad 16 // 2 = 8 \quad (\text{int})$$

$//$ is **floor division**: $7//2=3$, and $-7//2=-4$ (it floors, it does not truncate towards zero).

**(2) Python integers have no upper limit.** Integers are arbitrary precision; the only limit is memory, and running out raises $\text{MemoryError}$. Integer arithmetic is therefore exact: no rounding and no silent overflow.

Most languages and NumPy arrays store integers in a fixed number of bits, usually 32 or 64. A signed 64-bit integer stops at

$$2^{63}-1 = 9\,223\,372\,036\,854\,775\,807$$

and beyond that it **wraps round silently**. Ariane 5 is exactly this kind of limit.

**(3) A float is 64 bits, stored as IEEE 754 double precision.** The value occupies 64 bits (8 bytes) in three fields:

$$v = (-1)^{s}\,(1.f_1f_2\cdots f_{52})_2 \times 2^{\,e - 1023}, \qquad (1.f)_2 = 1 + \sum_{i=1}^{52} f_i 2^{-i}$$

The fields are one sign bit $s$, an 11-bit exponent $e$ and 52 fraction bits $f_1\cdots f_{52}$. Two details matter:

- **Hidden bit**: after binary normalisation the digit before the point is always $1$, so it is not stored. The stored fraction is 52 bits, but the **effective precision is $52+1=53$ bits**.
- **Bias**: the true exponent $E$ can be negative, but the 11-bit field holds an unsigned integer from $0$ to $2047$. So $e = E + 1023$ is stored and $1023$ is subtracted on the way back. Normalised numbers use $-1022 \le E \le 1023$; $e=0$ and $e=2047$ are reserved for zero, subnormals, infinity and $\text{NaN}$.

**(4) Why floats rather than fixed point.** Three reasons:

- **Dynamic range**: a 64-bit float covers about $2.2\times 10^{-308}$ to $1.8\times 10^{308}$. Fixed point (say "store speed in tenths of a metre per second as an integer") forces you to decide the decimal point in advance, and no single scale covers both the mass of an electron and the distance to a star. The exponent field rescales automatically.
- **Hardware speed**: CPUs have dedicated floating-point units; adds and multiplies are pipelined. Arbitrary-precision integer arithmetic slows down as the numbers grow.
- **Predictable memory**: every float is exactly 8 bytes, so arrays pack tightly. Python's arbitrary-precision integers vary in length and cannot be laid out in one contiguous block.

**(5) Is double precision enough?** Single precision (32 bits) gives about 7 significant decimal digits; double precision (64 bits) gives about 15–16. Engineering work needs the latter, which is why Python's $\text{float}$ is always double precision. Use $\text{numpy.float32}$ in large arrays when 15 digits are unnecessary.

**(6) The floating-point number line.** Between two consecutive powers of two the representable numbers are **equally spaced**; crossing a power of two **doubles** the spacing:

$$\text{between } 1 \text{ and } 2:\ \ \Delta = 2^{-52}, \qquad \text{between } 2 \text{ and } 4:\ \ \Delta = 2^{-51}$$

$$\text{between } 2^{52} \text{ and } 2^{53}:\ \Delta = 1, \qquad \text{between } 2^{53} \text{ and } 2^{54}:\ \Delta = 2$$

**Machine epsilon** is the gap between $1.0$ and the next representable float:

$$\varepsilon_{\text{mach}} = 2^{-52} \approx 2.220\times 10^{-16}$$

A common misstatement is that "$\varepsilon$ is the smallest $x$ with $1+x \ne 1$". **It is not.** Every arithmetic result is rounded to the nearest float, so anything slightly larger than $\varepsilon/2$ already rounds up. The useful statement: **one rounding changes a number by at most $\varepsilon/2 \approx 1.1\times 10^{-16}$ of its size**, which is precisely what "about 16 significant digits" means.

**(7) Past $2^{53}$, adding 1 changes nothing.**

$$2^{53} = 9\,007\,199\,254\,740\,992, \qquad \text{float}(2^{53}) + 1 = \text{float}(2^{53})$$

The spacing just below $2^{53}$ is 1 and just above it is 2, so adding 1 lands exactly halfway between two representable values and rounds back to the even one, while adding 2 does move. **Consequence**: integers above $2^{53}$ may lose precision when converted to float.

**(8) 0.1 cannot be stored exactly, so 0.1+0.2 is not 0.3.** In binary, $0.1$ repeats forever:

$$0.1 = 0.0001100110011\ldots_2 = 1.100110011\ldots_2 \times 2^{-4}$$

With only 52 fraction bits it must be cut and rounded. The same happens to $0.2$ and $0.3$, and **their errors do not cancel**, so the sum $0.1+0.2$ is slightly larger than the stored $0.3$ and $==$ returns $\text{False}$.

**(9) Absorption and catastrophic cancellation.** These two effects cause most numerical errors in scientific code.

**Absorption**: a small number added to a much larger one disappears if it is below half the local spacing.

$$1 + 10^{-16} = 1 \quad (\text{True in Python})$$

**Catastrophic cancellation**: two nearly equal numbers subtracted. The subtraction is exact, but the leading digits cancel and what remains is dominated by the rounding error already inside the operands.

```python
a = 1 + 1e-15          # the rounding error is already inside a
print(a - 1)           # 1.1102230246251565e-15, not 1e-15
```

$a$ itself was accurate to 16 digits; after subtracting 1 the answer is wrong by about 11% in its first digit. The fix is not more precision but a **rewritten formula** with no subtraction:

$$\frac{1-\cos x}{x^{2}} \quad \longrightarrow \quad \frac{2\sin^{2}(x/2)}{x^{2}}$$

The two are algebraically identical, but the second never subtracts and stays accurate for small $x$.

**(10) Special values and tolerances.** $\text{inf}$ appears when a floating result overflows, for example $1\text{e}308\times1\text{e}308$; $\text{nan}$ (not a number) comes from $\text{float('nan')}$ or from a library call that has no defined result, because plain $0/0$ and $0.0/0.0$ raise $\text{ZeroDivisionError}$, and $1\text{e}308^{2}$ raises $\text{OverflowError}$ instead of returning $\text{inf}$. $\text{nan}$ equals nothing, itself included, so $\text{nan} == \text{nan}$ is $\text{False}$ while $\text{nan} \ne \text{nan}$ is $\text{True}$; test it with $\text{math.isnan}$.

So do not lean on exact equality for results that travelled different calculation paths; compare with a tolerance:

```python
import math
math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)     # True
```

$\text{rel\_tol}$ is a relative tolerance: $1\text{e-}9$ means "about 9 significant digits agree". The test is $|a-b| \le \max(\text{rel\_tol}\cdot\max(|a|,|b|),\ \text{abs\_tol})$, so the relative part vanishes near zero and you must pass an $\text{abs\_tol}$ of the size that matters there. Exact cases still work: $0.5 == 0.5$ and $\text{math.isclose}(0.0, 0.0)$ are both $\text{True}$.

### 1.3 What the code looks like

**Example 1: true division versus floor division.**

```python
print(16 / 2)      # 8.0  always a float
print(16 // 2)     # 8    int
print(7 // 2)      # 3    floors
print(-7 // 2)     # -4   floors towards minus infinity, not -3
```

The last line is the one people miss: flooring walks left along the number line, so $-3.5$ becomes $-4$.

**Example 2: the truth about 0.1+0.2.**

```python
print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.2 == 0.3)       # False
import math
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))   # True
```

The first line shows the extra bit; the third gives the answer an engineer wants.

**Example 3: absorption.**

```python
print(1 + 1e-16 == 1)     # True: below half a gap at 1.0
print(1 + 1e-15 == 1)     # False: larger than half a gap
```

The threshold is $\varepsilon/2 \approx 1.1\times 10^{-16}$.

**Example 4: adding 1 past $2^{53}$ does nothing.**

```python
x = float(2**53)
print(x + 1 == x)     # True
print(x + 2 == x)     # False: the spacing is exactly 2
```

**Example 5: cancellation and the rewritten formula.**

```python
import math
x = 1e-8
print((1 - math.cos(x)) / x**2)          # 0.0: the numerator is rounded to 0
print(2 * math.sin(x/2)**2 / x**2)       # 0.5: accurate after rewriting
```

Both should be $0.5$. The first collapses because $\cos x$ rounds to exactly $1.0$.

### 1.4 Worked example E1: a value of 35000 that will not fit in a 16-bit register

**What is asked**

Ariane 5's inertial reference software encoded speed as a fixed-point integer. A non-negative speed $v$ in $\text{m s}^{-1}$ is stored as $\text{int}(10v)$ and decoded by dividing by 10. Take $v = 3500.0$ and answer: (a) what integer is stored, of what type, and does it fit a **signed 16-bit** field? (b) how much do "truncate then scale" and "scale then truncate" differ? (c) if the field must cover $0\sim 4000\ \text{m s}^{-1}$ with decoded spacing at most $0.1$, does $\text{int}(5v)$ work?

**Why this route**

The criterion here is not floating-point accuracy but the **range of a fixed-width field**. The number of bits is fixed, so the set of representable integers is fixed, and the only possible failure is "does not fit". So: encode to an integer, then compare with the field limits. You may not argue "Python computed 35000, so it is fine"; Python integers are arbitrary precision and the failure happens **at the transfer**, not in the arithmetic.

**Step 1: encode and look at the type**

$$\text{stored} = \text{int}(10 \times 3500.0) = 35000$$

This gives the integer $35000$ of type $\text{int}$, decoding back to $35000/10 = 3500.0\ \text{m s}^{-1}$. The value is right.

**Step 2: compare with the signed 16-bit range**

$$-2^{15} \le n \le 2^{15}-1 \quad \Longrightarrow \quad -32768 \le n \le 32767$$

$$35000 > 32767 \quad \Longrightarrow \quad \text{does not fit}$$

The largest decodable speed is

$$\frac{32767}{10} = 3276.7\ \text{m s}^{-1} < 3500\ \text{m s}^{-1}$$

**Step 3: compare the two orders of operations**

$$\text{int}(v)\times 10 = 123 \times 10 = 1230 \quad \text{vs} \quad \text{int}(10v) = \text{int}(1237.5) = 1237$$

With $v = 123.75$: the first truncates to $123$, throws away $0.75$ and multiplies to $1230$ (decoded $123.0$); the second multiplies to $1237.5$ and truncates to $1237$ (decoded $123.7$). **Truncating after scaling cannot recover the lost digit.**

**Where the constant comes from**

$32768$ and $32767$ are $2^{15}$ and $2^{15}-1$: one of the sixteen bits is the sign, leaving fifteen for the magnitude. The positive side has one fewer code because zero occupies a slot.

$35000$ is simply $10\times 3500.0$. The spacing $0.1\ \text{m s}^{-1}$ comes from the scale factor 10: adjacent integers differ by 1, so decoded values differ by $1/10$.

**(c) Does a scale factor of 5 work?** The range does:

$$\frac{32767}{5} = 6553.4\ \text{m s}^{-1} > 4000\ \text{m s}^{-1}$$

but the resolution does not:

$$\frac{1}{5} = 0.2\ \text{m s}^{-1} > 0.1\ \text{m s}^{-1}$$

**At a fixed bit width, range and resolution trade against each other**, exactly as on the floating-point number line in section 1.2(6). The fix is to keep scale 10 and widen the destination to signed 32 bits, with an explicit physical range check.

**Sanity check**

Three independent checks. Magnitude: $3500\ \text{m s}^{-1}$ scaled by 10 is $3.5\times 10^{4}$, the same order as the 16-bit ceiling $3.28\times 10^{4}$ and slightly larger, which matches a "just over the limit" accident. Endpoints: $v=0$ encodes to $0$; $v=3276.7$ encodes to $32767$ exactly at the ceiling; $v=3276.8$ encodes to $32768$ and overflows. Logic: the active and backup systems ran the **same software**, so the same input produced the same illegal conversion; **duplicating hardware does not remove a shared assumption**.

**Answer**

$$\text{stored} = 35000 > 32767 \ \Rightarrow\ \text{overflow}, \qquad v_{\max} = \frac{32767}{10} = 3276.7\ \text{m s}^{-1}$$

Scaling before truncating is required; a scale factor of 5 keeps the range but drops the spacing to $0.2$, which fails the requirement; use a 32-bit field with a range check.

**Traps**

- Believing "Python computed 35000, so it is fine": the overflow happens when the value is **put into the fixed-width field**.
- Treating $\text{int}()$ as rounding: it truncates, so $\text{int}(1237.5)=1237$.
- Truncating before scaling: the lost digit never comes back.
- Checking range but not resolution: a smaller scale factor fits larger speeds but coarser spacing.
- Trusting the backup: same source code, same failure.

![Example poster: Ariane 5 fixed-point telemetry](figures/ex_comp5_ariane.png)

### 1.5 Multiple-choice questions (8)

**Q1.1** What does $\text{print}(0.1 + 0.2 == 0.3)$ output?

- A. $\text{True}$
- B. $\text{False}$
- C. $\text{None}$
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $0.1$, $0.2$ and $0.3$ all repeat in binary and are rounded when stored in 52 bits; the errors do not cancel, so the sum differs from the stored $0.3$.

The other options: A is mathematical intuition, not floating-point fact; C is wrong because a comparison returns a bool; D is wrong because the syntax is valid. Use $\text{math.isclose}$ when you mean "close enough".

</details>

**Q1.2** How many bits does an IEEE 754 double take, and how many are the fraction field?

- A. 32 bits, 23 fraction bits
- B. 64 bits, 52 fraction bits
- C. 64 bits, 53 fraction bits
- D. 80 bits, 64 fraction bits

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: double precision is $1+11+52=64$ bits: one sign, eleven exponent, fifty-two fraction.

The other options: A is single precision; C confuses effective precision (53, including the hidden bit) with the field width; D describes extended precision.

</details>

**Q1.3** What is $\text{float}(2^{53}) + 1 == \text{float}(2^{53})$, and why?

- A. $\text{False}$, because adding 1 always changes something
- B. $\text{True}$, because $x+1$ is exactly halfway between $x$ and $x+2$ and rounds to the even one
- C. $\text{True}$, because Python integers overflow
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the gap doubles at every power of two, so it is $1$ on $[2^{52},2^{53})$ and $2$ on $[2^{53},2^{54})$, and $x+1$ is exactly halfway between $x$ and $x+2$, which rounds to the even value $x$; $x+2$ is representable.

The other options: A ignores the spacing; C is wrong because Python integers do not overflow; D is wrong, and the silence is exactly what makes this dangerous.

</details>

**Q1.4** What is the correct way to test whether two floats are "equal"?

- A. $a == b$
- B. $\text{abs}(a-b) < 1\text{e-}6$ with a fixed threshold
- C. $\text{math.isclose}(a, b, \text{rel\_tol}=1\text{e-}9)$
- D. convert both to strings and compare

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: $\text{isclose}$ uses a relative tolerance that scales with magnitude, which matches the relative nature of floating-point precision.

The other options: A is almost always false; B is too strict near $10^{6}$ and too loose near $10^{-6}$; D compares printed strings, which collapses formatting and storage into one question, since $\text{str}(1.0)$ and $\text{str}(1.00)$ are both $\text{'1.0'}$ and neither tells you the stored bits. An absolute tolerance answers a different question: how far from the target counts as close.

</details>

**Q1.5** What is $\text{print}(1 + 1\text{e-}16 == 1)$?

- A. $\text{True}$, because $1\text{e-}16$ is below half the gap at $1.0$
- B. $\text{False}$, because any non-zero addition changes the result
- C. $\text{True}$, because Python uses integers internally
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: A**

Why: the gap at $1.0$ is $\varepsilon = 2.22\times 10^{-16}$ and half of it is about $1.11\times 10^{-16}$; $1\text{e-}16$ is smaller, so it rounds back to $1.0$. This is absorption.

The other options: B ignores rounding; C is wrong because a Python float is a hardware double; D is wrong.

</details>

**Q1.6** Which statement about $\varepsilon_{\text{mach}} = 2^{-52}$ is correct?

- A. It is the smallest positive float
- B. It is the smallest $x$ with $1+x \ne 1$
- C. It is the gap between $1.0$ and the next float, and one rounding changes a number by at most $\varepsilon/2$ of its size
- D. It equals $2^{-53}$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: $\varepsilon = 2^{-52}$ is the **gap** at $1.0$; because results round to nearest, anything slightly above half the gap moves up, so the "smallest $x$" phrasing is sloppy.

The other options: A is off by hundreds of orders of magnitude; B is the common misstatement; D is half a gap.

</details>

**Q1.7** What is the range of a signed 16-bit integer?

- A. $0 \sim 65535$
- B. $-32768 \sim 32767$
- C. $-32767 \sim 32767$
- D. $-65536 \sim 65535$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: one bit is the sign and fifteen carry the magnitude, so the negative side reaches $-2^{15}$ and the positive side stops at $2^{15}-1$.

The other options: A is unsigned 16-bit; C forgets the extra negative code; D is a wider format.

</details>

**Q1.8** What are $\text{int}(123.75) \times 10$ and $\text{int}(10 \times 123.75)$?

- A. both $1237$
- B. $1230$ and $1237$
- C. $1240$ and $1237$
- D. $1237$ and $1230$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the first truncates to $123$ and multiplies; the second multiplies to $1237.5$ and truncates to $1237$.

The other options: A ignores the order of the truncation; C treats truncation as rounding; D reverses the order. Truncating after scaling cannot recover the lost digit.

</details>

### 1.6 Chapter traps

- Writing $0.1+0.2 == 0.3$: it prints $\text{False}$; use $\text{math.isclose}$.
- Using $\text{rel\_tol}$ against zero: the test never passes; use $\text{abs\_tol}$.
- Calling $\varepsilon$ "the smallest positive number" or "the smallest $x$ with $1+x\ne 1$".
- Judging equality with a fixed $1\text{e-}6$ threshold: it fails as soon as the magnitude changes.
- Truncating before scaling: the decoded value comes back short.
- Treating a fixed-width integer like a Python integer: it wraps silently past its range, which is how Ariane 5 was lost.
- Subtracting two nearly equal numbers: the leading digits vanish, so rewrite the formula instead of raising precision.
- Assuming adding 1 always changes a float: past $2^{53}$ it does not.


### 1.4b How this chapter is examined

Chapter 1 is examined in two shapes. The short shape asks you to predict a printed value: a division that surprises you, an integer that overflows a fixed-width register, or a comparison of two floats that should be equal and is not. The long shape asks you to explain: "state why" is a real one or two marks, and the marker wants the mechanism, which is that a binary mantissa with finitely many bits cannot hold most decimals, so the stored value is the nearest one and the arithmetic inherits that error. Writing "because of precision" earns nothing, because it restates the symptom.

## 2 Variables and functions: names, return and scope

### 2.1 What this chapter is about

One sentence: **a variable is a name, and a function is a name for a stretch of computation.**

Chapter 1 was about what a value looks like. This chapter is about how values get called up and reused. Two things are examined again and again: a function that only prints **returns nothing**, and **assignment does not copy**.

![Names, scope and aliasing: assignment only labels; a local name disappears when the function returns](figures/fig_review_names_scope.png)

The top half shows two names pointing at one list; the bottom half shows a local name inside a function. The arrows point at **objects**; a name is only an arrow.

**Remember this: assignment labels, it does not photocopy; only return hands the result out.**

### 2.2 Mechanisms you must know

**(1) A variable is a name, not a box.** Writing

$$x = 10$$

does not mean $x$ equals $10$; it means: evaluate the right-hand side, get an object, then make the name $x$ refer to it. So

$$x = x + 1$$

reads as "read the current value of $x$, add one, then point $x$ at the new result". The right-hand $x$ uses the **old** value.

**(2) Naming rules.** Letters, digits and underscores only, and it may not start with a digit. Names are case-sensitive ($\text{mass}$ and $\text{Mass}$ are different). Keywords such as $\text{if}$, $\text{for}$, $\text{def}$ and $\text{return}$ cannot be used.

One trap: **do not shadow built-ins.**

```python
sum = 0        # legal, but sum no longer refers to the built-in function
sum([1, 2])    # TypeError: int object is not callable
```

After that line the built-in sum is hidden. Use $\text{total}$ instead.

**(3) What a function is for.** A function packs a computation behind a name. Three benefits:

- **Reuse**: write a formula once and call it many times.
- **Clarity**: a good name says what is computed, not just how.
- **Testing**: a small function can be checked on simple inputs.

**(4) The anatomy of def.**

```python
def distance(x1, y1, x2, y2):
    """Return the Euclidean distance between two 2D points."""
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d
```

- $\text{def}$: the keyword that starts a definition.
- $\text{distance}$: the function name, following the variable naming rules.
- $\text{(x1, y1, x2, y2)}$: **parameters**, the local names for the inputs.
- The triple-quoted line: the **docstring**, documentation for humans.
- The indented block: the body, which only runs when the function is called.
- $\text{return}$: hands the result back and ends the call immediately.

**(5) return and print are different things.** The first trap of the chapter.

$\text{print}$ shows a value to a human and returns $\text{None}$; $\text{return}$ hands the value to the program.

```python
def double(x):
    print(x * 2)      # prints only, no return

print(double(5))      # prints 10, then prints None
double(5) + 15        # TypeError: unsupported operand type(s) for +: NoneType and int
```

Notice the order: $10$ comes from the inner print, then $\text{None}$ is what the call actually returned. Fix it with return:

```python
def double(x):
    return x * 2

double(5) + 15        # 25
```

**Remember this: a number that appeared on screen is not a number you hold.**

**(6) Three kinds of arguments.**

```python
def power(base, exponent=2):
    return base ** exponent

power(3)                      # positional, exponent takes the default, 9
power(3, 3)                   # positional, matched by order, 27
power(3, exponent=3)          # keyword, matched by name, 27
```

- **Positional**: matched by order.
- **Keyword**: matched by name, so order does not matter.
- **Default**: used when the argument is omitted.

**(7) A mutable default is evaluated once.** Second trap:

```python
def collect(x, acc=[]):
    acc.append(x)
    return acc

collect(1)      # [1]
collect(2)      # [1, 2]  <-- not [2]
```

The default list is created **once, when the function is defined**, and every call shares it. Write

```python
def collect(x, acc=None):
    if acc is None:
        acc = []
    acc.append(x)
    return acc
```

**(8) Scope.** Calling a function creates a **local scope**; names inside live there and vanish when the function returns.

$$\text{inside: } y=7 \quad\Longrightarrow\quad \text{outside: } y \text{ does not exist}$$

A function can **read** outer names, but rebinding the same name inside creates a new local and leaves the outer one alone, and reading that name before the assignment raises $\text{UnboundLocalError}$. Rebinding a module-level name needs $\text{global}$, rebinding a name in the enclosing function needs $\text{nonlocal}$; mutating a shared object in place needs neither declaration. The course discourages both keywords, so return a value instead.

**(9) Functions calling functions.** Splitting a problem into small functions is the main way to keep complexity down: five well-named functions read like five physical ideas rather than a pile of algebra.

### 2.3 What the code looks like

**Example 1: assignment is an action, not an equation.**

```python
x = 10
x = x + 1
print(x)      # 11
```

The second line evaluates $10+1=11$ and then makes $x$ refer to $11$.

**Example 2: a function wraps a formula and can be reused and tested.**

```python
def kinetic_energy(m, v):
    return 0.5 * m * v**2

print(kinetic_energy(2.0, 3.0))    # 9.0
print(kinetic_energy(10.0, 4.0))   # 80.0
```

Inputs are mass and speed, output is energy; $0.5\times 2\times 3^{2}=9$ checks out.

**Example 3: a function that only prints hands back nothing.**

```python
def average(a, b):
    print((a + b) / 2)

result = average(4, 8)     # screen: 6.0
print(result)              # screen: None
```

Anything computed from $\text{result}$ will fail. This is the most common find-the-bug question in the exam.

**Example 4: swapping two variables the wrong way.**

```python
a = 1
b = 2
a = b      # a becomes 2, the old 1 is lost
b = a      # b becomes 2 as well
print(a, b)   # 2 2
```

Either use a temporary variable, or use tuple assignment $\text{a, b = b, a}$.

### 2.4 Worked example E2: a unit error of 4.45 and a lost spacecraft

**What is asked**

In Mars Climate Orbiter, the module that computed thruster impulse produced pound-force seconds while the navigation module consumed newton-seconds. Given $1\ \text{lbf}\approx 4.448\ \text{N}$, by what factor is the impulse misread? And what would have happened if the computing function had printed instead of returned?

**Why this route**

There is only one route for units: convert both to a common basis and compare. The thrust curve is irrelevant; only the ratio of the two unit systems matters. Structurally the bug is not in the formula but in the **interface contract**: a returned value must carry its unit, otherwise the caller can only guess.

**Step 1: write both impulses**

$$I_{\text{calc}} = F\,\Delta t \quad \text{in}\ \text{lbf}\cdot\text{s}, \qquad I_{\text{used}} = I_{\text{calc}}\ \text{treated as}\ \text{N}\cdot\text{s}$$

The number is used unchanged; what is wrong is the label, not the multiplication.

**Step 2: compute the ratio**

$$\frac{I_{\text{used}}}{I_{\text{true}}} = \frac{1\ \text{N}\cdot\text{s}}{1\ \text{lbf}\cdot\text{s}} = \frac{1}{4.448} \approx 0.2248$$

The value is only $22.5\%$ of the true impulse.

**Step 3: turn the bias into accumulated error**

$$\Delta I = (4.448 - 1)\,I_{\text{calc}} \approx 3.45\,I_{\text{calc}}$$

Each burn's computed impulse is only about $22.5\%$ of the impulse actually applied, so the miss per burn is about $3.45$ times the computed value, and the error accumulates with the number of burns.

**Where the constant comes from**

$4.448$ is not arbitrary: one pound-force is the weight of one pound mass under standard gravity.

$$1\ \text{lbf} = 0.45359237 \times 9.80665 \approx 4.4482\ \text{N}$$

**Sanity check**

Reverse the direction: if the navigation side had misread $\text{N}\cdot\text{s}$ as $\text{lbf}\cdot\text{s}$, the ratio would be $4.448$, i.e. too large, not too small. The observed factor $0.2248$ matches "computed in $\text{lbf}\cdot\text{s}$, consumed as $\text{N}\cdot\text{s}$". Order of magnitude: $0.2248\times 4.448\approx 1.000$, so the two ends close.

On the function level: had the impulse function only printed, the caller would receive $\text{None}$ and raise $\text{TypeError}$ immediately. **The accident happened precisely because the function returned a perfectly good number**; the value was fine, the unit was not documented. Working code is not the same as correct code.

**Answer**

$$\frac{I_{\text{used}}}{I_{\text{true}}} = \frac{1}{4.4482} \approx 0.2248, \qquad \text{bias factor} \approx 4.45$$

**Traps**

- Reading $4.45$ as $4.45\%$: it is a factor; $0.2248$ is the fraction.
- Believing "it returned a number, so it is right": right type, wrong unit is the hardest class of bug.
- Computing a single burn: the damage is the **accumulation** over the mission.

![Example poster: return versus print](figures/ex_comp5_orbiter.png)

### 2.5 Multiple-choice questions (8)

**Q2.1** What does this program output?

```python
def double(x):
    print(x * 2)

print(double(5))
```

- A. $10$
- B. $10$ then $\text{None}$
- C. $\text{None}$
- D. $\text{TypeError}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the inner call prints $10$ and returns $\text{None}$; the outer print then shows $\text{None}$.

The other options: A misses the outer print; C misses the inner print; D only happens when the $\text{None}$ is used in arithmetic.

</details>

**Q2.2** After these three lines, what are $a$ and $b$?

```python
a = 5
b = a
a = a + 1
```

- A. $a=6$, $b=6$
- B. $a=6$, $b=5$
- C. $a=5$, $b=6$
- D. $a=6$, $b=\text{None}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: integers are immutable. $b=a$ points $b$ at $5$; $a=a+1$ creates a new $6$ and re-points $a$, leaving $b$ at $5$.

The other options: A treats names as storage cells; C reverses the order; D is unrelated, assignment never produces $\text{None}$. With a mutable value such as a list the answer changes, which is the chapter 4 trap.

</details>

**Q2.3** Which definition makes $\text{power(3)}$ return $9$?

- A. $\text{def power(base, exp): return base ** exp}$
- B. $\text{def power(base, exp=2): return base ** exp}$
- C. $\text{def power(base=2, exp): return base ** exp}$
- D. $\text{def power(base, exp): return base * exp}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the default lets the second argument be omitted, so $3^{2}=9$.

The other options: A raises $\text{TypeError}$ for a missing argument; C is a syntax error because a defaulted parameter must follow the non-defaulted ones; D computes $3\times 2=6$.

</details>

**Q2.4** What do the two calls print?

```python
def collect(x, acc=[]):
    acc.append(x)
    return acc

print(collect(1))
print(collect(2))
```

- A. $[1]$ and $[2]$
- B. $[1]$ and $[1, 2]$
- C. $[1]$ and $[]$
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the default list is created once at definition time, so both calls share it and the second sees the first append.

The other options: A is the intuitive but wrong answer; C implies a clearing that never happens; D is wrong, and the silence is what makes it dangerous. Fix: default to $\text{None}$ and build a fresh list inside.

</details>

**Q2.5** Which statement about $\text{return}$ and $\text{print}$ is correct?

- A. They are equivalent
- B. $\text{print}$ returns to the caller and $\text{return}$ only displays
- C. $\text{return}$ hands the value back and ends the function; $\text{print}$ only displays and the function returns $\text{None}$
- D. Every function must use both

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: only $\text{return}$ hands a value out; $\text{print}$ writes to the screen.

The other options: A conflates them; B reverses them; D is not required by any language rule.

</details>

**Q2.6** Does this program raise an error?

```python
def f():
    total = 10

f()
print(total)
```

- A. prints $10$
- B. prints $\text{None}$
- C. raises $\text{NameError}$
- D. raises $\text{TypeError}$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: $\text{total}$ is local and disappears when the call returns, so the name does not exist outside.

The other options: A assumes locals leak; B requires an existing name whose value is $\text{None}$; D is unrelated. Return the value if you need it.

</details>

**Q2.7** Which definition is bad practice?

- A. $\text{def area(r): return 3.14159 * r**2}$
- B. $\text{def mean(a, b): return (a + b) / 2}$
- C. $\text{def sum(x): return x + 1}$
- D. $\text{def f(x, y=1): return x * y}$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: $\text{sum}$ is a built-in name; redefining it hides the built-in for the rest of the program.

The other options: A, B and D are all legal and normal. Naming is style, but shadowing a built-in causes real bugs.

</details>

**Q2.8** Which expression successfully computes twice the average of 4 and 8?

- A. $\text{print((4+8)/2) * 2}$
- B. $((4+8)/2) * 2$
- C. $x = \text{print}((4+8)/2)$ then $x * 2$
- D. impossible without a variable

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: it is a pure expression that evaluates to $12$.

The other options: A multiplies the return value of print, which is $\text{None}$; C does the same through a variable; D is false.

</details>

### 2.6 Chapter traps

- Printing instead of returning: the caller receives $\text{None}$ and the next arithmetic step raises $\text{TypeError}$.
- A default of $\text{acc=[]}$: every call shares one list, so the second call returns $[1, 2]$.
- Assuming $b = a$ copies a list: both names point at one object.
- Shadowing built-ins such as $\text{sum}$ or $\text{list}$: the built-in becomes unreachable.
- Expecting a function to change an immutable argument in place: the outer value never changes.
- Treating units as comments: right type, wrong unit, program runs, result is wrong by a factor.
- Swapping the argument order: $\text{power(3, 2)}$ is not $\text{power(2, 3)}$.

### 2.4b How this chapter is examined

Chapter 2 is examined as find-the-bug and as short trace. Find-the-bug gives you a function and asks why the second call returns something different from the first: the usual answer is a mutable default argument, built once at definition time. Short trace gives you a function that prints instead of returning, or that rebinds a name inside its own body, and asks what the caller sees: the answer is `None`, or the global unchanged. Both shapes reward the same sentence, "assigning inside a function creates a local name unless `global` is declared", so learn that sentence as a sentence.

## 3 Control flow: the order of branches is the logic

### 3.1 What this chapter is about

One sentence: **the program stops running straight down and starts deciding and repeating.**

The first two chapters were straight lines. This chapter adds junctions ($\text{if}$) and loops ($\text{while}$, $\text{for}$). Two things are examined: **the order of branches is the logic**, and **inside a loop somebody must make progress**.

![Control flow: the first true branch wins, break leaves only the innermost loop, continue skips the rest of the iteration](figures/fig_review_control_flow.png)

Three things to keep from the figure: $\text{if}/\text{elif}/\text{else}$ is tried top to bottom and stops at the first hit; $\text{while}$ must make progress itself; $\text{for}$ makes progress automatically.

**Remember this: branches are tried in written order and the first hit wins; a loop with nobody making progress never ends.**

### 3.2 Mechanisms you must know

**(1) Booleans.** Two values, $\text{True}$ and $\text{False}$, capitalised, type $\text{bool}$. Comparisons produce them.

- $==$ tests equality; $=$ assigns. Do not confuse them.
- $<$, $>$, $\le$, $\ge$ compare magnitude.
- $\text{is}$ tests whether two names refer to the **same object**, not whether values are equal. Use $\text{is None}$ for $\text{None}$ and $==$ for values.
- Comparisons chain: $0 \le x < 10$ means both conditions, exactly as in mathematics, and chapter 4 uses it for interval filtering.
- Chapter 1 still applies: **never compare floats with $==$**; use $\text{math.isclose}$.

$$x = 3 \quad\Longrightarrow\quad x == 3\ \text{is}\ \text{True}, \qquad x != 3\ \text{is}\ \text{False}$$

**(2) Precedence.** Brackets, then function calls and arithmetic, then comparisons, then $\text{not}$, then $\text{and}$, then $\text{or}$.

$$\text{not}\ 10 > 5\ \text{and}\ \text{True}\ \text{or}\ 1 \ne 1 \;\equiv\; ((\text{not}(10>5))\ \text{and}\ \text{True})\ \text{or}\ (1\ne 1) = \text{False}$$

Step by step: $10>5$ is $\text{True}$, negated gives $\text{False}$; $\text{False}$ and $\text{True}$ gives $\text{False}$; $1\ne 1$ is $\text{False}$; $\text{False}$ or $\text{False}$ gives $\text{False}$. When unsure, add brackets: they cost nothing.

**(3) Short-circuit evaluation.** In $\text{A and B}$, if $\text{A}$ is false the whole expression is false and $\text{B}$ is never evaluated. In $\text{A or B}$, if $\text{A}$ is true, $\text{B}$ is skipped.

This lets the first test **guard** the second:

```python
x = 0
if x != 0 and (10 / x) > 1:     # with x = 0 the division never runs
    print("safe")
```

Swap the two conditions and you get $\text{ZeroDivisionError}$.

**(4) Truthiness.** These are false as conditions: $0$, $0.0$, $\text{None}$, the empty string, the empty list, the empty dictionary. Almost everything else is true. $\text{if readings:}$ asks "is there anything in it". While learning, explicit conditions such as $\text{if n != 0:}$ read better.

**(5) if / elif / else.** Tried top to bottom; **the first true branch runs and everything below is skipped**. So the order is the logic:

```python
speed = 45
if speed > 70:
    print("Too fast")
elif speed < 30:
    print("Too slow")
else:
    print("Speed OK")
```

Write $\text{if x > 18}$ before $\text{elif x > 21}$ and the second branch is unreachable. **For thresholds, test the most restrictive first.**

**(6) while: repeat an unknown number of times.** It runs while the condition holds, and **you** must change something:

```python
x = 0
while x < 3:
    print(x)
    x += 1        # forget this and the loop never ends
```

Forgetting the increment, or skipping it with $\text{continue}$, is an infinite loop.

**(7) for: a known number of repetitions, or a walk over a sequence.**

$$\text{range}(\text{start},\ \text{stop},\ \text{step}), \qquad \text{stop excluded}$$

- $\text{range}(5)$ gives $0,1,2,3,4$: five values, no $5$.
- $\text{range}(2, 10, 3)$ gives $2,5,8$.
- $\text{range}(10, 0)$ is **empty**, because the default step is $+1$ and $10$ is already past $0$. Count down with $\text{range}(10, 0, -1)$.

The half-open convention matches indexing from zero and returns in chapter 4 slicing. If you only need the values, iterate the sequence directly: $\text{for r in readings:}$ is clearer than $\text{for i in range(len(readings)):}$.

**(8) Nested loops.** The outer loop runs $m$ times and the inner $n$ times, so the body runs $mn$ times. Indentation decides which statements belong to which level, and statements after the inner loop belong to the outer one. This is where the $O(n^{2})$ of chapter 5 comes from.

**(9) break and continue.**

- $\text{break}$ leaves the **innermost** loop immediately.
- $\text{continue}$ skips the rest of the current iteration and starts the next.
- In nested loops, $\text{break}$ only leaves the inner one.

In a $\text{while}$ loop, a $\text{continue}$ that jumps over the update creates an infinite loop.

### 3.3 What the code looks like

**Example 1: order decides the logic.**

```python
x = 25
if x > 18:
    print("A")
elif x > 21:
    print("B")
else:
    print("C")
```

This prints $A$. $B$ can never print, because any $x$ reaching the second test already passed the first. Sort the thresholds to make all three reachable.

**Example 2: short-circuit guards a division.**

```python
x = 0
y = 10
if x != 0 and (y / x) > 1:
    print("safedivisionperformed")
```

Nothing prints and nothing crashes: the first condition is false, so the right side never runs.

**Example 3: range is half-open.**

```python
for i in range(5):
    print(i)          # 0 1 2 3 4

for i in range(10, 0, -1):
    print(i)          # 10 9 8 ... 1

for i in range(10, 0):
    print(i)          # nothing at all
```

The third loop prints nothing, which is a favourite exam question.

**Example 4: continue filters bad readings.**

```python
readings = [50, 90, -1, 70, -1, 100]
total = 0
for r in readings:
    if r < 0:
        continue          # skip invalid readings
    total += r
print(total)              # 310
```

Six readings, two skipped, $50+90+70+100=310$.

**Example 5: break leaves only the inner loop.**

```python
for outer in ["A", "B"]:
    print(outer)
    for inner in range(3):
        if inner == 1:
            break
        print(inner)
```

This prints $A\ 0\ B\ 0$: the inner loop is cut each time but the outer one continues.

### 3.4 Worked example E3: one false signal and a lost lander

**What is asked**

Mars Polar Lander's descent is divided into control cycles. In cycle $i$, $\text{height}[i]$ is the height above ground (metres, non-increasing) and $\text{touch}[i]$ says whether the touchdown sensor fired. Two rules must hold: readings above the enabling height $h_{\text{enable}}$ must have **no effect**, and touchdown is declared on the **second consecutive** triggered cycle. How do you write this, and why can a single spurious pulse not cut the engines?

**Why this route**

One $\text{if}$ cannot express two rules. This needs a **gate** (only readings at or below the enabling height count) and a **counter** (how many consecutive cycles fired). A gate is a Boolean; "consecutive" is a count; both must be stored. That is the structural difference from a single-condition question: state has to survive between cycles.

**Step 1: write the two rules as a state machine**

$$\text{armed}_i = \left[\, \text{height}[i] \le h_{\text{enable}} \,\right], \qquad c_i = c_{i-1}+1 \ \text{if}\ \text{armed}_i \wedge \text{touch}[i],\ \text{else}\ 0$$

The counter increments only when the height is low enough and the sensor fired; every other case resets it, which is what "consecutive" means.

**Step 2: declare touchdown**

$$\text{landing} = \left[\, c_i \ge 2 \,\right]$$

Testing $\ge 2$ rather than $== 2$ tolerates a repeated delivery in one cycle.

**Step 3: write the code**

```python
def touchdown_cycle(height, touch, h_enable):
    count = 0
    for i in range(len(height)):
        if height[i] <= h_enable and touch[i]:
            count += 1
        else:
            count = 0
        if count >= 2:
            return i
    return None
```

The function returns the first cycle that satisfies the rule, or $\text{None}$.

**Where the constant comes from**

The $2$ is not estimated: the rule says "two consecutive cycles". The $\le$ follows the sentence "above the enabling height must have no effect": at exactly the enabling height the sensor is allowed to work. Both come straight from the wording.

**Sanity check**

A spurious-pulse case: $\text{height}=[1000, 900, 200, 150, 40]$, $\text{touch}=[\text{T}, \text{F}, \text{F}, \text{F}, \text{F}]$, $h_{\text{enable}}=300$. The first two cycles are gated out, so the count stays $0$; below $200$ nothing fires, so it stays $0$ and the call returns $\text{None}$: no engine cut. A genuine landing: $\text{height}=[40, 20]$, $\text{touch}=[\text{T}, \text{T}]$ reaches $\text{count}=2$ at the second cycle and returns $1$.

**Answer**

$$\text{arm at } h<h_{\text{enable}},\quad \text{count consecutive triggers},\quad \text{fire when } c_i \ge 2$$

A single pulse can only reach $1$, so it cannot cut the engines; the gate plus the counter is exactly what separates "one misread" from "actually landed".

**Traps**

- Chaining the two rules with $\text{elif}$: one rule swallows the other.
- Writing only $\text{if touch[i]}$: a high-altitude false trigger cuts the engines.
- Incrementing but not resetting: two non-consecutive triggers add up and "consecutive" is lost.
- Using $\text{continue}$ where $\text{break}$ is meant.

![Example poster: control flow and the two-consecutive-cycle rule](figures/ex_comp5_polar.png)

### 3.5 Multiple-choice questions (8)

**Q3.1** What does this print?

```python
x = 25
if x > 18:
    print("A")
elif x > 21:
    print("B")
else:
    print("C")
```

- A. $A$
- B. $B$
- C. $A$ then $B$
- D. $C$

<details><summary>Answer and explanation</summary>

**Answer: A**

Why: $x>18$ is true, so the first branch runs and the rest of the chain is skipped.

The other options: B assumes the chain picks the "better" branch; C assumes several branches can run; D requires all earlier tests to fail.

</details>

**Q3.2** What does $\text{print(not True or True and not False)}$ print?

- A. $\text{True}$
- B. $\text{False}$
- C. $\text{None}$
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: A**

Why: $\text{not}$ applies first, then $\text{and}$, then $\text{or}$: $\text{False or (True and True)} = \text{False or True} = \text{True}$.

The other options: B evaluates $\text{or}$ before $\text{and}$; C is not a Boolean result; D is not a syntax error.

</details>

**Q3.3** What happens here?

```python
x = 0
while x < 3:
    if x == 1:
        continue
    print(x)
    x += 1
```

- A. prints $0\ 1\ 2$
- B. prints $0\ 2$
- C. prints $0$ then hangs
- D. raises an error

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: at $x=1$ the $\text{continue}$ skips the increment, so $x$ stays $1$ and the condition stays true forever.

The other options: A ignores continue; B assumes continue advances something; D is wrong, and the hang is why this bug is hard to find. Move the increment above the $\text{continue}$ or use a $\text{for}$ loop.

</details>

**Q3.4** How many times does $\text{range}(10, 0)$ iterate?

- A. 10
- B. 9
- C. 0
- D. infinitely many

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: the default step is $+1$ and the start is already past the stop, so the sequence is empty.

The other options: A and B assume range counts down automatically; D is impossible because range is finite. Write $\text{range}(10, 0, -1)$ to count down.

</details>

**Q3.5** How many times does the body run?

```python
count = 0
for i in range(0, 5, 2):
    for j in range(i):
        count += 1
```

- A. 4
- B. 6
- C. 10
- D. 15

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $i$ takes $0, 2, 4$, so the inner loops run $0$, $2$ and $4$ times: $0+2+4=6$.

The other options: A miscounts the inner lengths; C assumes $i$ runs over all integers; D multiplies $5\times 3$ and ignores that the inner count varies.

</details>

**Q3.6** Which condition safely avoids division by zero?

- A. $\text{if (y / x) > 1 and x != 0:}$
- B. $\text{if x != 0 and (y / x) > 1:}$
- C. $\text{if x != 0 or (y / x) > 1:}$
- D. $\text{if not x == 0 or (y / x) > 1:}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $\text{and}$ short-circuits left to right, so when $x$ is $0$ the division is never evaluated.

The other options: A divides before testing; C and D use $\text{or}$, which does not guard the second operand.

</details>

**Q3.7** What does this print?

```python
for outer in ["A", "B"]:
    print(outer)
    for inner in range(3):
        if inner == 1:
            break
        print(inner)
```

- A. $A\ 0\ 1\ 2\ B\ 0\ 1\ 2$
- B. $A\ 0\ B\ 0$
- C. $A\ 0\ 1\ B\ 0\ 1$
- D. $A\ 0$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: break leaves only the inner loop; the outer loop continues and the inner loop restarts.

The other options: A is the output without break; C misplaces where break takes effect; D assumes break ends everything.

</details>

**Q3.8** What is the clearest way to test whether $\text{values}$ has any content?

- A. $\text{if len(values) > 0:}$
- B. $\text{if values:}$
- C. $\text{if values != None:}$
- D. $\text{if values is True:}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: an empty list is false and a non-empty list is true, so $\text{if values:}$ means "has content".

The other options: A works but is verbose; C is true for an empty list as well, so it misjudges; D is never true for a list.

</details>

### 3.6 Chapter traps

- Writing $\text{elif}$ thresholds in the wrong order: the later branch becomes dead code.
- Forgetting the update in $\text{while}$, or skipping it with $\text{continue}$: infinite loop.
- Mixing up half-open ranges: $\text{range}(5)$ is five values and $\text{range}(10,0)$ is empty.
- Swapping $\text{and}$ and $\text{or}$: the guard disappears and you divide by zero.
- Expecting $\text{break}$ to leave every loop: it leaves only the innermost one.
- Writing $\text{if x = 3}$: a syntax error.
- Comparing floats with $==$ instead of $\text{math.isclose}$.
- Confusing truthiness with "equals $\text{True}$": an empty list is false but is not equal to $\text{True}$.


### 3.4b How this chapter is examined

Chapter 3 is examined by predictable output on a piece of control flow you have not seen before. Two shapes dominate. The branch shape reorders `if` and `elif` so that a broad condition swallows a specific one, and the mark is lost by reading only the first line that matches. The loop shape mixes `break`, `continue` and an accumulator, and the mark is lost by tracing only the passes that print. Write one line per pass, including skipped passes, and the answer becomes mechanical.

## 4 Data structures: lists, dictionaries, tuples and aliasing

### 4.1 What this chapter is about

One sentence: **choose the wrong structure and even a good algorithm is slow; get aliasing wrong and changing one thing changes two.**

The previous chapters handled a single number. Engineering handles collections: a set of measurements, a table from temperature to fault count, a point. This chapter gives three containers and spends most of its time on the trap: **assignment is not copying**.

![Choosing a structure: lists keep order, dictionaries keep lookups, tuples promise immutability](figures/fig_review_structures.png)

One line from the figure: **order and duplicates need a list, fast lookup needs a dictionary, a fixed record that must not change needs a tuple.**

**Remember this: lists keep order, dictionaries keep lookups, tuples keep promises.**

### 4.2 Mechanisms you must know

**(1) Lists.** Ordered, duplicates allowed, mutable, written with square brackets:

$$\text{readings} = [50, 90, 75], \qquad \text{readings}[0] = 50, \quad \text{readings}[-1] = 75$$

- Index from $0$; $-1$ is the last item.
- Slicing $\text{readings}[1:3]$ takes items $1$ and $2$: **half-open**, the same convention as $\text{range}$.
- $\text{append}$ adds at the end; $\text{len}$ gives the size.
- Membership $x\ \text{in list}$ is a **linear scan**, $O(n)$: in the worst case the whole list is examined.

**(2) Dictionaries.** Keys mapped to values, written with braces:

$$\text{by\_temp} = \{60{:}\ [2, 0],\ 70{:}\ [1]\}, \qquad \text{by\_temp}[60] = [2, 0]$$

- Keys are unique and hashable: numbers, strings and tuples work; lists do not.
- $\text{in}$ and lookup by key are $O(1)$ on average: no scanning, the position is computed.
- $\text{items()}$ yields key and value together; $\text{setdefault(key, [])}$ creates a default when the key is missing.
- Iteration follows insertion order; sort explicitly with $\text{sorted(by\_temp.items())}$.

**(3) Tuples.** Parentheses, immutable once built:

$$\text{point} = (36,\ 70), \qquad x, y = \text{point}$$

- The slots are fixed, so a tuple is hashable — and can be a dictionary key — only when every element is hashable: $\text{hash}((1,2))$ works, $\text{hash}((1,[2]))$ raises $\text{TypeError}$. Sharing it is safe from rebinding, not from mutating a list inside it.
- Unpacking assigns several names at once; swapping variables relies on it.
- A function returning several values returns one tuple.

**(4) Aliasing: assignment only labels.** The biggest trap in the chapter:

```python
a = [10, 20, 30]
b = a             # no copy: two names, one list
b.append(40)
print(a)          # [10, 20, 30, 40]
```

To copy, slice or call $\text{copy}$:

$$b = a[:] \quad \text{or} \quad b = a.\text{copy}()$$

Both are **shallow copies**: only the outer level is copied and any nested lists are still shared. Use $\text{copy.deepcopy}(a)$ for nested structures.

**(5) Why parallel lists break.** Two lists of equal length are related only by the promise that index $i$ belongs to the same record:

```python
temps  = [60, 70, 60]
faults = [1, 0, 0]
```

Delete one item or sort one list and the correspondence is gone. Put the relationship into the data:

```python
records = [(60, 1), (70, 0), (60, 0)]
```

or group the values into a dictionary. **A relationship either lives in the data or it will eventually fail.**

**(6) How to choose.** Ask three questions: is order needed, is fast lookup by key needed, must the record be unchangeable. The answers point to list, dictionary and tuple respectively. Real programs mix them: a dictionary of groups, values that are lists, keys that are tuples.

### 4.3 What the code looks like

**Example 1: indexing and slicing.**

```python
values = [10, 20, 30, 40, 50]
print(values[0])      # 10
print(values[-1])     # 50
print(values[1:3])    # [20, 30]  half-open
print(len(values))    # 5
```

**Example 2: grouping by temperature.**

```python
records = [(60, 1), (70, 0), (60, 0)]
groups = {}
for temp, faults in records:
    groups.setdefault(temp, []).append(faults)
print(groups)     # {60: [1, 0], 70: [0]}
```

$\text{setdefault}$ takes care of "the key does not exist yet".

**Example 3: aliasing versus a shallow copy.**

```python
a = [1, 2]
b = a          # alias
c = a[:]       # shallow copy
a.append(3)
print(b)       # [1, 2, 3]  followed
print(c)       # [1, 2]     unchanged
```

**Example 4: tuple unpacking swaps values.**

```python
a, b = 1, 2
a, b = b, a
print(a, b)    # 2 1
```

The right-hand side is packed into a tuple first, then unpacked, so no temporary variable is needed.

**Example 5: the grouping trap that overwrites.**

```python
def group(records):
    groups = {}
    for temp, faults in records:
        if temp not in groups:
            groups[temp] = []
        groups[temp].append(faults)
    return groups
```

The name of the game is "create the list once, then append". Writing $\text{groups[temp] = [faults]}$ replaces the earlier records for that temperature with the newest one.

### 4.4 Worked example E4: Challenger and what "failure rate" means

**What is asked**

A set of test records gives, for each test, a temperature and the number of damaged seals. (a) group by temperature; (b) for an interval $[\text{low},\ \text{high})$ return the number of tests and the fraction with any damage; (c) explain why averaging the two interval fractions directly is wrong and how to pool them.

**Why this route**

A statistic is meaningless until the denominator is named. There are two different quantities here: **incidents per flight** (numerator incidents, denominator flights) and **fraction of tests with any damage** (numerator damaged tests, denominator tests). The question asks for the second, so the records must be expanded to one row per test and counted. Averaging an average gets the weights wrong.

**Step 1: group**

$$\text{groups}[t] = [\, f_1, f_2, \dots \,], \qquad t = \text{temperature}$$

One position per test.

**Step 2: filter the interval and count**

$$\text{tests} = \sum_{t \in [\text{low},\text{high})} \#\text{groups}[t], \qquad \text{faulty} = \sum_{t \in [\text{low},\text{high})} \#\{\, f \in \text{groups}[t] : f > 0 \,\}$$

Two counters; a test with $f=0$ enters only the denominator.

**Step 3: divide**

$$\text{fraction} = \frac{\text{faulty}}{\text{tests}}$$

This is a weighted average, weighted by the number of tests.

**Where the constant comes from**

In the worked data the interval $[60, 80)$ holds five tests, three of them damaged, so $\text{fraction}=3/5=0.6$. Suppose the cold group is $2/3$ and the warm group $1/2$; averaging the fractions gives

$$\frac{2/3 + 1/2}{2} = \frac{7}{12} \approx 0.583$$

but if the cold group has three tests and the warm group two, the correct pooling is

$$\frac{3\cdot \frac{2}{3} + 2 \cdot \frac{1}{2}}{3+2} = \frac{2+1}{5} = 0.6$$

The difference comes from the weights $3$ and $2$: averaging gives the smaller group too much say. So $0.583$ versus $0.6$ is a weighting error, not rounding.

**Sanity check**

Count directly: $\text{faulty}=3$, $\text{tests}=5$, so $3/5=0.6$, inside $[0,1]$ and equal to the weighted formula. Check the empty interval: it must return $(0, \text{None})$, because $0/0$ is undefined. **No data and no failures are different statements.**

**Answer**

$$\text{fraction}([\text{low},\text{high})) = \frac{\#\{\text{tests with any damage}\}}{\#\{\text{tests}\}}, \qquad \text{cold}\ [0,66): 1.0,\quad \text{warm}\ [66,100): 0.158$$

The cold group is entirely damaged; about one warm test in six is. On 28 January 1986 the launch temperature was about $36\ ^\circ\text{F}$ against a previous minimum of $53\ ^\circ\text{F}$, outside the range the data covered. That extrapolation, not the arithmetic, was the risk.

**Traps**

- Mixing incidents per flight with the fraction of damaged tests.
- Averaging two percentages: $0.583$ instead of $0.6$.
- Dropping the $f=0$ tests from the denominator: the fraction is inflated.
- Writing the interval closed: it is half-open, like slices and range.

![Example poster: dictionary grouping, weighted fractions and shallow copies](figures/ex_comp5_challenger.png)

### 4.5 Multiple-choice questions (8)

**Q4.1** What does this print?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

- A. $[1, 2, 3]$
- B. $[1, 2, 3, 4]$
- C. $[4]$
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $b=a$ gives the same list a second name, so the append is visible through $a$.

The other options: A assumes a copy; C treats append as a replacement; D is wrong. Use $a[:]$ to copy.

</details>

**Q4.2** Which structure best supports repeatedly testing whether a student number is present?

- A. a list
- B. a dictionary or a set
- C. a tuple
- D. a string

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: hashing gives $O(1)$ average membership, so repeated lookups do not slow down.

The other options: A is $O(n)$ per test; C is also linear, only immutable; D is a substring search, even slower.

</details>

**Q4.3** With $\text{values} = [10, 20, 30, 40, 50]$, what is $\text{values[1:3]}$?

- A. $[10, 20, 30]$
- B. $[20, 30]$
- C. $[20, 30, 40]$
- D. $[30]$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: slicing is half-open, so it takes indices $1$ and $2$.

The other options: A starts too early; C includes index $3$; D takes one item.

</details>

**Q4.4** Which really copies the nested list $\text{a} = [[1,2],[3,4]]$?

- A. $b = a$
- B. $b = a[:]$
- C. $b = \text{copy.deepcopy}(a)$
- D. $b = a.append([])$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: deepcopy copies the inner lists too, so changing $b$ cannot touch $a$.

The other options: A is an alias; B is shallow, so $a[0]$ is still shared; D appends to $a$ and returns $\text{None}$.

</details>

**Q4.5** What does $\text{groups.setdefault(60, []).append(1)}$ do when key $60$ is absent?

- A. raises $\text{KeyError}$
- B. creates $\text{groups[60] = []}$ and then appends $1$
- C. does nothing
- D. clears the dictionary

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: setdefault inserts the default when the key is missing and returns it, so the append lands in the new list.

The other options: A is what plain $\text{groups[60]}$ would do; C is the behaviour when the key exists; D is unrelated.

</details>

**Q4.6** Why are two parallel lists fragile?

- A. lists are slow
- B. the correspondence exists only as a promise, so sorting or deleting breaks it
- C. lists cannot hold numbers
- D. lists cannot have equal length

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: nothing in the data enforces that index $i$ belongs to the same record.

The other options: A is irrelevant to correctness; C is false; D is false. Fix: one list of tuples or a dictionary.

</details>

**Q4.7** What type does $\text{def stat(xs): return len(xs), sum(xs)}$ return?

- A. two independent values
- B. one tuple
- C. a list
- D. a dictionary

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: comma-separated return values are packed into a tuple such as $(3, 6)$.

The other options: A is the usual misreading; C needs brackets; D needs braces.

</details>

**Q4.8** Why is returning $\text{fraction}=0$ for an empty interval a problem?

- A. it is not a problem
- B. it says "nothing failed" when the truth is "no data", which can invert the conclusion
- C. it raises $\text{ZeroDivisionError}$
- D. it returns $\text{None}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $0/0$ is undefined; reporting $0$ claims everything was fine when in fact nothing is known.

The other options: A ignores the meaning; C would happen if the division were attempted; D describes the recommended fix of returning $(0, \text{None})$.

</details>

### 4.6 Chapter traps

- Assuming $b = a$ copies: the original data gets modified through the alias.
- Treating a shallow copy as a deep one: nested lists stay shared.
- Building a fresh list for every record: earlier records for that key are overwritten.
- Sorting one of two parallel lists: the pairing is destroyed.
- Expecting dictionary order to be sorted: it is insertion order; sort explicitly.
- Reporting an average when the question asks for a fraction of tests.
- Using a list as a dictionary key: unhashable, $\text{TypeError}$; use a tuple.


### 4.4b How this chapter is examined

Chapter 4 is examined by "what does the program print" on two names for one object. The examiner builds a short list or dictionary, aliases it with a plain assignment, copies it in one of the three ways, mutates one name, and asks for every printed value. The whole mark comes from counting objects first, names second. A second shape asks a definition question: why a list cannot be a dictionary key, why a tuple holding a list can still change, why removing items while iterating skips elements.

## 5 Algorithms and complexity: Big-O, search and sorting

### 5.1 What this chapter is about

One sentence: **running is not enough; you need to know how much slower it gets as the data grows.**

One and the same mathematical function, written two ways: one chokes at $n=40$, the other reaches $n=1000$ in tens of microseconds. The first program is not wrong, it is using the wrong method. This chapter provides the ruler: how the cost grows with problem size.

![Complexity growth: constant, logarithmic, linear, linearithmic, quadratic and exponential curves separate quickly](figures/fig_review_bigO.png)

The horizontal axis is $n$ and the vertical axis is operations on a log scale. Once the exponential curve lifts, nothing saves it.

**Remember this: keep the shape of the growth, drop the constants.**

### 5.2 Mechanisms you must know

**(1) The definition.** Wall-clock time cannot measure an algorithm: it depends on the laptop and on whatever else is running. What matters is how $T(n)$ grows with $n$:

$$T(n) = O(f(n)) \quad \Longleftrightarrow \quad \text{for large } n,\ T(n) \le C\,f(n)$$

Only the **dominant term** survives; constant factors and lower-order terms are dropped:

$$3n^{2} + 100n = O(n^{2}), \qquad \frac{n^{2}}{2} + 5n = O(n^{2})$$

**(2) The common classes.** The right column is the order of operations at $n=10^{6}$:

| Class | Big-O | Typical source | $n=10^{6}$ |
| --- | --- | --- | --- |
| constant | $O(1)$ | dictionary lookup | $1$ |
| logarithmic | $O(\log n)$ | binary search | $20$ |
| linear | $O(n)$ | one pass | $10^{6}$ |
| linearithmic | $O(n\log n)$ | a good sort | $2\times 10^{7}$ |
| quadratic | $O(n^{2})$ | loop inside a loop | $10^{12}$ |
| exponential | $O(2^{n})$ | every subset | $10^{301030}$ |

Learn to reproduce this table. $10^{12}$ operations is slow but feasible; $10^{301030}$ exceeds the number of atoms in the observable universe.

![Cost ladder: at the same $n=10^{6}$ the six complexity classes land in wildly different orders of magnitude](figures/fig_review_cost_ladder.png)

The six bars are operation counts at the same problem size $n=10^{6}$, on a log scale. The three on the left sit almost on the axis; the exponential bar has left the chart. **Same problem size, hundreds of thousands of orders of magnitude apart.** That is why complexity beats memorising seconds: the seconds change with the laptop, the order of magnitude does not.

**(3) How to count.** Count how often the **innermost statement** runs as a function of $n$, then keep the dominant term.

```python
total = 0
for i in range(n):
    total += x[i] * y[i]
```

The multiply runs $n$ times: $O(n)$.

```python
for i in range(n):
    for j in range(n):
        result[i] += A[i][j] * x[j]
```

The multiply runs $n^{2}$ times: $O(n^{2})$.

```python
steps = 0
while n > 1:
    n = n // 2
    steps += 1
```

$n$ halves each round, so the count is $\Theta(\log n)$: exactly $\lfloor\log_{2} n\rfloor$ halvings for a positive integer $n$. For $n=16$ that is $4$ rounds; for $n=1000$ the sequence is $1000\to500\to250\to125\to62\to31\to15\to7\to3\to1$, which is $9$ rounds.

**(4) The exponential recursion trap.** Naive Fibonacci satisfies

$$T(n) = T(n-1) + T(n-2) + O(1) \quad \Longrightarrow \quad T(n) = O(\varphi^{n}),\ \varphi = \frac{1+\sqrt{5}}{2}\approx 1.618$$

Measured: every increase of $5$ in $n$ multiplies the time by about $11$, because $\varphi^{5}\approx 11.09$. The loop version is $O(n)$.

**(5) Search: the structure sets the cost.**

- $x\ \text{in list}$: linear scan, $O(n)$.
- $x\ \text{in dict}$ or $\text{set}$: hash lookup, $O(1)$ average.
- $\text{list.index}(x)$: linear, raises $\text{ValueError}$ when absent.
- A sorted list supports binary search, $O(\log n)$; $\text{bisect.bisect\_left}$ implements it.

$$\text{ten million lookups: list } \approx 0.08\ \text{s}, \qquad \text{set } \approx 2\times 10^{-6}\ \text{s}$$

Four orders of magnitude. Convert once and all later lookups are cheap.

**(6) Why binary search needs sorted data.** Every step discards half the list based on whether the middle element is larger or smaller. Without sorting, "smaller than the middle" says nothing about which half contains the target.

**(7) Sorting: use the built-ins.**

```python
sorted(data)                 # returns a new list
data.sort()                  # in place, returns None
sorted(parts, key=mass, reverse=True)   # custom key, descending
```

- $\text{key=}$ takes the **function itself** (no brackets), or a $\text{lambda}$.
- $\text{reverse=True}$ sorts downwards.
- Tuples compare element by element.

**(8) The cost of three sorts.**

- Bubble sort: about $n^{2}/2$ comparisons, $O(n^{2})$.
- Quicksort: partition then recurse, $O(n\log n)$ on average, $O(n^{2})$ worst case.
- Built-in: $O(n\log n)$, running in compiled code.

| $n$ | bubble | quicksort | built-in |
| --- | --- | --- | --- |
| 1000 | 0.033 s | 0.0008 s | 0.00012 s |
| 2000 | 0.144 s | 0.0017 s | 0.00021 s |
| 4000 | 0.577 s | 0.0035 s | 0.00045 s |
| 8000 | 2.339 s | 0.0098 s | 0.00101 s |

Doubling $n$ quadruples bubble sort but only doubles quicksort.

**(9) Is sorting before searching worth it?** For one lookup, no: $O(n\log n)$ exceeds one $O(n)$ pass. For $m$ lookups, sorting plus $m$ binary searches costs $O(n\log n + m\log n)$ against $O(mn)$, so it wins as soon as $m$ grows.

### 5.3 What the code looks like

**Example 1: counting operations.**

```python
def count_pairs(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
```

The inner loop runs $0+1+\dots+(n-1)=\frac{n(n-1)}{2}$ times, still $O(n^{2})$: halving the inner loop does not change the class.

**Example 2: a set turns lookup into a constant.**

```python
numbers = list(range(10_000_000))
numbers_set = set(numbers)
print(9_999_999 in numbers)       # True, about 0.08 s
print(9_999_999 in numbers_set)   # True, about 0.000002 s
```

**Example 3: sorting by a custom key.**

```python
parts = [("bolt", 0.02), ("panel", 2.1), ("washer", 0.004)]
heaviest = sorted(parts, key=lambda p: p[1], reverse=True)
print(heaviest[0])     # ('panel', 2.1)
```

**Example 4: binary search only works on sorted data.**

```python
import bisect
data = [1, 3, 5, 7, 9]
print(bisect.bisect_left(data, 5))       # 2
print(bisect.bisect_left([9, 1, 5], 5))  # meaningless: not sorted
```

The second call does not raise; it simply returns nonsense. **It does not check that you sorted.**

### 5.4 Worked example E5: search the likeliest patch of ocean first

**What is asked**

After AF447, the search area is divided into cells with a probability (percent, summing to $100$) that the wreckage lies in each. (a) rank by probability descending and give the cumulative probability of the first two cells; (b) write a function returning the shortest prefix whose cumulative probability reaches a target such as $70\%$ or $90\%$; (c) after a cell is searched and nothing is found, the remaining probabilities are rescaled to sum to $100$: must they be re-sorted?

**Why this route**

When every cell costs the same to search, the optimal strategy is to search in descending probability: for a fixed number of cells the covered probability is the sum of those cells. This becomes "sort, then prefix-sum", costing $O(n\log n)$ instead of enumerating orderings. So: fix the order by sorting, then sweep once.

**Step 1: sort**

$$\text{ranked} = \text{sorted}(\text{cells},\ \text{key}=\text{probability},\ \text{reverse}=\text{True})$$

Without $\text{reverse=True}$ the most likely cell is searched last.

**Step 2: accumulate**

$$S_k = \sum_{j=1}^{k} p_j, \qquad k^{\ast} = \min\{\, k : S_k \ge \text{target} \,\}$$

The condition is $\ge$: reaching the target exactly counts.

**Step 3: write the code**

```python
def search_prefix(ranked, target):
    names, total = [], 0
    for name, p in ranked:
        names.append(name)
        total += p
        if total >= target:
            break
    return names
```

**Where the constant comes from**

With the sample data the ranking is $B(45), D(30), C(15), A(10)$, summing to $100$.

- target $70$: $45<70$, adding $30$ gives $75\ge 70$, so the prefix is $[B, D]$: two cells.
- target $90$: $75<90$, adding $15$ gives $90\ge 90$, so the prefix is $[B, D, C]$: three cells.

The numbers $75$ and $90$ are additions, not guesses. Un-sorted, the order $A, C, D, B$ needs $10+15+30=55$ and then $100$ to pass $70$, that is four cells; sorting cuts it to two.

**Sanity check**

Two independent checks. First, a prefix sum cannot exceed $100$: $75$ and $90$ pass. Second, monotonicity: a larger target cannot need fewer cells, and indeed $70\to 90$ takes two to three. On cost: sorting is $O(n\log n)$ and the sweep is $O(n)$, so the total is $O(n\log n)$.

For part (c): the cleared cell gets probability $0$ and every remaining probability is multiplied by the same positive constant $c = 100/55$. **Multiplying by a positive constant preserves order**, so the ranking stands and the cleared cell is simply removed.

$$p_i < p_j \quad \Longleftrightarrow \quad c\,p_i < c\,p_j \quad (c>0)$$

**Answer**

$$\text{sort descending} \Rightarrow \text{accumulate} \Rightarrow \text{stop at the first } S_k \ge \text{target}, \qquad O(n\log n)$$

Target $70$ gives $[B, D]$ at $75\%$; target $90$ gives $[B, D, C]$ at $90\%$; rescaling needs no re-sort.

**Traps**

- Forgetting $\text{reverse=True}$: the least likely cell is searched first.
- Using $>$ instead of $\ge$: one extra cell when the total lands exactly on the target.
- Re-sorting after every update: rescaling does not change order.
- Sorting inside the loop: $O(n^{2}\log n)$.
- Assuming greedy is always optimal: with unequal survey times, ranking by probability per hour can fail.

![Example poster: ranking, prefix selection and complexity](figures/ex_comp5_af447.png)

### 5.5 Multiple-choice questions (8)

**Q5.1** What is the complexity of $T(n) = 3n^{2} + 100n + 7$?

- A. $O(n)$
- B. $O(n^{2})$
- C. $O(n^{2} + n)$
- D. $O(3n^{2})$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: for large $n$ the square term dominates; the constant $3$ and the linear term are dropped.

The other options: A drops the square; C is not a canonical form; D keeps a constant factor.

</details>

**Q5.2** What is the complexity here?

```python
total = 0
for i in range(n):
    for j in range(n):
        total += A[i][j] * x[j]
```

- A. $O(n)$
- B. $O(n\log n)$
- C. $O(n^{2})$
- D. $O(2^{n})$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: the outer loop runs $n$ times and the inner loop $n$ times each, so the body runs $n^{2}$ times.

The other options: A sees only one loop; B has no halving; D has no subset enumeration.

</details>

**Q5.3** What is the complexity of $\text{while n > 1: n = n // 2}$?

- A. $O(1)$
- B. $O(\log n)$
- C. $O(n)$
- D. $O(n\log n)$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $n$ halves each round, so about $\log_{2} n$ rounds are needed.

The other options: A the count depends on $n$; C that is a loop decrementing by one; D there is no second loop.

</details>

**Q5.4** To test membership repeatedly among $10^{7}$ integers, what is best?

- A. scan the list with $\text{in}$ each time
- B. convert once to a set, then test with $\text{in}$
- C. sort it and scan from the start each time
- D. store it in a tuple and test with $\text{in}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: hashing gives $O(1)$ per test, and one $O(n)$ conversion pays for all later lookups.

The other options: A and D are linear scans; C still scans, ignoring the order (binary search would be needed).

</details>

**Q5.5** Binary search requires that the data is

- A. integers
- B. sorted
- C. free of duplicates
- D. stored in a list

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: each step uses the comparison with the middle element to discard half, which is only valid when the data is ordered.

The other options: A floats work too; C duplicates are allowed; D tuples and arrays work too.

</details>

**Q5.6** What is the difference between $\text{sorted(data)}$ and $\text{data.sort()}$?

- A. none
- B. the first returns a new list; the second sorts in place and returns $\text{None}$
- C. the first only works on numbers
- D. the second returns a sorted copy

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: sorted is a built-in function returning a new list; sort is a method mutating the list and returning $\text{None}$.

The other options: A ignores the return value, and $x = \text{data.sort()}$ gives $\text{None}$; C sorted handles strings and tuples; D reverses them.

</details>

**Q5.7** The complexity of naive recursive Fibonacci is about

- A. $O(n)$
- B. $O(n\log n)$
- C. $O(\varphi^{n})$ with $\varphi\approx 1.618$
- D. $O(n^{2})$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: each call splits into two, so the work grows exponentially at the golden ratio; measured, every extra $5$ in $n$ multiplies the time by $11$.

The other options: A is the loop version; B is unrelated to sorting; D is far slower than exponential growth would allow at $n=100$.

</details>

**Q5.8** For a single lookup, "sort then binary search" compared with one linear scan is

- A. always faster
- B. usually slower, because sorting costs $O(n\log n)$, more than one $O(n)$ pass
- C. the same
- D. incomparable

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: sorting dominates; only many lookups amortise it.

The other options: A holds only for many lookups; C ignores the sorting cost; D is false, complexities compare directly.

</details>

### 5.6 Chapter traps

- Keeping constants and lower-order terms: write $O(n^{2})$, not $O(3n^{2}+100n)$.
- Believing a shorter inner loop changes the class: $n(n-1)/2$ is still $O(n^{2})$.
- Binary searching unsorted data: no error, no meaning.
- Forgetting $\text{reverse=True}$ when the largest should come first.
- Sorting inside a loop: $O(n\log n)$ becomes $O(n^{2}\log n)$.
- Repeated $\text{in}$ tests on a list: convert to a set once.
- Writing $x = \text{data.sort()}$: $\text{None}$ is not a list.
- Assuming greedy is always optimal: unequal costs break it.


### 5.4b How this chapter is examined

Chapter 5 is examined by attaching a complexity to a snippet, and the snippet is always a loop nest. Count the innermost statement, not the number of loops: two loops over the same list give $n^{2}$, two loops over the same list where the inner one starts at the outer index give about $n^{2}/2$, which is still $O(n^{2})$. A second shape asks for the precondition rather than the complexity: binary search needs a sorted list, so an unsorted list invalidates both the answer and the method. Keep the sentence "count the innermost statement" ready, because it converts a guess into work you can show.

## Tracing drills

Predict-the-output questions are decided on paper, never by running the code. The whole mark turns on one habit: write the value of every changing variable after every pass, before you commit to an answer. The five drills below are the shapes that appear most often, and each one teaches a rule you can carry into the hall.

### D1 A loop with an accumulator and a skip

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i * i
print(total)
```

List one line per pass, including the passes that `continue` throws away. A skipped pass still consumed one value of $i$, so it belongs in the trace; that is exactly where marks are lost.

$$\text{pass }1:\quad i=1,\quad i\bmod 2=1,\quad \text{total}=0+1=1$$

$$\text{pass }2:\quad i=2,\quad i\bmod 2=0,\quad \text{continue},\quad \text{total}=1$$

$$\text{pass }3:\quad i=3,\quad \text{total}=1+9=10$$

$$\text{pass }4:\quad i=4,\quad \text{continue},\quad \text{total}=10$$

$$\text{pass }5:\quad i=5,\quad \text{total}=10+25=35$$

The answer is $\text{total}=35$, and two independent checks support it: the odd squares below six sum to $1+9+25=35$, and the addition ran three times, not five, because two passes were skipped.

### D2 Alias, slice copy and one list

```python
a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(5)
print(a, b, c)
```

The question is not what `append` does; it is how many list objects exist. There are two: the one that `a` and `b` both name, and the fresh one that `a[:]` built for `c`. Appending through `b` mutates the shared object, so `a` moves with it; appending through `c` touches the separate object, so `a` stops changing.

$$b=a:\quad \text{one object},\quad a=b=[1,2,3]$$

$$c=a[:]:\quad \text{second object},\quad c=[1,2,3]$$

$$b.\text{append}(4):\quad a=b=[1,2,3,4],\quad c=[1,2,3]$$

$$c.\text{append}(5):\quad a=b=[1,2,3,4],\quad c=[1,2,3,5]$$

The printed line is $[1,2,3,4]\ [1,2,3,4]\ [1,2,3,5]$. The check: replace `b = a` with `b = a[:]` and redo it; if the printed `a` then stops moving, you had the alias step right.

### D3 A while loop that stops early

```python
n = 10
while n > 0:
    n -= 3
    if n == 1:
        break
print(n)
```

Write down the value of $n$ after the subtraction, not before it: the test `n == 1` runs on the new value, and `break` leaves the loop at once, so what gets printed is the value that triggered the break.

$$\text{test }1:\quad n=10-3=7,\quad n>0\ \text{true},\quad \text{continue}$$

$$\text{test }2:\quad n=7-3=4,\quad \text{continue}$$

$$\text{test }3:\quad n=4-3=1,\quad n==1,\quad \text{break}$$

$$\text{printed}:\quad n=1$$

Without the `break` the sequence would be $10\to7\to4\to1\to-2$ and the printed value would be $-2$, so the `break` saves exactly one pass.

### D4 One dictionary, two names

```python
d = {"x": 1}
e = d
e["y"] = 2
print(d, len(d))
```

Assigning a dictionary never copies it. `e = d` gives one object a second name, so the new key shows through both names and the length is two.

$$d=\{\text{x}:1\}\Rightarrow e=d\ \text{names the same object}$$

$$e[\text{y}]=2\Rightarrow d=e=\{\text{x}:1,\text{y}:2\},\quad \text{len}=2$$

Two independent dictionaries would need `e = dict(d)` or `e = d.copy()`; neither appears, so the answer stays "one object, two names".

### D5 What may change inside a tuple or a string

```python
t = (1, [2])
t[1].append(3)
print(t)

s = "ab"
s[0] = "c"
```

A tuple is immutable in the sense that its slots cannot be rebound; it does not freeze the objects those slots point at. Slot 1 still names the same list, so calling `append` on that list is legal and changes what the tuple shows. A string is different: it has no mutable slots at all, so character assignment raises `TypeError` and the string stays as it was.

$$t=(1,[2])\Rightarrow t[1].\text{append}(3)\Rightarrow t=(1,[2,3])$$

$$t[1]=[9]\Rightarrow \text{TypeError},\quad \text{tuple slot cannot be rebound}$$

$$s=\text{ab};\ s[0]=\text{c}\Rightarrow \text{TypeError},\quad s\ \text{stays ab}$$

Two questions asked in the margin cover almost every predict-the-output item: am I rebinding a slot or mutating an object, and is this type mutable at all. List is mutable and rebindable, tuple is not rebindable, string is neither, dictionary is both.

---

## Simulated paper A

This is a fifty-mark paper in the shape of the progress test: four questions, no starred parts, no calculator beyond arithmetic. Time yourself, write only on paper, and mark yourself against the eight-beat solutions that follow each question. Every question here is written to the lecture scope, so none of it is a past-paper question.

### A1 Types, floor division and float comparison

```python
x = 3500
y = -3500
print(x // 400, y // 400)
print(x % 400, y % 400)
print(3 * 0.1 == 0.3)
```

**What is asked** — Five printed values: two results of floor division, two remainders, and one boolean. Full marks need the values plus one sentence on why the boolean is the value it is. No explanation of the division direction, no full marks.

**Why this route** — Every symbol here is decided by Python's definitions, not by the numbers: `//` is defined as the floor of the true quotient, and `%` is defined so that the identity below holds for any sign combination, so the route is to apply the definitions in order rather than to divide and round by intuition.

$$\frac{3500}{400}=8.75 \;\Longrightarrow\; \left\lfloor 8.75\right\rfloor = 8$$

$$\frac{-3500}{400}=-8.75 \;\Longrightarrow\; \left\lfloor -8.75\right\rfloor = -9$$

The first line gives $8$, and the second gives $-9$: floor always moves toward minus infinity, which for a negative number is away from zero.

**Get the remainder from the identity**

$$a = b\left\lfloor \frac{a}{b}\right\rfloor + (a \bmod b)$$

$$3500 = 400\times 8 + 300 \;\Longrightarrow\; 3500 \bmod 400 = 300$$

$$-3500 = 400\times(-9) + 100 \;\Longrightarrow\; -3500 \bmod 400 = 100$$

Substituting the floors from step 1 leaves $300$ and $100$, and both remainders come out with the sign of the divisor, which is the property that makes the identity work for negatives.

**Decide the float comparison**

$$3\times 0.1 = 0.30000000000000004 \;\ne\; 0.3$$

$$0.1 \approx 0.1000000000000000055511151231257827$$

The product is one unit in the last place away from $0.3$, so `==` returns `False`; the cause is that $0.1$ is stored as the nearest binary fraction, and the doubling error surfaces at the sixteenth significant digit.

**Where the constant comes from** — $8$ and $-9$ come from the two floors, $300$ and $100$ from the identity, so nothing here is a guess. The one subtle constant is the extra digit in $0.30000000000000004$: it is not a typo, it is the shortest decimal that round-trips to the stored double.

**Sanity check** — Substituting back gives the two identities $3500=3200+300$ and $-3500=-3600+100$, both true; and a second check on the boolean is that $0.1+0.2$ shows the same one-digit excess, so the pattern is consistent rather than a one-off.

**Answer**

$$8,\quad -9,\quad 300,\quad 100,\quad \text{False}$$

**Trap** — Truncating instead of flooring gives the pair $(-8,\,-300)$, which still satisfies $a=bq+r$ but breaks Python's rule that the remainder takes the sign of the divisor; pairing $q=-8$ with Python's own remainder $+100$ gives $400\times(-8)+100=-3100\ne-3500$, which is how the identity actually falls apart. Writing "floating point is imprecise" without the mantissa explanation loses the explanation mark.

![Worked example poster: simulated paper A1, floor division and one float test](figures/ex_sim_a1.png)

### A2 A mutable default argument and a fixed version

```python
def add_item(item, basket=[]):
    basket.append(item)
    return len(basket)

def add_item2(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("a"), add_item("b"), add_item("c"))
print(add_item2("a"), add_item2("b"))
```

**What is asked** — Two printed lines, plus the reason the first function behaves differently on its second and third call, plus what the second function prints.

**Why this route** — The two functions differ in exactly one place, the default value, so the route is to ask when each default is evaluated. Default values are evaluated once, when the `def` statement runs, not once per call; that single fact decides both lines.

**Count the objects**

$$\text{call }1: \text{basket}\to L_1,\quad \text{call }2: \text{basket}\to L_1,\quad \text{call }3: \text{basket}\to L_1$$

The default list $L_1$ is created once at definition, so all three calls append to the same object, and the returned lengths are $1,2,3$.

**See what an explicit argument does**

$$\text{add\_item}(x, [\,])\Rightarrow \text{basket}\to L_{\text{new}}$$

Passing a list yourself replaces the default, so the guard only matters when the argument is omitted; the default object survives between calls in either case.

**Rebuild from None**

$$\text{basket}=\text{None}\Rightarrow \text{basket}\to L_2 \text{ (fresh each call)}$$

In the second function the default is `None`, which is immutable, and a fresh list is built inside the body on every call, so the two calls give $['a']$ and $['b']$.

**Where the constant comes from** — The numbers $1,2,3$ are the lengths after each append, so they come from counting appends to one object; the second line's two single-element lists come from counting objects, one per call.

**Sanity check** — Run the first function twice more in your head: the lengths keep climbing, which is the signature of a persistent object; if the printed lengths restarted at $1$, the default would have been rebuilt and the answer would be wrong.

**Answer**

$$1\ 2\ 3 \qquad\text{then}\qquad [\text{a}]\ [\text{b}]$$

**Trap** — Saying "the default is re-created each call" gives $1\ 1\ 1$ and loses the whole question; the fix is not to forbid defaults but to use an immutable sentinel such as `None` and build inside the body.

![Worked example poster: simulated paper A2, a mutable default argument](figures/ex_sim_a2.png)

### A3 A loop that skips and stops

```python
total = 0
for n in range(1, 8):
    if n % 3 == 0:
        continue
    if total + n > 10:
        break
    total += n
print(total, n)
```

**What is asked** — The two values printed, and which pass ended the loop.

**Why this route** — There are two exit conditions on the same pass, `continue` before the accumulator and `break` before it, so the only reliable route is a pass-by-pass table with the order of the two tests preserved.

**Tabulate every pass**

$$n=1:\ total=0+1=1 \qquad n=2:\ total=1+2=3$$

$$n=3:\ 3\bmod 3=0 \Rightarrow \text{continue} \qquad n=4:\ total=3+4=7$$

$$n=5:\ 7+5=12>10 \Rightarrow \text{break}$$

The first two passes add, the third is skipped before it can add, the fourth adds, and the fifth trips the guard and leaves.

**Confirm what the break carries out**

$$\text{printed}:\quad \text{total}=7,\quad n=5$$

`break` leaves the loop without executing the body's remaining statements, so $n$ keeps the value that triggered it, $5$, and `total` keeps the last value it had, $7$.

**Compute a control case**

$$\text{without the break}:\ total=1+2+4+5+7=19$$

Removing the guard lets every non-multiple-of-three pass add, and the sum would be $19$, so the guard changes the answer rather than merely ending it early.

**Where the constant comes from** — $12$ is the first running total that exceeds $10$, which is why the loop stops at $n=5$ and not at $n=4$; the threshold $10$ and the addend $5$ together decide that pass.

**Sanity check** — Two checks: the three added values are $1,2,4$, and $1+2+4=7$ matches the printed total; and the loop index reached $5$ while `range` would have gone to $7$, so the `break` is confirmed active.

**Answer**

$$\text{total}=7,\qquad n=5$$

**Trap** — Adding on the `continue` pass gives $10$ and then a different $n$; and forgetting that `break` skips the rest of the body gives $n=4$ from a lazily read table.

![Worked example poster: simulated paper A3, a loop that skips and stops](figures/ex_sim_a3.png)

### A4 One grid, three names

```python
grid = [[1, 2], [3, 4]]
cp = grid[:]
deep = [row[:] for row in grid]
cp[0].append(9)
deep[1].append(8)
print(grid)
print(cp)
print(deep)
```

**What is asked** — Three printed lists, and the reason `cp` and `grid` change together while `deep` does not.

**Why this route** — Three names, three different amounts of copying: plain assignment would share everything, a slice copies one level, and a comprehension over slices copies two. The route is to draw the object graph, not to remember the words "shallow" and "deep".

**Draw the outer level**

$$\text{cp} = \text{grid}[:] \Rightarrow \text{new outer list},\ \text{same inner rows}$$

The slice builds a new outer list whose three slots point at the same inner lists, so the rows are shared even though the container is not.

**Draw the inner level**

$$\text{deep} = [\,row[:]\ \text{for}\ row\ \text{in}\ \text{grid}\,] \Rightarrow \text{new rows too}$$

The comprehension applies the slice to each row, so `deep` has new inner lists and shares nothing mutable with `grid`.

**Append one at a time**

$$\text{cp}[0].\text{append}(9) \Rightarrow \text{grid} = [[1,2,9],[3,4]]$$

$$\text{deep}[1].\text{append}(8) \Rightarrow \text{deep} = [[1,2],[3,4,8]]$$

The first append goes through a shared row, so both `grid` and `cp` show it; the second goes into a private row, so only `deep` shows it.

**Where the constant comes from** — The $9$ lands in row $0$ because that is the row `cp` shares; the $8$ lands in row $1$ because `deep` owns its rows; both indices come straight from the code, not from counting.

**Sanity check** — Count mutable objects before and after: two original rows plus two copies is four, and the printed output must show exactly one row changed in two lists and one row changed in one list, which it does.

**Answer**

$$\text{grid} = [[1,2,9],[3,4]],\quad \text{cp} = [[1,2,9],[3,4]],\quad \text{deep} = [[1,2],[3,4,8]]$$

**Trap** — Trusting the slice as a full copy gives `deep` sharing rows and a wrong third line; and `copy.deepcopy` is not needed here, so answering with library calls instead of the object graph loses the explanation mark.

![Worked example poster: simulated paper A4, one grid and three names](figures/ex_sim_a4.png)

---

## 6 Twelve mixed questions

**Q6.1** What does this print?

```python
def f(xs):
    total = 0
    for x in xs:
        total += x
    return total

print(f([0.1, 0.2]) == 0.3)
```

- A. $\text{True}$
- B. $\text{False}$
- C. $\text{None}$
- D. an error

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $0.1$ and $0.2$ already carry rounding when stored, so their sum differs from the stored $0.3$ (chapter 1).

The other options: A is the mathematical intuition; C the function returns a bool; D the syntax and types are fine. Use $\text{math.isclose}$.

</details>

**Q6.2** Where does this code go wrong?

```python
def add_item(x, bucket=[]):
    bucket.append(x)
    return bucket

print(add_item(1))
print(add_item(2))
```

- A. the first call fails
- B. the second prints $[1, 2]$, because the default list is created once
- C. the second prints $[2]$
- D. append cannot be used with a default argument

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: the default is evaluated once at definition time, so both calls share one list (chapter 2).

The other options: A it does not fail, and the silence is the danger; C is intuitive but wrong; D is false. Default to $\text{None}$ and build the list inside.

</details>

**Q6.3** To count "how many tests at each temperature", the best structure is

- A. two lists of equal length
- B. a dictionary mapping temperature to a count or a list
- C. a tuple
- D. a string

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: a key-to-value map expresses "temperature leads to records" directly, with $O(1)$ lookup and no fragility when sorting (chapter 4).

The other options: A relies on index alignment; C is immutable and cannot take new keys; D means writing your own parser.

</details>

**Q6.4** What is the time complexity?

```python
count = 0
for i in range(n):
    j = 0
    while j < n:
        count += 1
        j += 2
```

- A. $O(\log n)$
- B. $O(n)$
- C. $O(n^{2})$
- D. $O(n\log n)$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: the outer loop runs $n$ times; the inner loop advances by $2$ and so runs $n/2$ times, which is still $O(n)$; the product is $O(n^{2})$ (chapter 5).

The other options: A the inner loop does not halve; B only one loop is counted; D there is no logarithmic structure, and stepping by two is linear.

</details>

**Q6.5** What does this print?

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(len(a), len(b))
```

- A. $4\ 4$
- B. $3\ 4$
- C. $3\ 3$
- D. $4\ 3$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $a[:]$ is a shallow copy, so appending to $b$ leaves $a$ alone (chapter 4).

The other options: A is what $b = a$ would give; C ignores the append; D reverses the order.

</details>

**Q6.6** Does this loop terminate?

```python
n = 10
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
```

- A. no, $n$ keeps growing
- B. yes: $10\to5\to16\to8\to4\to2\to1$, six passes through the body
- C. no, because there is no break
- D. it raises $\text{ZeroDivisionError}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $10$ halves to $5$, the odd branch maps $5$ to $16$, then halving reaches $1$; that is six passes through the body, and the seventh check sees $n=1$ and exits (chapter 3).

The other options: A even steps divide immediately; C a break is not needed when the condition eventually turns false; D there is no division by zero.

</details>

**Q6.7** To group $10^{6}$ records by temperature and then print in temperature order, you should

- A. group in a dictionary and print $\text{sorted(groups.items())}$
- B. keep a list in arrival order
- C. group in a set
- D. group in a tuple

<details><summary>Answer and explanation</summary>

**Answer: A**

Why: the dictionary does the grouping with $O(1)$ lookups, and sorted fixes the order: two jobs, two tools (chapters 4 and 5).

The other options: B is insertion order, not temperature order; C loses the key-to-value link; D is immutable.

</details>

**Q6.8** Which test is most likely to misbehave?

- A. $\text{if } x \ne 0:\ y = 10 / x$
- B. $\text{if } x == 0.1 + 0.2:\ \text{print("hit")}$
- C. $\text{if } 0 \le x < 10:\ \text{print("in range")}$
- D. $\text{if isinstance}(x, \text{int}):\ \text{print("int")}$

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: comparing floats with $==$ almost never succeeds; use $\text{math.isclose}(x, 0.3)$ (chapters 1 and 3).

The other options: A guards before dividing; C is a legal chained comparison; D is a fine type test.

</details>

**Q6.9** What does this print?

```python
def g(n):
    if n <= 1:
        return 1
    return n * g(n - 1)

print(g(4))
```

- A. $4$
- B. $10$
- C. $24$
- D. infinite recursion

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: this is the factorial, $4\times 3\times 2\times 1 = 24$, and the base case $n\le 1$ stops the recursion (chapters 2 and 3).

The other options: A only one level; B that is a sum; D the base case prevents it.

</details>

**Q6.10** A counter $c_i$ increments only when the height is below the gate and the sensor fired, and resets otherwise. Which test is right?

- A. $\text{if } \text{touch}[i]:\ c += 1$
- B. $\text{if } h[i] < h_{\text{enable}} \text{ and } \text{touch}[i]:\ c += 1\ \text{else}:\ c = 0$
- C. $\text{if } h[i] < h_{\text{enable}}:\ c += 1$
- D. $c = c + 1$ every cycle

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: it expresses both the gate and the count, and resets in every other case, which is what "consecutive" requires (chapter 3, E3).

The other options: A drops the gate; C drops the trigger; D ignores the data entirely.

</details>

**Q6.11** "Sort then binary search" beats one linear scan when

- A. always
- B. never
- C. $m$ is large enough that $O(n\log n + m\log n) < O(mn)$
- D. it does not depend on $m$

<details><summary>Answer and explanation</summary>

**Answer: C**

Why: sorting is a one-off investment and each binary search is cheap, so more lookups amortise it (chapter 5).

The other options: A fails for a single lookup; B ignores repeated lookups; D is false.

</details>

**Q6.12** What is wrong here?

```python
def mean(readings):
    total = 0
    for r in readings:
        total = total + r
    print(total / len(readings))

x = mean([1, 2, 3]) * 2
```

- A. the loop is wrong
- B. $\text{mean}$ prints but never returns, so $x$ is $\text{None}$ and $\text{None}\times 2$ raises $\text{TypeError}$
- C. len cannot be used on a list
- D. nothing

<details><summary>Answer and explanation</summary>

**Answer: B**

Why: $2.0$ appears on screen, but the call returns $\text{None}$ and the multiplication fails (chapter 2).

The other options: A the loop is correct; C len works on lists; D it crashes. Replace print with return.

</details>

## Where marks are lost

Every line below is a real way this paper takes marks off, written as "if you write this, you lose that". Read it the night before and again in the corridor: most of the loss is not ignorance, it is a habit that looked harmless while revising.

1. Writing "floating point is inaccurate" without naming the cause → lose the explanation mark, because the binary mantissa cannot store $0.1$ exactly and the sum lands on the nearest representable value.
2. Calling $2^{15}$ the largest signed 16-bit value → lose the arithmetic, the range is $-2^{15}$ to $2^{15}-1$.
3. Answering `7 // 2` and `-7 // 2` with the same sign rule → lose both, floor division rounds toward minus infinity, not toward zero.
4. Treating `/` as integer division when both operands are ints → lose the type mark, in Python 3 a single slash always returns a float.
5. Explaining `print` as if it returned its argument → lose the return-value mark, it returns `None`.
6. Claiming a function can rebind a global by plain assignment → lose the scope mark, assignment inside a function always creates a local name unless `global` is declared.
7. Saying a mutable default argument is "created fresh each call" → lose the mechanism mark, the default object is built once at definition time.
8. Saying a list passed into a function is copied → lose the aliasing mark, the function receives a reference to the same object.
9. Writing the loose condition first in an `if/elif` chain → lose the branch that never runs, and the marker sees the dead branch immediately.
10. Counting `range(a, b)` as $b-a+1$ values → lose the loop count, the stop value is exclusive.
11. Treating `continue` as `break` in a trace → lose the whole output, a skipped pass still consumes one value.
12. Claiming both sides of `and` always run → lose the short-circuit mark, the moment the left side is false the right side never evaluates.
13. Saying `b = a` copies the list → lose every later output, both names point at one object.
14. Saying a tuple is completely immutable, including what it holds → lose the counter-example, the slots are fixed but a contained list can still be mutated.
15. Using a list as a dictionary key → lose the statement, keys must be hashable and a list is not.
16. Reporting the complexity of two nested loops over the same list as $n+n$ → lose it twice, the inner statement runs $n$ times for each of $n$ outer passes.
17. Binary-searching an unsorted list and reporting $O(\log n)$ → lose the premise and the result, halving only works after sorting.
18. Confusing "stable sort" with "fast sort" → lose the definition mark, stable means equal keys keep their original relative order.
19. Claiming $n\log n$ is always faster than $n^{2}$ → lose the nuance, below the crossover the constants decide.
20. Leaving a complexity answer as a bare $O(\cdot)$ with no counted line → lose the method, the marker wants the innermost statement and how many times it runs.
21. Writing $8$ for $16/2$ → lose the output mark, because a single slash returns $8.0$.
22. Fixing a comparison with zero by setting $\text{rel\_tol}$ → lose the fix, only an absolute tolerance can pass near zero.
23. Defining machine epsilon as the smallest positive float → lose the definition, it is the gap between $1.0$ and the next float, $2^{-52}$.
24. Reaching for $\text{global}$ when the question wants a result → lose the reasoning, the expected fix is to return the value and catch it outside.
25. Shadowing a builtin such as $\text{sum}$ with a variable → lose the find-the-bug mark, because the builtin is no longer callable.

## The last thirty minutes

Do these seven things in this order and stop when the time is gone. Nothing here needs new thinking, which is the point: the last half hour is for converting things you already know into marks.

1. Minutes 30 to 22: re-read the question-type map and say the first stroke for each row out loud.
2. Minutes 22 to 15: redo the trace drills on blank paper, all five, without looking at the answers.
3. Minutes 15 to 10: write down the four numeric facts you are least sure of ($2^{15}-1$, floor division on negatives, $\log n$ halving, $n\log n$ crossover).
4. Minutes 10 to 6: check that your calculator is in the right mode and that you know how to write a tolerance comparison.
5. Minutes 6 to 3: skim the chapter traps of Ch1 and Ch3, the two chapters where wording decides the answer.
6. Minutes 3 to 1: pack pens, water, student card; close every note.
7. Last minute: breathe, and decide that any question you cannot start gets its "first stroke" line written before you leave it.

---

## 7 One-page revision sheet

### 7.1 Formula card

$$\varepsilon_{\text{mach}} = 2^{-52} \approx 2.22\times 10^{-16}, \qquad v = (-1)^{s}(1.f)_2\,2^{e-1023}$$

$$2^{53} = 9\,007\,199\,254\,740\,992, \qquad \text{float}(2^{53})+1 = \text{float}(2^{53})$$

$$-2^{15} \le n_{\text{int16}} \le 2^{15}-1, \qquad \text{int}(10v)\ \text{scales first, truncates second}$$

$$\theta = \frac{\sum \text{faulty}}{\sum \text{tests}}\ \text{(pooled, not averaged)}, \qquad \varphi = \frac{1+\sqrt{5}}{2}\approx 1.618$$

### 7.2 Complexity table

| Big-O | Name | Typical source | operations at $n=10^{6}$ |
| --- | --- | --- | --- |
| $O(1)$ | constant | dictionary or set lookup | $1$ |
| $O(\log n)$ | logarithmic | binary search, halving loop | $20$ |
| $O(n)$ | linear | one pass | $10^{6}$ |
| $O(n\log n)$ | linearithmic | a good sort | $2\times 10^{7}$ |
| $O(n^{2})$ | quadratic | loop inside a loop | $10^{12}$ |
| $O(2^{n})$ | exponential | every subset, naive recursion | $10^{301030}$ |

### 7.3 Trap list, to read five minutes before the test

- $0.1+0.2 \ne 0.3$; compare floats with $\text{math.isclose}$, and use $\text{abs\_tol}$ near zero.
- The gap doubles at every power of two; past $2^{53}$ adding $1$ changes nothing.
- Fixed-width integers wrap silently; $\text{int}()$ truncates; scale before truncating.
- A function that only prints returns $\text{None}$.
- A default of $\text{acc=[]}$ is created once and shared by every call.
- $\text{elif}$ order is the logic; test the strictest threshold first.
- A $\text{while}$ loop must make progress; a $\text{continue}$ over the update hangs.
- $\text{range}(a, b)$ is half-open; $\text{range}(10, 0)$ is empty.
- $x\ \text{in list}$ is $O(n)$; $x\ \text{in dict}$ or set is $O(1)$ average.
- $\text{data.sort}()$ returns $\text{None}$; $\text{sorted(data)}$ returns a new list.
- Binary search needs sorted data, otherwise the answer is meaningless and no error is raised.
- Assignment does not copy; $\text{copy()}$ is shallow; nested structures need $\text{deepcopy}$.

## 8 Answer key

| Chapter | Questions | Answers |
| --- | --- | --- |
| Ch1 | Q1.1 – Q1.8 | B B B C A C B B |
| Ch2 | Q2.1 – Q2.8 | B B B B C C C B |
| Ch3 | Q3.1 – Q3.8 | A A C C B B B B |
| Ch4 | Q4.1 – Q4.8 | B B B C B B B B |
| Ch5 | Q5.1 – Q5.8 | B C B B B B C B |
| mixed | Q6.1 – Q6.12 | B B B C B B A B C B C B |

## 9 Coverage table

| Notes chapter | Section | Covered in |
| --- | --- | --- |
| Ch1 Types and Floating Point | 1.1–1.2 types, int and float | §1.2(1)(2) |
| | 1.3 IEEE 754 double format | §1.2(3) |
| | 1.4 the floating-point number line | §1.2(6)(7) |
| | 1.5 absorption, cancellation, special values | §1.2(9)(10) |
| | 1.6 Ariane 5 | §1.4 E1 |
| Ch2 Variables and Functions | 2.1–2.3 variables and anatomy of a function | §2.2(1)–(4) |
| | 2.4 return vs print | §2.2(5) |
| | 2.5–2.7 arguments, scope, nested calls | §2.2(6)–(9) |
| | 2.8 Mars Climate Orbiter | §2.4 E2 |
| Ch3 Control Flow | 3.1 booleans and logic | §3.2(1)–(4) |
| | 3.2 if/elif/else | §3.2(5) |
| | 3.3–3.4 while and for | §3.2(6)(7) |
| | 3.5 break and continue | §3.2(9) |
| | 3.6 Mars Polar Lander | §3.4 E3 |
| Ch4 Data Structures | 4.1–4.3 lists, dictionaries, tuples | §4.2(1)–(3) |
| | 4.4 aliasing | §4.2(4) |
| | 4.5 choosing the right structure | §4.2(5)(6) |
| | 4.6 Challenger | §4.4 E4 |
| Ch5 Algorithms and Complexity | 5.1 Big-O notation | §5.2(1)–(4) |
| | 5.2 search | §5.2(5)(6) |
| | 5.3 sorting | §5.2(7)(8)(9) |
| | 5.4 Air France 447 | §5.4 E5 |

## 10 Glossary

| Term | One-line meaning |
| --- | --- |
| floating point | a real number stored as sign, exponent and fraction, with relative precision |
| machine epsilon | the gap between $1.0$ and the next float, $2^{-52}$ |
| rounding | moving a computed value to the nearest representable float |
| absorption | a small addend disappearing when added to a much larger number |
| catastrophic cancellation | subtracting nearly equal numbers and losing the leading digits |
| silent overflow | a fixed-width integer wrapping round to a wrong value without an error |
| fixed point | an integer encoding with the decimal point fixed in advance |
| in-place | mutating the original object, as $\text{list.sort}()$ does |
| shallow copy | copying only the outer container, still sharing the inner objects |
| aliasing | two names referring to one object |
| scope | the region in which a name is visible |
| docstring | the triple-quoted description under a function definition |
| short-circuit evaluation | skipping the second operand once the outcome is known |
| half-open interval | an interval that includes the lower bound and excludes the upper |
| hash | a computed location that gives average $O(1)$ lookup |
| complexity | how cost grows with problem size |
| linearithmic | $O(n\log n)$, the typical cost of a good sort |
| common-mode failure | duplicates sharing one assumption, so both fail together |

## 11 Self-check

- Coverage: every section of notes Ch1–Ch5, item by item in the §9 coverage table (20 rows).
- Worked examples: 9 (E1–E5 and the four questions of simulated paper A), all written to the eight-part template, each with its own poster.
- Questions: $8\times 5 + 12 + 4 = 56$: forty multiple-choice, twelve mixed and four simulated, each with an answer and the reasoning that reaches it.
- Figures: 7 concept figures plus 9 posters, 16 references in total, no duplicates and none missing, all pointing at existing files under `figures/`.
- Formulas: inline $\ldots$ and display $$\ldots$$ throughout; no align environment, no boxed, no newcommand.
- Numbers rechecked: $2^{-52}\approx 2.22\times10^{-16}$, $2^{53}=9\,007\,199\,254\,740\,992$, $32767/10=3276.7$, $3/5=0.6$, $\varphi^{5}\approx 11.09$, all restated exactly as the notes give them.
