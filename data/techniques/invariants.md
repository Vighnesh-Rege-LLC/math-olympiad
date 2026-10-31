---
id: invariants
name: Invariants and monovariants
group: Combinatorics
related: [parity, modular-arithmetic, extremal, induction, coloring]
---
## What it is
A process changes a configuration step by step: moves on a board, operations on numbers, swaps. An **invariant** is a quantity that does not change under any allowed step. A **monovariant** is a quantity that strictly decreases (or strictly increases) at every step and takes values in a set where this cannot go on forever, such as the non-negative integers.

Invariants prove impossibility. If the start and the target have different values of an invariant, no sequence of steps connects them. Monovariants prove that a process must stop, or that it must end in a particular state.

An invariant can be a sum, a parity, a remainder, a color count, or a product. Try small cases and see what survives.

## Recognize
- The problem asks "is it possible to reach...?" and the answer feels like no.
- A repeated operation is applied to a collection: numbers erased and replaced, tokens moved, signs flipped.
- The problem asks you to show a process terminates, or to find the final result of any order of operations.
- After a few trials, something stays the same: a total, a parity, a count mod $3$.

## Example: The last number on the board
**Problem.** The numbers $1,2,\dots,2023$ are written on a board. In each step choose two numbers $a,b$, erase them and write $|a-b|$. After $2022$ steps one number remains. Can it be $1$?
1. Try to find what each step preserves. The sum changes from $a+b$ to $|a-b|$, which is not constant. But $|a-b|\equiv a+b\pmod 2$, so the parity of the sum does not change.
2. Initially the sum is $\frac{2023\cdot2024}{2}=2023\cdot1012$, which is even.
3. After every step the sum of the numbers on the board is even.
4. At the end the single number is that sum, so it is even. It cannot be $1$.

## Example: Dominoes on a damaged board
**Problem.** Two opposite corner squares are removed from an $8\times8$ board. Can the remaining $62$ squares be tiled by $1\times2$ dominoes?
1. Look for a property every domino shares. Each domino covers two adjacent squares.
2. Color the board like a chessboard. Adjacent squares have different colors, so every domino covers exactly one white and one black square.
3. So any tiling covers equally many white and black squares. The difference (white minus black) is invariant: zero for any set of dominoes.
4. Opposite corners have the same color, say both white. The remaining board has $30$ white and $32$ black squares.
5. The difference is not zero, so no tiling exists.

## Example: A process that must end (monovariant)
**Problem.** $n$ red and blue stones lie in a row. A move picks a red stone immediately followed by a blue stone and swaps them. Show that the process cannot go on forever.
1. Count $P$, the number of pairs of stones $(i,j)$ with $i<j$, stone $i$ red and stone $j$ blue.
2. A move swaps adjacent stones at positions $k,k+1$ (red at $k$, blue at $k+1$). For any third stone, its position relative to both swapped stones is unchanged, so pairs involving a third stone are unchanged.
3. The pair $(k,k+1)$ itself was a counted pair (red then blue). After the swap it is blue then red, and it is no longer counted. So $P$ drops by exactly $1$.
4. $P$ starts at some value at most $\binom n2$ and is never negative. So there are at most $\binom n2$ moves.

## Mistakes
- Proving "the invariant is preserved" in only one case of the operation. Check every allowed move, including edge cases.
- Choosing an invariant that is equal at the start and the target, so it proves nothing. You need a difference between them.
- Using an invariant to claim something is possible. Invariants only show impossibility. For possibility, give an explicit construction ([[constructive]]).
- A monovariant that is not integer-valued, so it could decrease forever (for example, real numbers that keep halving).

## Variations
- **Coloring invariants:** see [[coloring]]. Counts of colored cells covered by a piece act like invariants.
- **Residue invariants:** a quantity mod $2$, $3$, or $9$ (see [[parity]] and [[modular-arithmetic]]).
- **Ranking monovariants:** a lexicographic order or a sorted-sequence pattern improves each step, even when no single number monotonically changes.
