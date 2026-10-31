---
id: graph-theory
name: Graph theory basics
group: Combinatorics
related: [double-counting, parity, extremal, induction, coloring]
---
## What it is
A graph is a set of vertices joined by edges. Many puzzles about people, roads, tournaments, or games become questions about a graph once you decide what the vertices and edges are.

Basic facts to carry:
- The sum of all degrees is twice the number of edges ($\sum_vd(v)=2e$), so the number of odd-degree vertices is even.
- A **tree** is a connected graph with no cycle. A tree on $n$ vertices has exactly $n-1$ edges and has at least two leaves (degree-1 vertices) if $n\ge2$.
- A connected graph has a closed walk using every edge exactly once (an **Euler circuit**) if and only if every degree is even.

It works because it strips a problem to its structure. Arguments by [[double-counting]], [[extremal|extremal choice]], [[induction]] on vertices, and [[parity]] all become standard moves.

## Recognize
- Relationships between pairs: friends, games played, roads, handshakes, "knows".
- Paths, routes, cycles, connectivity, or coloring conditions.
- "Each person is connected to exactly $k$ others" or "no three are mutually...".
- A process that moves between states along allowed moves: states are vertices, moves are edges.

## Example: Trees have $n-1$ edges
**Problem.** Show that a tree with $n\ge1$ vertices has exactly $n-1$ edges.
1. Induct on $n$. For $n=1$ there is one vertex and no edges.
2. For $n\ge2$, take a longest path in the tree. Its end vertex $v$ has no neighbor off the path (the path could be extended) and no neighbor on the path other than the previous vertex (that would create a cycle). So $v$ is a leaf.
3. Remove $v$ and its edge. The result is still connected, because a path between two other vertices never passes through a vertex of degree $1$. It has no cycle, so it is a tree on $n-1$ vertices. It has $n-2$ edges by the induction hypothesis.
4. Adding back $v$ gives $n-1$ edges.

## Example: An impossible network
**Problem.** Can $15$ computers be wired so that each is connected to exactly $3$ others?
1. Suppose such a graph existed. The sum of the degrees is $15\cdot3=45$.
2. The sum of degrees is twice the number of edges, so it must be even.
3. $45$ is odd, so no such network exists.

## Example: Walking every bridge once
**Problem.** A town has islands and bridges forming a connected graph. A walk uses every bridge exactly once and starts and ends on different islands. Show that exactly two islands have an odd number of bridges.
1. Consider an island $x$ that is neither the start nor the end. Each time the walk passes through $x$ it enters by one bridge and leaves by another. So the bridges at $x$ are used in pairs, and $x$ has even degree.
2. The start island $s$: the walk leaves it once at the beginning, and each later visit enters and leaves. So the number of bridge-uses at $s$ is $1+2k$, which is odd. The same holds for the end island $t$ (enter once at the end plus pairs).
3. Since $s\ne t$ and every bridge is used exactly once, $s$ and $t$ have odd degree and all other islands have even degree.

## Mistakes
- Allowing loops or multiple edges when the problem says a simple graph, or the reverse.
- Assuming connected when not given. A tree argument may need each component separately.
- Using a result like "tree has a leaf" for a graph with a cycle.
- Modeling badly: if vertices and edges are chosen poorly, the graph does not capture the problem. Ask what is being related.

## Variations
- **Directed graphs and tournaments:** every pair joined by one directed edge ([[extremal]] gives a king).
- **Bipartite graphs:** vertices split into two sets with edges only across. A graph is bipartite exactly when it has no odd cycle.
- **Planar graphs:** Euler's formula $V-E+F=2$ for connected planar graphs.
- **Graph coloring:** color vertices so adjacent ones differ ([[coloring]]).
- **Ramsey type:** among six people, there are three mutual friends or three mutual strangers ([[casework]]).
