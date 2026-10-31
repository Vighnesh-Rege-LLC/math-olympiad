---
id: descent
name: Infinite descent and Vieta jumping
group: Proof methods
related: [extremal, modular-arithmetic, diophantine, induction]
---
## What it is
**Infinite descent** proves that no solutions exist. Assume a solution in positive integers exists, and from it build a strictly smaller solution. Repeating forever would give an infinite decreasing sequence of positive integers, which is impossible. Equivalently, pick the smallest solution (see [[extremal]]) and produce a smaller one.

**Vieta jumping** is a particular descent. If $(a,b)$ solves an equation that is quadratic in $a$, the other root $a'$ of the same quadratic gives another solution $(a',b)$, and Vieta's formulas say $a'$ is an integer. Jump between roots to make the pair smaller.

It works because positive integers cannot decrease forever. Descent turns "there is a solution" into "there is a smaller one", which cannot hold for the smallest.

## Recognize
- An equation in integers that you suspect has no nontrivial solutions, especially one that is homogeneous (every term has the same degree).
- A divisibility condition like $ab+1\mid a^2+b^2$ symmetric in $a,b$ and quadratic in each.
- Reducing mod a small number shows every variable is divisible by that number.
- You have a result of the form "the only solution is $0$" or "$k$ must be a perfect square".

## Example: No solutions for $x^2+y^2=3z^2$
**Problem.** Show that the only integers with $x^2+y^2=3z^2$ are $x=y=z=0$.
1. Suppose there is a nonzero solution, and take one with $|x|+|y|+|z|$ as small as possible, not all zero. We will build a smaller one.
2. Squares are $0$ or $1$ mod $3$. If $x^2+y^2\equiv0\pmod3$, then both $x^2$ and $y^2$ are $0$ mod $3$ (otherwise the sum is $1$ or $2$ mod $3$).
3. So $3\mid x$ and $3\mid y$. Write $x=3a$, $y=3b$. The equation becomes $9a^2+9b^2=3z^2$, so $z^2=3(a^2+b^2)$.
4. Then $3\mid z^2$, so $3\mid z$. Write $z=3c$. Then $9c^2=3(a^2+b^2)$, so $a^2+b^2=3c^2$.
5. So $(a,b,c)$ is another nonzero solution, with $|a|+|b|+|c|=\frac13(|x|+|y|+|z|)$. It is smaller, contradicting minimality.
6. Therefore no nonzero solution exists.

## Example: Vieta jumping
**Problem.** Let $a,b$ be positive integers with $ab+1\mid a^2+b^2$. Show that $\dfrac{a^2+b^2}{ab+1}$ is a perfect square.
1. Let $k=\frac{a^2+b^2}{ab+1}$, a positive integer. Suppose $k$ is not a perfect square. Among all pairs of positive integers $(a,b)$ with $a^2+b^2=k(ab+1)$, choose one with $a+b$ minimal. By symmetry assume $a\ge b$.
2. View the equation as a quadratic in $a$: $a^2-kb\,a+(b^2-k)=0$. Its roots are $a$ and $a'$, with $a+a'=kb$ and $aa'=b^2-k$.
3. So $a'=kb-a$ is an integer, and $(a',b)$ satisfies the same equation.
4. **$a'\ne0$:** if $a'=0$, then $b^2-k=0$ and $k=b^2$ would be a perfect square.
5. **$a'$ is not negative:** if $a'\le-1$, then $a'^2-kba'+b^2-k=0$ with $-kba'\ge kb\ge k$, so $0=a'^2-kba'+b^2-k\ge a'^2+b^2>0$, a contradiction.
6. So $a'$ is a positive integer, and $(a',b)$ is a valid pair. Minimality forces $a'+b\ge a+b$, i.e. $a'\ge a$.
7. But $a'=\dfrac{b^2-k}{a}<\dfrac{b^2}{a}\le b\le a$ (using $a\ge b$). So $a'<a$, contradicting step 6.
8. So $k$ is a perfect square.

## Mistakes
- Not checking that the new solution is also in the allowed set (positive, integer, satisfies the same condition). In Vieta jumping the sign of the new root needs its own argument.
- Using descent to claim a solution exists. Descent shows nonexistence, or shows a structure, never produces a solution by itself.
- Choosing a measure that does not strictly decrease. Show the new value is strictly smaller.
- In Vieta jumping, forgetting the symmetric case $a=b$ or the case where the "smaller" root equals the larger.

## Variations
- **Descent via divisibility:** reduce mod $p$ to show each variable is a multiple of $p$, divide out, repeat (first example).
- **Vieta jumping:** quadratic in two variables, symmetric or nearly so. A common ending is that a boundary case (a root $0$) pins the answer.
- **Descent on a different quantity:** the size of a configuration, a perimeter, or the number of objects.
- **Fermat's classic:** $x^4+y^4=z^2$ has no positive solutions, proved by descent.
