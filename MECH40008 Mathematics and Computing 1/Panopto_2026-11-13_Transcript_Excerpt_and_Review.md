# Panopto Transcript Excerpt and Review

## Source

- Course: MECH40008 Mathematics and Computing 1
- Recording: ME MECH40008 - Mathematics and Computing 1 CAGB-02-200 2026-11-13
- Duration: 59:57
- URL: https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f129a324-275f-48af-a4c3-b4b40179ea01
- Source type: Panopto's automatically generated English captions and the course handout notes

## Main topics verified

### 1. Partial derivatives and their geometric meaning (0:36-3:43)

Holding the other variable fixed extends ordinary differentiation to functions of two variables. To take the partial derivative with respect to $x$, hold $y$ fixed. To take it with respect to $y$, hold $x$ fixed. A vertical plane at the fixed coordinate cuts the surface along a curve. The partial derivative is the slope of the tangent to that curve at the specified point.

### 2. Higher-order and mixed partial derivatives (4:12-7:48)

The recording first calculates the pure second-order partial derivatives, then discusses mixed partials. The mixed partials of the polynomial and exponential functions in the handout are continuous, so the following equality applies.

$$f_{xy}=f_{yx}.$$

The precise condition concerns the continuity of the mixed second partial derivatives in the relevant neighbourhood. Continuity of the function alone is insufficient.

### 3. Partial differentiation practice with an exponential function (8:17-9:45)

The captions give $e^{x^{2}y}$ as the example and emphasise the chain rule, the product rule and holding the other variable fixed. See E5 in the main notes for the results. Recalculate the formulas from the handout to verify any symbols identified by automatic speech recognition (ASR).

### 4. Small changes and the total differential (10:41-13:27)

The linear part of the total differential is

$$dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy.$$

For a finite change, the usual approximation is

$$\Delta z\approx dz,$$

Keep the approximation sign. The captions may confuse $d$, $\Delta$ and $\delta$, so check them against the board or the handout.

### 5. Propagating errors in the moment of inertia of a disc (13:50 to about 16:18)

The handout uses the model

$$I=\frac{1}{2}Ma^{2}.$$

If the board confirms a relative change of $+0.1\%$ in $M$ and $-0.2\%$ in $a$, then

$$\frac{\Delta I}{I}\approx\frac{\Delta M}{M}+2\frac{\Delta a}{a}=0.1\%-0.4\%=-0.3\%.$$

The $2$ comes from squaring the radius $a$. A question about the maximum error magnitude calls for adding the absolute contributions, which gives $0.5\%$. Keep that separate from the signed change.

## ASR risks and items to check

1. Check the order of $x/y$ and the orientation of the cross-section on the board at 3:11-3:27.
2. Check the handout's notation for the mixed-partial subscripts and the order of differentiation at 4:12.
3. At 7:29, check the theorem's wording to see whether "continuous" refers to the function or to the mixed second partial derivatives.
4. Check the board at 11:17-12:45 for $d$, $\Delta$, $\delta$ and the use of equality or approximation signs.
5. Check the board at 13:50-14:18 to identify the object, the definition of the radius, the symbol for mass and which quantity each error applies to.

## Relationship to the main notes

The main course notes are [MECH40008_Ch9-9_2026-11-13_Partial_Differentiation.md](MECH40008_Ch9-9_2026-11-13_Partial_Differentiation.md). This excerpt records the source, timestamps and uncertainties for use alongside the full notes.
