---
id: casework
name: Casework
group: Proof methods
related: [pigeonhole, modular-arithmetic, symmetry, extremal]
---
## What it is
Split the problem into a few exhaustive cases and handle each separately. The cases must cover every possibility (exhaustive); if they also do not overlap, you can add counts without double counting (exclusive).

It works because a hard general statement may become easy once an extra assumption is available in each case. In case $A$ you can use $x>0$, in case $B$ you have $x\le0$.

Good casework chooses cases that give you information, such as by residue class, by sign, by the position of a particular element, or by "largest value here / elsewhere". It then reduces the number of cases using [[symmetry]].

## Recognize
- The statement involves absolute values, minimums, maximums, or floor functions.
- A parameter takes a few types of value (parity, residue mod $3$, sign, size).
- A natural object has a special element (a person with the most friends, the largest side) and you can split on what happens at it.
- Direct search is finite but large, and structure reduces it.

## Example: Three mutually related people
**Problem.** Any two of six people are either friends or strangers. Show there are three people who are all mutual friends or all mutual strangers.
1. Pick a person $A$. The other $5$ people are each a friend or a stranger of $A$.
2. By [[pigeonhole]] either at least $3$ are friends of $A$, or at least $3$ are strangers of $A$. These are the two cases.
3. **Case 1: $A$ has three friends $X,Y,Z$.** If any two of them are friends, say $X,Y$, then $A,X,Y$ are three mutual friends. Otherwise $X,Y,Z$ are mutual strangers.
4. **Case 2: $A$ has three strangers $X,Y,Z$.** If any two of them are strangers, say $X,Y$, then $A,X,Y$ are mutual strangers. Otherwise $X,Y,Z$ are mutual friends.
5. Either way, a triple exists.

## Example: Twin-prime-like triples
**Problem.** Find all primes $p$ such that $p+2$ and $p+4$ are also prime.
1. Split by the residue of $p$ mod $3$, the three possible cases.
2. If $p\equiv0\pmod3$, then $p$ is prime and divisible by $3$, so $p=3$. Check: $3,5,7$ are all prime. ✓
3. If $p\equiv1\pmod3$, then $p+2\equiv0\pmod3$. Since $p+2>3$, it is composite. ✗
4. If $p\equiv2\pmod3$, then $p+4\equiv0\pmod3$. Since $p+4>3$, it is composite. ✗
5. So the only such prime is $p=3$.

## Mistakes
- Gaps: a case you didn't think of (negative values, zero, equality, small $n$). Say why your cases cover everything.
- Overlapping cases when counting, which counts an object twice.
- Too many cases. If you have $20$ cases, look for a better organizing idea or use symmetry to merge them.
- Doing one case carefully and waving the rest away with "similarly". Check that the others really are the same.

## Variations
- **Without loss of generality (WLOG):** when a problem is symmetric, assume an ordering such as $a\le b\le c$ (see [[symmetry]]).
- **Complementary counting:** count the cases that are not wanted.
- **Case on the extreme:** put the largest element or the first violation in a case of its own.
- **Residue cases:** all cases mod $n$ ([[modular-arithmetic]]).
