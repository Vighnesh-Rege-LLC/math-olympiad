#!/usr/bin/env python3
"""Code checks for the computable claims in the pilot problems."""
import itertools, math, random
from fractions import Fraction
import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


# originals
check("o01 pigeonhole", all(len({v % 5 for v in s}) < 6 for s in itertools.combinations(range(30), 6)))
check("o04 7^2025", pow(7, 2025, 10) == 7)
check("o05 abs", [n for n in range(-100, 100) if abs(n - 3) + abs(n + 2) == 9] == [-4, 5])
check("o06 min", min(x + 9 / x for x in [i / 1000 for i in range(1, 20000)]) >= 6 - 1e-9)
check("o07 tele", sum(Fraction(1, k * (k + 1)) for k in range(1, 100)) == Fraction(99, 100))
check("o08 gcd", all(math.gcd(2 * n + 1, 3 * n + 2) == 1 for n in range(-500, 500)))
# o09: 6x6 minus opposite corners, exhaustive tiling search
def tileable(cells):
    cells = set(cells)
    def go(rem):
        if not rem:
            return True
        c = min(rem)
        for d in ((0, 1), (1, 0)):
            n = (c[0] + d[0], c[1] + d[1])
            if n in rem and go(rem - {c, n}):
                return True
        return False
    return go(frozenset(cells))
board = {(i, j) for i in range(6) for j in range(6)}
check("o09 domino", not tileable(board - {(0, 0), (5, 5)}))
# o10 invariant simulation
random.seed(1)
for _ in range(50):
    nums = list(range(1, 11))
    while len(nums) > 1:
        a, b = random.sample(range(len(nums)), 2)
        x, y = nums[a], nums[b]
        nums = [v for i, v in enumerate(nums) if i not in (a, b)] + [x + y - 1]
    assert nums == [46]
ok.append("o10 invariant")
a = 1
for _ in range(9):
    a = 2 * a + 1
check("o12 recurrence", a == 1023)
x, k = sp.symbols("x k")
check("o13 vieta", sp.solve(sp.Eq(25 - 2 * k, 13), k) == [6])
sol = [(x_, y_) for x_ in range(1, 200) for y_ in range(1, 200) if x_ * y_ - 3 * x_ - 2 * y_ == 0]
check("o14 dioph", sorted(sol) == [(3, 9), (4, 6), (5, 5), (8, 4)])
check("o15 n!>2^n", all(math.factorial(n) > 2**n for n in range(4, 60)) and math.factorial(3) <= 8)
check("o19 abc=a+b+c", sorted((a, b, c) for a in range(1, 60) for b in range(a, 60) for c in range(b, 200) if a * b * c == a + b + c) == [(1, 2, 3)])
check("o21 count", sum(1 for a in range(6) for b in range(6) for c in range(6) if a + b + c == 10) == 21)
check("o22 (1+i)^20", (1 + 1j) ** 20 == -1024)
check("o23 cos", Fraction(49 + 64 - 81, 2 * 7 * 8) == Fraction(2, 7))
check("o25 tangent", 12**2 == 8 * 18)
check("o27 CS", abs(1 / .5 + 4 / 1 + 9 / 1.5 - 12) < 1e-12 and min(1 / a_ + 4 / b_ + 9 / (3 - a_ - b_) for a_ in [i / 40 for i in range(1, 119)] for b_ in [j / 40 for j in range(1, 119)] if a_ + b_ < 3) >= 12 - 1e-9)
check("o28 descent small", not any(x_**3 + 2 * y_**3 == 4 * z_**3 for x_ in range(1, 80) for y_ in range(1, 80) for z_ in range(1, 80)))
check("o30 E distinct", Fraction(6) * (1 - Fraction(5, 6) ** 3) == Fraction(91, 36)
      and Fraction(sum(len(set(t)) for t in itertools.product(range(6), repeat=3)), 216) == Fraction(91, 36))
check("o31 strings", sum(1 for t in itertools.product((0, 1), repeat=8) if "11" not in "".join(map(str, t))) == 55)
check("o32 P(4)", sp.expand(sp.Symbol("x") + (sp.Symbol("x") - 1) * (sp.Symbol("x") - 2) * (sp.Symbol("x") - 3)).subs(sp.Symbol("x"), 4) == 10)
check("o33 mod5", all((n * n + n + 1) % 5 != 0 for n in range(5)))
check("o34 midpoint", all(any((p[0] + q[0]) % 2 == 0 and (p[1] + q[1]) % 2 == 0 for p, q in itertools.combinations(s, 2)) for s in itertools.combinations([(i, j) for i in range(2) for j in range(4)], 5)))
signs = [1, -1, -1, 1] * 506
check("o35 signs", sum(s * (i + 1) for i, s in enumerate(signs)) == 0 and len(signs) == 2024)
check("o36 primes", [p for p in sp.primerange(2, 3000) if sp.isprime(8 * p * p + 1)] == [3])

# MathNet set
N = 10 * (10**132 - 1)
check("m01", N % 2010 == 0 and set(str(N)) == {"9", "0"})
def P(colors):
    n = len(colors)
    pr = Fraction(1)
    for i in range(n):
        u, v = colors[i], colors[(i + 1) % n]
        pr *= 2 if (u, v) == (1, 1) else Fraction(1, 2) if (u, v) == (0, 0) else 1
    return pr
