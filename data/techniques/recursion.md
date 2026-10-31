---
id: recursion
name: Recurrences
group: Algebra
related: [induction, generating-functions, telescoping, polynomials]
---
## What it is
A recurrence expresses the $n$th term of a sequence using earlier terms. To count objects recursively, express the count for size $n$ using counts for smaller sizes, by looking at how a size-$n$ object is built from smaller ones.

For a linear recurrence $a_{n+2}=pa_{n+1}+qa_n$, the **characteristic equation** $t^2=pt+q$ gives roots $r,s$. If $r\ne s$ then $a_n=Ar^n+Bs^n$ with $A,B$ fixed by the first two terms. (If $r=s$, then $a_n=(A+Bn)r^n$.)

It works because a recurrence plus the starting terms determines the whole sequence. Solving a recurrence means finding a closed form, and proving that closed form usually takes one line of [[induction]].

## Recognize
- Counting tilings, strings, paths, or arrangements where the last piece splits the problem into smaller copies.
- A sequence defined by $a_{n+1}=f(a_n)$ or in terms of two previous terms.
- A quantity that changes by a simple rule when you add one more object (a line, a point, a person).
- Small values $1,2,3,5,8,\dots$ suggest a known sequence.

## Example: Domino tilings
**Problem.** In how many ways can a $2\times n$ board be tiled by $1\times2$ dominoes?
1. Let $T_n$ be the number of tilings. Directly: $T_1=1$ (one vertical domino) and $T_2=2$ (two vertical or two horizontal).
2. Look at the leftmost column of a $2\times n$ board. Either it is covered by a vertical domino, leaving a $2\times(n-1)$ board: $T_{n-1}$ ways.
3. Or the top-left cell is covered by a horizontal domino. Then the bottom-left cell must also be covered by a horizontal domino (a vertical one would not fit), and two columns are used: $T_{n-2}$ ways.
4. These cases are exclusive and exhaustive, so $T_n=T_{n-1}+T_{n-2}$. These are Fibonacci numbers: $1,2,3,5,8,\dots$.

## Example: Regions cut by lines
**Problem.** $n$ lines in the plane, no two parallel and no three through one point, cut the plane into how many regions?
1. Let $R_n$ be the count; $R_0=1$.
2. Add the $n$th line. It crosses the previous $n-1$ lines at $n-1$ distinct points, which cut it into $n$ pieces.
3. Each piece splits one existing region into two, so the new line adds $n$ regions: $R_n=R_{n-1}+n$.
4. Therefore $R_n=1+(1+2+\dots+n)=1+\dfrac{n(n+1)}2$.

## Example: Characteristic equation
**Problem.** A sequence has $a_0=2$, $a_1=5$ and $a_{n+2}=5a_{n+1}-6a_n$. Find $a_n$.
1. The characteristic equation is $t^2=5t-6$, i.e. $(t-2)(t-3)=0$, with roots $2$ and $3$.
2. So $a_n=A\,2^n+B\,3^n$.
3. From $a_0=2$: $A+B=2$. From $a_1=5$: $2A+3B=5$. Subtracting twice the first from the second: $B=1$, so $A=1$.
4. Hence $a_n=2^n+3^n$. Check: $a_2=5\cdot5-6\cdot2=13=4+9$. ✓

## Mistakes
- Wrong initial conditions or missing base cases, which shifts the whole sequence.
- Cases that overlap or miss objects when deriving the recurrence. Describe every object exactly once.
- Using the distinct-roots formula when the roots coincide.
- Trusting a pattern guessed from a few terms without a proof.

## Variations
- **Generating functions:** turn the recurrence into an equation for a power series ([[generating-functions]]).
- **Telescoping:** if $a_{n+1}-a_n$ is simple, sum it ([[telescoping]]).
- **Divide and conquer:** $T(2n)=2T(n)+c$ type recurrences.
- **Inhomogeneous recurrences:** $a_{n+1}=2a_n+1$ can be solved by shifting: $a_{n+1}+1=2(a_n+1)$.
- **Invariant of a recurrence:** a combination of terms that stays constant ([[invariants]]).
