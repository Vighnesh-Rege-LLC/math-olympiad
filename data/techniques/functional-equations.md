---
id: functional-equations
name: Functional equations
group: Algebra
related: [symmetry, induction, polynomials, modular-arithmetic]
---
## What it is
A functional equation relates the values of an unknown function at different points, and you must find all functions satisfying it. The standard toolkit:
- **Substitute special values:** $x=0$, $y=0$, $x=y$, $y=1$, $y=-x$, $y=1/x$.
- **Swap roles:** if the equation is symmetric after a substitution, use both versions.
- **Injectivity / surjectivity:** if $f(a)=f(b)$ forces $a=b$ (injective), you can cancel $f$. If every value is attained (surjective), you can choose arguments to hit any target.
- **Solve for $f$:** treat $f(x)$ and $f$ at a related point as unknowns in a linear system.
- **Check your answer:** substitute back. A found candidate must be verified.

It works because a rich equation holds for all inputs. Special inputs give constraints that, together, pin $f$ down.

## Recognize
- "Find all functions $f:\mathbb R\to\mathbb R$ such that...".
- An equation with $f$ applied to expressions in $x$ and $y$ for all $x,y$.
- A relation like $f(x)+2f(1/x)=3x$ involving $f$ at two linked points.
- Candidate solutions suggest themselves: linear, constant, $x^2$.

## Example: Solving a linear system
**Problem.** Find all functions $f:\mathbb R\setminus\{0\}\to\mathbb R$ with $f(x)+2f\!\left(\frac1x\right)=3x$ for every real $x\ne0$.
1. Replace $x$ by $\frac1x$: $f\!\left(\frac1x\right)+2f(x)=\dfrac3x$.
2. Now we have two equations in the unknowns $u=f(x)$ and $v=f(1/x)$: $u+2v=3x$ and $2u+v=\dfrac3x$.
3. Multiply the second by $2$ and subtract the first: $3u=\dfrac6x-3x$, so $f(x)=\dfrac2x-x$.
4. Check: $f(x)+2f(1/x)=\dfrac2x-x+2\left(2x-\dfrac1x\right)=3x$. ✓

## Example: Special substitutions
**Problem.** Find all $f:\mathbb R\to\mathbb R$ with $f(x)f(y)-f(xy)=x+y$ for all real $x,y$.
1. Put $y=0$, and let $c=f(0)$: $c\,f(x)-c=x$ for all $x$.
2. If $c=0$ the left side is $0$ but the right side is $x$, which fails for $x=1$. So $c\ne0$ and $f(x)=1+\dfrac xc$.
3. Put $x=y=0$ in the original: $c^2-c=0$, so $c=1$ (since $c\ne0$).
4. So $f(x)=1+x$. Check: $(1+x)(1+y)-(1+xy)=x+y$. ✓

## Example: Additive functions on the rationals
**Problem.** Find all $f:\mathbb Q\to\mathbb Q$ with $f(x+y)=f(x)+f(y)$.
1. Put $x=y=0$: $f(0)=2f(0)$, so $f(0)=0$.
2. Let $c=f(1)$. By induction $f(n)=nc$ for positive integers $n$ (since $f(n+1)=f(n)+f(1)$).
3. Putting $y=-x$ gives $f(-x)=-f(x)$, so $f(n)=nc$ for all integers $n$.
4. For $x=\frac pq$ with $q>0$: $q\,f\!\left(\frac pq\right)=f(p)=pc$ (adding $\frac pq$ to itself $q$ times). So $f\!\left(\frac pq\right)=c\cdot\frac pq$.
5. So $f(x)=cx$. Check: it works for any rational $c$.

(Over the reals this equation has other, wild solutions unless you add a condition like continuity or monotonicity.)

## Mistakes
- Finding a candidate and not verifying it in the original equation.
- Assuming $f$ is continuous, differentiable, or injective without justification.
- Dividing by $f(x)$ or $x$ when it could be zero. Handle the zero case separately.
- Forgetting solutions: constants $f\equiv0$ or $f\equiv1$ often satisfy the equation too.
- Substituting values outside the domain.

## Variations
- **Injectivity and surjectivity:** prove one early, then use cancellation or choose arguments freely.
- **Fixed points and iteration:** $f(f(x))=x$ equations.
- **Cauchy's equation:** the additive case above, extended using continuity.
- **Equations on integers:** use [[induction]] and [[modular-arithmetic]] after substituting small values.
- **Polynomial functional equations:** compare degrees and coefficients ([[polynomials]]).
