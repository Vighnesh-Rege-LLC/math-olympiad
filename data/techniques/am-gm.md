---
id: am-gm
name: AM-GM and mean inequalities
group: Inequalities
related: [cauchy-schwarz, symmetry, induction, polynomials]
---
## What it is
For non-negative reals $a_1,\dots,a_n$:
$$\frac{a_1+\dots+a_n}{n}\ \ge\ \sqrt[n]{a_1a_2\cdots a_n},$$
with equality exactly when all the $a_i$ are equal. This is the AM-GM inequality.

A consequence for two numbers: $a^2+b^2\ge2ab$, because $(a-b)^2\ge0$. The same trick, "a square is non-negative", proves many inequalities.

It works because the product of numbers with a fixed sum is largest when they are balanced. This tells you both the bound and the place where it is sharp, so the equality case guides how to split terms.

## Recognize
- A sum (or product) of positive terms is compared to a product (or sum).
- You are asked for the minimum of a sum like $x+\frac1x$, or the maximum of a product with fixed sum.
- The expected extremum occurs when variables are equal.
- Terms can be split or grouped so that their product becomes constant.

## Example: Minimum of $x+\frac1x$
**Problem.** Find the minimum of $x+\dfrac1x$ over $x>0$.
1. By AM-GM on the two terms: $\dfrac{x+\frac1x}2\ge\sqrt{x\cdot\frac1x}=1$.
2. So $x+\dfrac1x\ge2$.
3. Equality needs $x=\dfrac1x$, i.e. $x=1$, which is allowed. So the minimum is $2$.

## Example: A product inequality
**Problem.** For $a,b,c\ge0$ prove $(a+b)(b+c)(c+a)\ge8abc$.
1. Apply AM-GM to each factor: $a+b\ge2\sqrt{ab}$, $b+c\ge2\sqrt{bc}$, $c+a\ge2\sqrt{ca}$.
2. All terms are non-negative, so multiply the three inequalities: $(a+b)(b+c)(c+a)\ge8\sqrt{ab\cdot bc\cdot ca}=8abc$.
3. Equality holds when $a=b=c$ (it also holds when two of the variables are $0$).

## Example: Splitting to match equality
**Problem.** Positive reals $x,y$ satisfy $x+y=3$. Find the maximum of $x^2y$.
1. The product has $x$ twice, so split $x$ into two equal parts $\frac x2,\frac x2$ and apply AM-GM to the three numbers $\frac x2,\frac x2,y$.
2. $\dfrac{\frac x2+\frac x2+y}3\ge\sqrt[3]{\dfrac x2\cdot\dfrac x2\cdot y}$. The left side is $\dfrac{x+y}3=1$.
3. So $\dfrac{x^2y}4\le1$ and $x^2y\le4$.
4. Equality needs $\frac x2=y$, so with $x+y=3$ we get $y=1$, $x=2$. At that point $x^2y=4$, so the maximum is $4$.

## Mistakes
- Applying AM-GM to terms that can be negative. It requires non-negative numbers.
- Reaching a bound but never checking that equality is attainable. The bound may not be the true minimum or maximum.
- Choosing a split that makes the equality case impossible. Find where equality should occur first.
- Multiplying inequalities when some sides could be negative.

## Variations
- **Weighted AM-GM:** $\lambda_1a_1+\dots+\lambda_na_n\ge a_1^{\lambda_1}\cdots a_n^{\lambda_n}$ for non-negative $a_i$ and non-negative weights summing to $1$.
- **Power mean chain:** $\min\le\text{HM}\le\text{GM}\le\text{AM}\le\text{QM}\le\max$.
- **Homogenization:** use a constraint to make all terms the same degree before comparing.
- **Cauchy–Schwarz:** often an alternative when sums of squares or fractions appear ([[cauchy-schwarz]]).
- **Proof by induction:** the general case can be proved by forward-backward (Cauchy) induction ([[induction]]).
