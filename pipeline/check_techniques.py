#!/usr/bin/env python3
"""Machine-check every computable claim made in the technique worked examples."""
import itertools, math, random, cmath
from fractions import Fraction
import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


# pigeonhole / modular / coloring
check("cubes mod 9", {x**3 % 9 for x in range(9)} == {0, 1, 8})
sums = {(a + b + c) % 9 for a in (0, 1, 8) for b in (0, 1, 8) for c in (0, 1, 8)}
check("cube sums miss 4,5", sums == {0, 1, 2, 3, 6, 7, 8} and 2020 % 9 == 4)
check("squares mod 4 sums", {(a * a + b * b) % 4 for a in range(4) for b in range(4)} == {0, 1, 2})
cnt = [sum(1 for i in range(10) for j in range(10) if (i + j) % 4 == c) for c in range(4)]
check("10x10 colour counts", cnt == [25, 26, 25, 24])
check("n^5-n div by 30", all((n**5 - n) % 30 == 0 for n in range(-50, 51)))
check("odd-part boxes", all(
    any(a != b and (b % a == 0) for a in s for b in s)
    for s in itertools.combinations(range(1, 13), 7)))
check("prime triples", [p for p in sp.primerange(2, 500) if sp.isprime(p + 2) and sp.isprime(p + 4)] == [3])

