---
id: expectation
name: Expectation and probabilistic method
group: Combinatorics
related: [double-counting, pigeonhole, recursion, constructive]
---
## What it is
The **expected value** of a random quantity $X$ is its average over all outcomes. Two facts do most of the work:
- **Linearity of expectation:** $E[X+Y]=E[X]+E[Y]$, always, even when $X$ and $Y$ are dependent.
- **Indicator variables:** write a count as a sum of $0/1$ variables $I_j$, one per object. Then $E[\text{count}]=\sum_jP(I_j=1)$.

The **probabilistic method** uses the averaging principle: a random object has some quantity with expected value $\mu$, so some object has that quantity $\ge\mu$ and some has it $\le\mu$. That proves existence without building the object.

It works because linearity lets you ignore dependencies, and averaging is the pigeonhole principle for numbers ([[pigeonhole]]).

## Recognize
- You are asked for an expected value of a count (fixed points, runs, pairs).
- A problem says "show there exists a way to... with at least $k$ ...", and a random choice makes each part succeed with probability $p$.
- Waiting-time questions: expected number of tries until something happens.
- A sum over objects of "does this object satisfy the condition".

## Example: Fixed points of a random permutation
**Problem.** A permutation of $1,\dots,n$ is chosen uniformly at random. What is the expected number of fixed points (positions $i$ with $\sigma(i)=i$)?
1. Let $I_i=1$ if $\sigma(i)=i$, else $0$. The number of fixed points is $\sum_iI_i$.
2. $P(I_i=1)=\dfrac1n$, because $\sigma(i)$ is equally likely to be any of the $n$ values.
3. By linearity, $E=n\cdot\dfrac1n=1$, for every $n$. The indicators are dependent, but linearity does not care.

## Example: Probabilistic existence
**Problem.** A graph has $e$ edges. Show its vertices can be split into two sets so that at least $\dfrac e2$ edges go between the sets.
1. Put each vertex independently into set $A$ or set $B$ with probability $\frac12$ each.
2. An edge $uv$ crosses when $u$ and $v$ land in different sets, with probability $\frac12$.
3. By linearity, the expected number of crossing edges is $\dfrac e2$.
4. A random variable cannot be less than its average for every outcome, so some split gives at least $\dfrac e2$ crossing edges.

## Example: Waiting time
**Problem.** A fair die is rolled repeatedly. What is the expected number of rolls until the first six?
1. Let $E$ be the expected number of rolls.
2. The first roll is a six with probability $\frac16$, and then the process stops after $1$ roll.
3. Otherwise (probability $\frac56$), one roll is used and the situation is as at the start. So $E=1+\dfrac56E$.
4. $E$ is finite, because the chance of needing more than $n$ rolls is $\left(\frac56\right)^n$, which shrinks geometrically. So we may solve: $\dfrac E6=1$, so $E=6$.

## Mistakes
- Assuming independence where there is none, and multiplying probabilities. Linearity of expectation does not need independence; products of probabilities do.
- Treating the expectation as the most likely value. The average need not be attained, but it does force a value on each side of it.
- Counting outcomes unevenly. Make sure the random model is uniform over the objects you intend.
- In the existence argument, forgetting to say that "some outcome is at least the average".

## Variations
- **Variance and second moment:** show a variable is concentrated near its mean.
- **Alteration method:** pick randomly, then fix the few bad parts.
- **First-step analysis:** the waiting-time example, a recurrence on the expectation ([[recursion]]).
- **Counting form:** expected count is a [[double-counting]] of pairs (object, event).
