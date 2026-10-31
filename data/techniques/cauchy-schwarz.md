---
id: cauchy-schwarz
name: Cauchy–Schwarz and Titu's lemma
group: Inequalities
related: [am-gm, double-counting, symmetry]
---
## What it is
For real numbers $a_1,\dots,a_n$ and $b_1,\dots,b_n$:
$$\left(\sum a_i^2\right)\left(\sum b_i^2\right)\ \ge\ \left(\sum a_ib_i\right)^2,$$
with equality exactly when the vectors $(a_i)$ and $(b_i)$ are proportional.

Its most useful form for olympiads is **Titu's lemma** (also called the Engel form): for $x_i>0$,
$$\frac{a_1^2}{x_1}+\dots+\frac{a_n^2}{x_n}\ \ge\ \frac{(a_1+\dots+a_n)^2}{x_1+\dots+x_n}.$$

It works because it bounds a sum of products by sums of squares. When a problem has a squared quantity, or fractions with a square in the numerator, the inequality turns many terms into one.

## Recognize
- A constraint on $\sum a_i$ and an expression involving $\sum a_i^2$, or the reverse.
- Sums of fractions $\sum\frac{a_i}{b_i}$ that can be written as $\sum\frac{a_i^2}{a_ib_i}$.
- You need a lower bound for $\sum\frac1{x_i}$ with $\sum x_i$ fixed.
- A sum of square roots needs an upper bound.

## Example: Sum of squares
**Problem.** If $a+b+c=1$ show that $a^2+b^2+c^2\ge\dfrac13$.
1. Apply Cauchy–Schwarz with $(a,b,c)$ and $(1,1,1)$: $(a^2+b^2+c^2)(1+1+1)\ge(a+b+c)^2=1$.
2. So $a^2+b^2+c^2\ge\dfrac13$, with equality for $a=b=c=\dfrac13$.

## Example: Reciprocals
**Problem.** Positive reals $x,y,z$ satisfy $x+y+z=1$. Show that $\dfrac1x+\dfrac1y+\dfrac1z\ge9$.
1. Write each term as $\dfrac{1^2}{x}$ and apply Titu's lemma with numerators $1,1,1$.
2. $\dfrac{1^2}{x}+\dfrac{1^2}{y}+\dfrac{1^2}{z}\ge\dfrac{(1+1+1)^2}{x+y+z}=9$.
3. Equality for $x=y=z=\frac13$.

## Example: Nesbitt's inequality
**Problem.** For positive reals $a,b,c$ show $\dfrac a{b+c}+\dfrac b{c+a}+\dfrac c{a+b}\ge\dfrac32$.
1. Multiply numerator and denominator by $a$ (and similarly for the others): $\dfrac a{b+c}=\dfrac{a^2}{a(b+c)}$.
2. By Titu's lemma, the sum is at least $\dfrac{(a+b+c)^2}{a(b+c)+b(c+a)+c(a+b)}=\dfrac{(a+b+c)^2}{2(ab+bc+ca)}$.
3. Since $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)\ge3(ab+bc+ca)$ (because $a^2+b^2+c^2\ge ab+bc+ca$), the fraction is at least $\dfrac{3(ab+bc+ca)}{2(ab+bc+ca)}=\dfrac32$.

## Mistakes
- Using Titu with a denominator that can be negative or zero.
- Forgetting to check equality conditions. The bound is sharp only when the sequences are proportional.
- Choosing the wrong splitting of a term into $a_i$ and $b_i$. Try to make the equality condition match what you expect.
- Applying the inequality in the wrong direction. It bounds the square of a sum by a product of sums.

## Variations
- **Hölder's inequality:** the cube version, for non-negative reals: $\left(\sum a^3\right)\left(\sum b^3\right)\left(\sum c^3\right)\ge\left(\sum abc\right)^3$.
- **Rearrangement inequality:** a sum of products is largest when sequences are similarly ordered.
- **Sums of square roots:** $\left(\sum\sqrt{x_i}\right)^2\le n\sum x_i$.
- **Alternative proof:** [[am-gm]] often gives the same result, and works when terms aren't of the right shape.