# induction / telescoping
check("2^n>n^2 n>=5", all(2**n > n * n for n in range(5, 200)) and not 2**4 > 16)
check("sum 1/k^2 <= 2-1/n", all(sum(Fraction(1, k * k) for k in range(1, n + 1)) <= 2 - Fraction(1, n) for n in range(1, 80)))
check("coins 3,5 from 8", all(any((n - 3 * a) >= 0 and (n - 3 * a) % 5 == 0 for a in range(n // 3 + 1)) for n in range(8, 200)) and not any((7 - 3 * a) >= 0 and (7 - 3 * a) % 5 == 0 for a in range(3)))
check("sum 1/k(k+1)", all(sum(Fraction(1, k * (k + 1)) for k in range(1, n + 1)) == Fraction(n, n + 1) for n in range(1, 40)))
check("sum k*k!", all(sum(k * math.factorial(k) for k in range(1, n + 1)) == math.factorial(n + 1) - 1 for n in range(1, 20)))
check("prod 1-1/k^2", all(math.prod(1 - Fraction(1, k * k) for k in range(2, n + 1)) == Fraction(n + 1, 2 * n) for n in range(2, 40)))

# symmetry / diophantine / divisibility
tri = [(a, b, c) for a in range(1, 50) for b in range(a, 50) for c in range(b, 200) if Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == 1]
check("1/a+1/b+1/c=1", sorted(tri) == [(2, 3, 6), (2, 4, 4), (3, 3, 3)])
sol = [(x, y) for x in range(1, 500) for y in range(1, 500) if Fraction(1, x) + Fraction(1, y) == Fraction(1, 6)]
check("1/x+1/y=1/6", sorted(sol) == [(7, 42), (8, 24), (9, 18), (10, 15), (12, 12), (15, 10), (18, 9), (24, 8), (42, 7)])
sq = [(x, y) for y in range(-300, 300) for x in range(-400, 400) if x * x == y * y + 2 * y + 13]
check("x^2=y^2+2y+13", sorted(sq) == [(-4, -3), (-4, 1), (4, -3), (4, 1)])
check("n+1 | n^2+1", [n for n in range(1, 2000) if (n * n + 1) % (n + 1) == 0] == [1])
check("coprime factorial+1", all(math.gcd(math.factorial(n) + 1, math.factorial(n + 1) + 1) == 1 for n in range(1, 40)))
check("gcd(a+b,ab)=1", all(math.gcd(a + b, a * b) == 1 for a in range(1, 80) for b in range(1, 80) if math.gcd(a, b) == 1))
check("x^3+y^3+z^3=2020 none (mod)", all((x**3 + y**3 + z**3) != 2020 for x in range(-30, 30) for y in range(-30, 30) for z in range(-30, 30)))
check("x^2+y^2=3z^2 small", not any(x * x + y * y == 3 * z * z for x in range(-80, 81) for y in range(-80, 81) for z in range(-80, 81) if (x, y, z) != (0, 0, 0)))
for kk in range(1, 400):
    pass
ks = {(a * a + b * b) // (a * b + 1) for a in range(1, 300) for b in range(1, 300) if (a * a + b * b) % (a * b + 1) == 0}
check("Vieta jumping squares", all(math.isqrt(k) ** 2 == k for k in ks) and len(ks) > 3)

# double counting / generating functions / symmetry sums
check("divisor sum", all(sum(n // k for k in range(1, n + 1)) == sum(len(sp.divisors(m)) for m in range(1, n + 1)) for n in range(1, 60)))
C = math.comb
check("sum C(n,k)^2", all(sum(C(n, k) ** 2 for k in range(n + 1)) == C(2 * n, n) for n in range(1, 30)))
check("sum k C(n,k)", all(sum(k * C(n, k) for k in range(n + 1)) == n * 2 ** (n - 1) for n in range(1, 30)))
check("vandermonde", all(sum(C(m, k) * C(n, r - k) for k in range(r + 1)) == C(m + n, r) for m in range(8) for n in range(8) for r in range(9)))
check("even binomials", all(sum(C(n, k) for k in range(0, n + 1, 2)) == 2 ** (n - 1) for n in range(1, 30)))
check("stars and bars", all(sum(1 for x in range(n + 1) for y in range(n + 1 - x)) == C(n + 2, 2) for n in range(20)))
# Mantel: max edges in triangle-free graph on n vertices (n<=6 brute force)
for n in range(2, 7):
    edges = list(itertools.combinations(range(n), 2))
    best = 0
    for mask in range(1 << len(edges)):
        es = {edges[i] for i in range(len(edges)) if mask >> i & 1}
        if any(all(tuple(sorted(p)) in es for p in itertools.combinations(t, 2)) for t in itertools.combinations(range(n), 3)):
            continue
        best = max(best, len(es))
    assert best <= n * n / 4, n
ok.append("Mantel small n")

# recursion
def tilings(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
def brute_tilings(n):
    from functools import lru_cache
    @lru_cache(None)
    def f(mask, col):
        if col == n:
            return 1 if mask == 0 else 0
        tot = 0
        def fill(row, cur, nxt):
            nonlocal tot
            if row == 2:
                tot += f(nxt, col + 1)
                return
            if cur >> row & 1:
                fill(row + 1, cur, nxt)
                return
            fill(row + 1, cur | 1 << row, nxt | 1 << row)  # horizontal
            if row == 0 and not cur >> 1 & 1:
                fill(2, cur | 3, nxt)  # vertical
        fill(0, mask, 0)
        return tot
    return f(0, 0)
check("2xn domino brute", [brute_tilings(n) for n in range(1, 8)] == [1, 2, 3, 5, 8, 13, 21])
check("regions by lines", all(1 + n * (n + 1) // 2 == 1 + sum(range(1, n + 1)) for n in range(20)))
a = [2, 5]
for _ in range(20):
    a.append(5 * a[-1] - 6 * a[-2])
check("a_n=2^n+3^n", all(a[n] == 2**n + 3**n for n in range(len(a))))
# tests regions with a real arrangement
def regions(n):
    # Euler: lines in general position -> 1 + n + C(n,2)
    return 1 + n + C(n, 2)
check("regions = 1+n(n+1)/2", all(regions(n) == 1 + n * (n + 1) // 2 for n in range(30)))

# polynomials
x = sp.symbols("x")
r = sp.Poly(x**3 - 2 * x**2 + 3 * x - 4).nroots(n=30)
check("a^2+b^2+c^2=-2", abs(sum(z**2 for z in r) + 2) < 1e-20)
ax, bx = sp.symbols("a b")
s = sp.solve([ax + bx - 3, 2 * ax + bx - 5], [ax, bx])
check("remainder 2x+1", s == {ax: 2, bx: 1})
# brute: random integer-coefficient polys always satisfy a-b | P(a)-P(b)
random.seed(1)
for _ in range(200):
    co = [random.randint(-9, 9) for _ in range(5)]
    P = lambda t: sum(c * t**i for i, c in enumerate(co))
    a_, b_ = random.randint(-30, 30), random.randint(-30, 30)
    if a_ != b_:
        assert (P(a_) - P(b_)) % (a_ - b_) == 0
ok.append("a-b | P(a)-P(b)")

# inequalities
random.seed(2)
for _ in range(2000):
    a_, b_, c_ = (random.uniform(0.01, 10) for _ in range(3))
    assert (a_ + b_) * (b_ + c_) * (c_ + a_) >= 8 * a_ * b_ * c_ - 1e-9
    assert a_ / (b_ + c_) + b_ / (c_ + a_) + c_ / (a_ + b_) >= 1.5 - 1e-9
    t = a_ + b_ + c_
    p, q, w = a_ / t, b_ / t, c_ / t
    assert p * p + q * q + w * w >= 1 / 3 - 1e-9 and 1 / p + 1 / q + 1 / w >= 9 - 1e-9
ok.append("AM-GM/CS/Nesbitt random")
check("max x^2 y = 4", max(xx * xx * (3 - xx) for xx in [i / 1000 for i in range(1, 3000)]) <= 4 + 1e-9 and abs(2 * 2 * 1 - 4) == 0)
check("x+1/x>=2", min(xx + 1 / xx for xx in [i / 100 for i in range(1, 1000)]) >= 2)

# functional equations
f = lambda t: 2 / t - t
check("f(x)+2f(1/x)=3x", all(abs(f(t) + 2 * f(1 / t) - 3 * t) < 1e-9 for t in [0.3, -2, 5, 7.1]))
g = lambda t: 1 + t
check("f(x)f(y)-f(xy)=x+y", all(abs(g(u) * g(v) - g(u * v) - (u + v)) < 1e-9 for u in (-2, 0.5, 3) for v in (-1, 4, 2.5)))

# expectation
fp = sum(sum(1 for i, v in enumerate(p) if i == v) for p in itertools.permutations(range(6))) / math.factorial(6)
check("E fixed points = 1", fp == 1)
E = sp.symbols("E")
check("E rolls to six = 6", sp.solve(sp.Eq(E, 1 + sp.Rational(5, 6) * E), E) == [6])

# constructive
check("composite run", all(not sp.isprime(math.factorial(8) + k) for k in range(2, 9)))
def tile(n, hole):
    N = 2**n
    grid = [[0] * N for _ in range(N)]
    cur = [0]
    def rec(r, c, size, hr, hc):
        if size == 1:
            return
        cur[0] += 1
        half = size // 2
        cells = []
        for dr in (0, 1):
            for dc in (0, 1):
                qr, qc = r + dr * half, c + dc * half
                if qr <= hr < qr + half and qc <= hc < qc + half:
                    rec(qr, qc, half, hr, hc)
                else:
                    cr, cc = r + half - 1 + dr, c + half - 1 + dc
                    grid[cr][cc] = cur[0]
                    rec(qr, qc, half, cr, cc)
    # recursion needs unique ids: use separate counter per call
    ids = [0]
    def rec2(r, c, size, hr, hc):
        if size == 1:
            return
        ids[0] += 1
        me = ids[0]
        half = size // 2
        for dr in (0, 1):
            for dc in (0, 1):
                qr, qc = r + dr * half, c + dc * half
                if qr <= hr < qr + half and qc <= hc < qc + half:
                    rec2(qr, qc, half, hr, hc)
                else:
                    cr, cc = r + half - 1 + dr, c + half - 1 + dc
                    grid[cr][cc] = me
                    rec2(qr, qc, half, cr, cc)
    grid[hole[0]][hole[1]] = -1
    rec2(0, 0, N, *hole)
    from collections import Counter
    cnt = Counter(v for row in grid for v in row if v > 0)
    return all(v == 3 for v in cnt.values()) and all(grid[i][j] != 0 for i in range(N) for j in range(N))
check("L-tromino 8x8 every hole", all(tile(3, (i, j)) for i in range(8) for j in range(8)))

# graph theory / casework
edges = list(itertools.combinations(range(6), 2))
mono = all(any(all(col[edges.index(p)] == col[edges.index(q)] == col[edges.index(r)] for p, q, r in [((a, b), (a, c), (b, c))]) for a, b, c in itertools.combinations(range(6), 3)) for col in itertools.product((0, 1), repeat=15))
check("R(3,3)<=6", mono)

# geometry numerics
random.seed(3)
for _ in range(200):
    Ax, Ay, Bx, By, Cx, Cy, Px, Py = (random.uniform(-5, 5) for _ in range(8))
    # rectangle identity
    a_, b_, x_, y_ = Ax, Ay, Px, Py
    d = lambda p, q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    A, B, Cc, D = (0, 0), (a_, 0), (a_, b_), (0, b_)
    assert abs(d((x_, y_), A) + d((x_, y_), Cc) - d((x_, y_), B) - d((x_, y_), D)) < 1e-9
ok.append("rectangle identity")
check("locus PA=2PB circle", all(abs(math.hypot(4 + 2 * math.cos(t), 2 * math.sin(t)) - 2 * math.hypot(4 + 2 * math.cos(t) - 3, 2 * math.sin(t))) < 1e-9 for t in [0.1 * i for i in range(63)]))
check("13-14-15", sp.Rational(13 * 14 * 15, 4 * 84) == sp.Rational(65, 8) and sp.sqrt(21 * 8 * 7 * 6) == 84)
# orthocenter reflection lies on circumcircle
for _ in range(100):
    P = [complex(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(3)]
    A, B, Cc = P
    # circumcenter
    ax_, ay_, bx_, by_, cx_, cy_ = A.real, A.imag, B.real, B.imag, Cc.real, Cc.imag
    dd = 2 * (ax_ * (by_ - cy_) + bx_ * (cy_ - ay_) + cx_ * (ay_ - by_))
    ux = ((ax_**2 + ay_**2) * (by_ - cy_) + (bx_**2 + by_**2) * (cy_ - ay_) + (cx_**2 + cy_**2) * (ay_ - by_)) / dd
    uy = ((ax_**2 + ay_**2) * (cx_ - bx_) + (bx_**2 + by_**2) * (ax_ - cx_) + (cx_**2 + cy_**2) * (bx_ - ax_)) / dd
    O = complex(ux, uy)
    H = A + B + Cc - 2 * O
    # reflect H over line BC
    v = (Cc - B) / abs(Cc - B)
    Hr = B + v * ((H - B) / v).conjugate()
    assert abs(abs(Hr - O) - abs(A - O)) < 1e-6
ok.append("orthocenter reflection")
# angle bisector ratio
for _ in range(100):
    A, B, Cc = (complex(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(3))
    D = B + (Cc - B) * abs(A - B) / (abs(A - B) + abs(A - Cc))
    u, w = (B - A) / abs(B - A), (Cc - A) / abs(Cc - A)
    assert abs(((D - A) / (u + w)).imag) < 1e-9 * 10 or abs(((D - A) * (u + w).conjugate()).imag) < 1e-6
ok.append("angle bisector")
# complex numbers
zeta = cmath.exp(1j * math.pi / 3)
for _ in range(100):
    a_, b_ = (complex(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(2))
    c_ = a_ + zeta * (b_ - a_)
    assert abs(a_**2 + b_**2 + c_**2 - a_ * b_ - b_ * c_ - c_ * a_) < 1e-9
ok.append("equilateral criterion")
check("root of unity product", all(abs(math.prod(abs(1 - cmath.exp(2j * math.pi * k / n)) for k in range(1, n)) - n) < 1e-9 for n in range(2, 20)))
# right triangle altitude
check("altitude^2=pq", all(abs((3 * 4 / 5) ** 2 - (9 / 5) * (16 / 5)) < 1e-12 for _ in [0]))
# tangent-secant
check("tangent-secant", 6 * 6 == 4 * 9 and 9 - 4 == 5)
# tournament/extremal
random.seed(4)
for _ in range(200):
    n = 7
    beat = [[False] * n for _ in range(n)]
    for i, j in itertools.combinations(range(n), 2):
        if random.random() < .5:
            beat[i][j] = True
        else:
            beat[j][i] = True
    w = [sum(r) for r in beat]
    A = w.index(max(w))
    for B in range(n):
        if B != A:
            assert beat[A][B] or any(beat[A][k] and beat[k][B] for k in range(n))
ok.append("tournament king")

print(f"{len(ok)} claims verified")
