---
id: angle-chasing
name: Angle chasing and cyclic quadrilaterals
group: Geometry
related: [similar-triangles, trigonometry, coordinates]
---
## What it is
Compute unknown angles from known ones, using these facts:
- The angles of a triangle sum to $180^\circ$.
- **Inscribed angle theorem:** an inscribed angle is half the central angle on the same arc, so angles on the same arc are equal.
- **Cyclic quadrilateral:** a convex quadrilateral $ABCD$ is cyclic exactly when $\angle A+\angle C=180^\circ$, equivalently when $\angle ABD=\angle ACD$.
- **Tangent-chord angle:** the angle between a tangent and a chord equals the inscribed angle in the alternate segment on that chord.
- **Thales:** an angle subtending a diameter is $90^\circ$.

The main move: find that four points lie on a circle (by equal angles), then use the circle to get more equal angles.

It works because angle relations are rigid and local. Spotting that two equal angles on the same side of a segment subtend it tells you the four points are concyclic.

## Recognize
- Perpendicular lines, altitudes, and feet of perpendiculars (right angles give circles with a diameter).
- Several equal angles in a diagram, or an angle condition to prove.
- A circle through three points of the figure, with a fourth that may lie on it.
- A claim of "concyclic", "collinear", or "perpendicular".

## Example: Feet of altitudes
**Problem.** In triangle $ABC$ let $D$ and $E$ be the feet of the altitudes from $A$ and $B$. Show that $A,B,D,E$ lie on a circle.
1. $\angle ADB=90^\circ$ and $\angle AEB=90^\circ$.
2. Both $D$ and $E$ see the segment $AB$ at a right angle, so they lie on the circle with diameter $AB$ (Thales' converse).
3. Hence $A,B,D,E$ are concyclic.

## Example: Reflecting the orthocenter
**Problem.** In an acute triangle $ABC$ with orthocenter $H$, let $H'$ be the reflection of $H$ over $BC$. Show that $H'$ lies on the circumcircle of $ABC$.
1. Let $E$ be the foot of the altitude from $B$ and $F$ the foot of the altitude from $C$. Both pass through $H$.
2. In right triangle $BEC$ the angle at $C$ is $C$, so $\angle HBC=\angle EBC=90^\circ-C$.
3. In right triangle $CFB$ the angle at $B$ is $B$, so $\angle HCB=\angle FCB=90^\circ-B$.
4. In triangle $BHC$: $\angle BHC=180^\circ-(90^\circ-C)-(90^\circ-B)=B+C=180^\circ-A$.
5. Reflection over $BC$ preserves angles, so $\angle BH'C=180^\circ-A$.
6. In an acute triangle $H$ is inside the triangle, on the altitude $AD$ with $D$ strictly between $B$ and $C$. So $H'$ lies on line $AD$ on the other side of $BC$ from $A$, and $ABH'C$ is a convex quadrilateral.
7. Its opposite angles at $A$ and $H'$ sum to $180^\circ$, so it is cyclic and $H'$ lies on the circumcircle.

## Mistakes
- Relying on a diagram's configuration. The same argument may fail for an obtuse triangle or a different point order. Use directed angles mod $180^\circ$ to be safe.
- Assuming a quadrilateral is convex when applying the cyclic criterion.
- Asserting points are concyclic because they "look" it.
- Mislabeling which arc an inscribed angle sees.

## Variations
- **Directed angles:** $\angle(\ell,m)$ mod $180^\circ$ remove configuration issues.
- **Spiral similarity and Miquel's theorem:** circles through a common point.
- **Radical axis:** pairs of circles and lines of equal power ([[similar-triangles]]).
- **Trigonometric alternative:** compute instead of chase ([[trigonometry]]).