check("m02", all(P(c) == Fraction(2) ** (sum(c) - (len(c) - sum(c))) for n in range(3, 11) for c in itertools.product((0, 1), repeat=n)))
check("m05", all(math.isqrt(2 * a * b + 1) ** 2 == 2 * a * b + 1 for a in range(1, 400) for b in range(1, 400) if a != b and (a * a + b * b + 1) % (2 * a * b + 1) == 0))
check("m06", [(a, b, c) for a in range(0, 13) for b in range(0, a + 1) for c in range(0, b + 1) if a**3 + 9 * b * b + 9 * c + 7 == 1997] == [(10, 10, 10)])
check("m07 eq", 4 * 2011 == 8044)
def rects(m, n):
    return sum(1 for a in range(m + 1) for b in range(a + 1, m + 1) for c in range(n + 1) for d in range(c + 1, n + 1) if (b - a) % 2 and (d - c) % 2)
check("m10", sorted((m, n) for m in range(1, 40) for n in range(1, 40) if rects(m, n) == 225) == [(1, 29), (5, 9), (9, 5), (29, 1)])
check("m11 bound", 44**2 < 2009 <= 45**2 and 2009 - 45 == 1964 <= 45 * 44)
xx, yy = sp.symbols("x y")
a_, b_ = sp.symbols("a b")
M = sp.solve([a_ + b_ - 2 * xx, a_ + 2 * b_ - 2 * yy], [a_, b_])
expr = sp.expand((M[b_] - M[a_]) ** 2 + (2 * M[b_] - M[a_]) ** 2 - 16)
check("m14 locus", sp.simplify(expr - 4 * (25 * xx**2 - 36 * xx * yy + 13 * yy**2 - 4)) == 0)
# m15: min girls on a 30-cycle with no child having two boy neighbours
def min_girls(n):
    best = n
    for mask in range(1 << n):
        s = [(mask >> i) & 1 for i in range(n)]  # 1 = boy
        if any(s[(i - 1) % n] and s[(i + 1) % n] for i in range(n)):
            continue
        best = min(best, n - sum(s))
    return best
# DP for n=30 (transfer on last two cells, cyclic)
def dp_min_girls(n):
    best = n
    for first in itertools.product((0, 1), repeat=2):
        f = {(first[0], first[1]): first[0] + first[1]}
        for _ in range(2, n):
            g = {}
            for (a, b), cnt in f.items():
                for c in (0, 1):
                    if a and c:
                        continue
                    key = (b, c)
                    g[key] = max(g.get(key, -1), cnt + c)
            f = g
        for (a, b), cnt in f.items():
            if (a and first[0]) or (b and first[1]):
                continue
            best = min(best, n - cnt)
    return best
check("m15 n=30 -> 16", dp_min_girls(30) == 16)
check("m15 dp==brute", all(dp_min_girls(n) == min_girls(n) for n in (6, 8, 10, 12)))
def gcds(t):
    return sorted(math.gcd(a, b) for a, b in itertools.combinations(t, 2))
check("m17 example", gcds((4, 15, 70, 84)) == [1, 2, 3, 4, 5, 14])
best = None
for t in itertools.combinations(range(1, 160), 4):
    g = gcds(t)
    if g[:5] == [1, 2, 3, 4, 5] and g[5] > 5:
        best = g[5] if best is None else min(best, g[5])
check("m17 minimum search", best == 14)
def best_odd_starts(order):
    page, cnt = 1, 0
    for L in order:
        cnt += page % 2
        page += L
    return cnt
random.seed(2)
mx = max(best_odd_starts(random.sample(range(1, 31), 30)) for _ in range(20000))
check("m18", mx <= 23 and best_odd_starts(list(range(2, 31, 2)) + list(range(1, 31, 2))) == 23)
def small_best(n):
    return max(best_odd_starts(p) for p in itertools.permutations(range(1, n + 1)))
check("m18 analog n=8", small_best(8) == 6)
# m20
def works(a, p):
    return (a**p - a) % p == 0 and math.isqrt((a**p - a) // p) ** 2 == (a**p - a) // p and (a**p - a) // p >= 4
check("m20", not any(works(a, p) for a in range(1, 9) for p in sp.primerange(2, 60)) and works(9, 2))
# m21
t = sp.Symbol("t")
bad = []
for k in range(-300, 301):
    f = sp.Poly(t**4 + 2 * t + k, t)
    rr = [r for r in sp.roots(f, filter="Q") if r.is_rational]
    if not rr and not f.is_irreducible:
        bad.append(k)
check("m21", not bad)
# m22 sample
from fractions import Fraction as F
check("m22 var", sum((i - F(5 + 1, 2)) ** 2 for i in range(1, 6)) == F(5 * 24, 12))
random.seed(5)
for _ in range(500):
    a_, b_, c_ = (random.uniform(0.01, 8) for _ in range(3))
    s = a_ + b_ + c_
    a_, b_, c_ = 6 * a_ / s, 6 * b_ / s, 6 * c_ / s
    assert a_ / (a_ + 1) + b_ / (b_ + 1) + c_ / (c_ + 1) <= 2 + 1e-9
    x, y, z = (random.uniform(0.01, 8) for _ in range(3))
    lhs = (x + y + z) * (1 / x + 1 / y + 1 / z)
    rhs = 4 * (x / (x * y + 1) + y / (y * z + 1) + z / (z * x + 1)) ** 2
    assert lhs >= rhs - 1e-9
ok.append("m19/m23 random")
# m24: ring-area claim numerically
for _ in range(2000):
    A = complex(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
    B = complex(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
    d = abs(A - B)
    ds = [abs(A + (B - A) * s / 1000) for s in range(1001)]
    assert max(ds) ** 2 - min(ds) ** 2 >= d * d / 4 - 1e-3
ok.append("m24 ring claim")
print(f"{len(ok)} problem checks passed")
