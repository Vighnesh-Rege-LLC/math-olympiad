---
id: coordinates
name: Coordinate geometry
group: Geometry
related: [complex-numbers, trigonometry, similar-triangles, symmetry]
---
## What it is
Place the figure in a coordinate system and turn geometric statements into algebra: distances become $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$, lines become equations, perpendicularity becomes slopes with product $-1$ (or a zero dot product), and circles become $(x-h)^2+(y-k)^2=r^2$.

The key choice is the coordinate system. Put the origin at a natural point and an axis along a natural line, so that as many coordinates as possible are $0$ or symmetric. A well-chosen frame turns a messy statement into a short computation.

It works because algebra is mechanical. Once the setup is right, the proof is a verification, and it avoids most dependence on the diagram, though sign and root choices still need care.

## Recognize
- The figure has right angles, a rectangle, a square, or a line you can use as an axis.
- Distances, midpoints, ratios, or loci (sets of points satisfying a condition) are involved.
- Synthetic angle-chasing gets stuck, or depends on a diagram.
- The statement is an identity about lengths (sum of squares, ratios).

## Example: A rectangle identity
**Problem.** $ABCD$ is a rectangle and $P$ is any point in the plane. Show that $PA^2+PC^2=PB^2+PD^2$.
1. Place $A=(0,0)$, $B=(a,0)$, $C=(a,b)$, $D=(0,b)$, and let $P=(x,y)$.
2. $PA^2=x^2+y^2$ and $PC^2=(x-a)^2+(y-b)^2$.
3. $PB^2=(x-a)^2+y^2$ and $PD^2=x^2+(y-b)^2$.
4. Both $PA^2+PC^2$ and $PB^2+PD^2$ equal $x^2+y^2+(x-a)^2+(y-b)^2$, so they are equal.

## Example: A locus
**Problem.** $A$ and $B$ are points at distance $3$. Describe the set of points $P$ with $PA=2\,PB$.
1. Put $A=(0,0)$ and $B=(3,0)$, and let $P=(x,y)$.
2. $PA=2PB$ means $x^2+y^2=4\big((x-3)^2+y^2\big)$ (both sides are non-negative, so squaring loses nothing).
3. Expand: $x^2+y^2=4x^2-24x+36+4y^2$, i.e. $3x^2+3y^2-24x+36=0$, i.e. $x^2+y^2-8x+12=0$.
4. Complete the square: $(x-4)^2+y^2=4$.
5. The locus is the circle with center $(4,0)$ and radius $2$.

## Mistakes
- A coordinate system that makes the problem harder: general positions of all vertices lead to heavy algebra. Use symmetry to put points on axes.
- Assuming a special case (an isosceles triangle, a right angle) by choosing coordinates too specially. Keep as many parameters as the problem has degrees of freedom.
- Arithmetic slips. Re-verify by plugging in a specific point.
- Squaring both sides when one side could be negative.

## Variations
- **Vectors:** dot products for angles and perpendicularity.
- **Barycentric coordinates:** weights relative to a triangle, strong for concurrency and ratios.
- **Complex numbers:** treat the plane as $\mathbb C$ for rotations ([[complex-numbers]]).
- **Trigonometric coordinates:** $(r\cos\theta,\ r\sin\theta)$ when circles are involved ([[trigonometry]]).
- **Shoelace formula:** area from coordinates of the vertices.
