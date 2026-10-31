---
id: coloring
name: Coloring arguments
group: Combinatorics
related: [invariants, parity, double-counting, pigeonhole]
---
## What it is
Assign colors (or labels, or numbers) to the cells, points or vertices of a configuration so that every allowed piece or move interacts with the colors in a controlled way. Then count colors.

It works as an [[invariants|invariant]] built in space. If every tile of a certain shape covers exactly one cell of each color, then a tiling must use each color equally often, and a board with unequal color counts cannot be tiled.

The art is choosing the coloring: two colors for dominoes, four colors for $1\times4$ strips, stripes, diagonals, or $(i+j)\bmod k$.

## Recognize
- Tilings, coverings, or "can pieces fill this board?".
- A piece or token that moves by a fixed rule (knight, bishop, king, rook), and the question asks about reaching a place or making a tour.
- Regions of a grid are removed, and the remaining part is to be covered.
- Counts of two or more types of cell must match some quantity.

## Example: Strips of length 4
**Problem.** Can a $10\times10$ board be tiled by $1\times4$ rectangles (placed horizontally or vertically)?
1. Number rows and columns $0,\dots,9$ and color the cell $(i,j)$ with $c=(i+j)\bmod4$.
2. A horizontal strip covers cells with $i+j$ equal to $s,s+1,s+2,s+3$ for some $s$, which is each of the four colors exactly once. A vertical strip does the same.
3. So a tiling by $25$ strips covers each color exactly $25$ times.
4. Count cells by color. The residues $0,\dots,9$ mod $4$ occur $3,3,2,2$ times for residues $0,1,2,3$. Count the cells with $i+j\equiv1\pmod4$ by the pair of residues $(i\bmod4,\ j\bmod4)$: $(0,1)$ gives $3\cdot3=9$ cells, $(1,0)$ gives $9$, $(2,3)$ gives $2\cdot2=4$, and $(3,2)$ gives $4$. The total is $26$.
5. $26\ne25$, so no tiling exists.

## Example: A closed knight's tour on a $5\times5$ board
**Problem.** Can a knight visit every square of a $5\times5$ board exactly once and return to its starting square?
1. Color the board like a chessboard. A knight's move always goes from one color to the other.
2. A closed tour visiting all $25$ squares is a cycle of $25$ moves, alternating colors.
3. Alternating colors around a cycle requires an even number of squares, since the colors alternate and the tour must come back to the starting color.
4. $25$ is odd, so it is impossible.

## Mistakes
- Using a coloring where pieces do not cover colors uniformly. Check every orientation of every piece.
- Counting cells of each color wrongly. Recount using a formula or a small table.
- Treating "equal counts" as sufficient. A tiling-count coloring argument proves impossibility only. When counts match, you still must give a construction ([[constructive]]).
- Forgetting that you can try more than one coloring. If chessboard coloring fails, try stripes or $(i+j)\bmod3$.

## Variations
- **Weighted colorings:** assign numbers such as $\pm1$ (for example $(-1)^{i+j}$) or powers of a root of unity, not just colors, and show the total covered by any piece is fixed (often $0$).
- **Coloring graphs:** vertices colored so adjacent vertices differ (see [[graph-theory]]).
- **Coloring the plane:** color points, then use [[pigeonhole]] to find two of the same color at a given distance.
- **Coloring to prove existence:** probabilistic or counting colorings are advanced relatives.
