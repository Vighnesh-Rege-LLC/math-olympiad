---
id: parity
name: Parity
group: Number theory
related: [invariants, modular-arithmetic, coloring, double-counting]
---
## What it is
Parity is whether an integer is even or odd. It obeys simple rules: even $\pm$ even is even, odd $\pm$ odd is even, odd $\pm$ even is odd, and a product is odd only if every factor is odd. It is arithmetic mod $2$, the simplest case of [[modular-arithmetic]].

Parity is powerful because it throws away almost everything and keeps a robust two-valued fact. If a count must be even and you compute it as odd, you have a contradiction. If a quantity's parity never changes under a process, you have an [[invariants|invariant]].

## Recognize
- Objects pair up (edges join two vertices, dominoes cover two squares, handshakes involve two people).
- A process flips things (switches, signs, coin faces, colors) and the question is whether a state is reachable.
- A sum, product, or count is claimed to equal a specific number, and you can see its parity does not match.
- Moves alternate between two kinds of positions (a knight, a single step along a grid line).

## Example: Handshakes
**Problem.** At a party some people shake hands. Show that the number of people who shook an odd number of hands is even.
1. Add up, over all people, the number of hands each shook. Each handshake involves two people, so it is counted twice.
2. So the total is $2H$ where $H$ is the number of handshakes. It is even.
3. Split the total into people with an even count and people with an odd count. The even ones contribute an even amount.
4. So the contribution of the odd ones is even too. A sum of odd numbers is even only if there is an even number of them.
5. So the number of people with an odd count is even.

## Example: Making a sum zero with signs
**Problem.** Can one put a plus or minus sign in front of each of $1,2,\dots,10$ so that the total is $0$?
1. Changing a sign changes a term $m$ to $-m$, a change of $2m$, which is even. So the parity of the total never depends on the signs.
2. With all plus signs the sum is $1+2+\dots+10=55$, which is odd.
3. So every choice of signs gives an odd total, and it can never be $0$.
4. (For $1,\dots,11$ the sum is $66$, which is even. Parity doesn't forbid it, and indeed $11+10+9+3=33$ gives a split into two equal halves, so signs exist.)

## Mistakes
- Using parity to prove something is possible. Parity gives necessary conditions. For existence, construct an example ([[constructive]]).
- Forgetting that $0$ is even and negative numbers have parities too.
- Overlooking useful facts like $a^2\equiv a\pmod2$ and $a+b\equiv a-b\pmod2$, which let you replace awkward expressions by simple ones.
- Ignoring that a product of integers is even as soon as one factor is even.

## Variations
- **Counting pairs:** the handshake lemma is the degree-sum formula in graph theory (see [[graph-theory]]).
- **Parity of a permutation:** every swap of two elements flips the sign of a permutation, so the parity of the number of swaps needed to reach a given arrangement is fixed.
- **Mod 2 coloring:** squares of a board are colored by $(i+j)\bmod2$ (see [[coloring]]).
- **Parity plus size arguments:** an odd number of objects cannot be split into equal pairs, and a closed route alternating between two types has even length.
