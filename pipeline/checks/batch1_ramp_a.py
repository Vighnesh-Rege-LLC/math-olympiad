import itertools, random, math
from fractions import Fraction
from collections import deque
import sympy as sp

N = 0
def ok(cond, msg):
    global N
    assert cond, "FAILED: " + msg
    N += 1

random.seed(1)

# o37: subset sums bound and random sanity
ok(sum(range(90, 100)) == 945 < 2**10 - 1, "o37 bound")
for _ in range(300):
    S = random.sample(range(1, 100), 10)
    seen = {}
    found = False
    for r in range(1, 11):
        for c in itertools.combinations(S, r):
            s = sum(c)
            if s in seen and not (set(seen[s]) & set(c)):
                found = True; break
            seen.setdefault(s, c)
        if found: break
    # direct disjoint search over distinct equal-sum subsets
    subs = {}
    for m in range(1, 1 << 10):
        subs.setdefault(sum(S[i] for i in range(10) if m >> i & 1), []).append(m)
    d = any(a & b == 0 for v in subs.values() for a, b in itertools.combinations(v, 2))
    ok(d, "o37 disjoint equal-sum subsets exist")

# o38: max subset of 1..20 with no two differing by 3
best = 0
for m in range(1 << 20):
    if m & (m >> 3) == 0:
        best = max(best, bin(m).count("1"))
ok(best == 11, "o38 max 11 -> answer 12")

# o39: product invariant
for _ in range(200):
    b = list(range(1, 11))
    while len(b) > 1:
        i, j = random.sample(range(len(b)), 2)
        x, y = b[i], b[j]
        b = [v for k, v in enumerate(b) if k not in (i, j)] + [x * y + x + y]
    ok(b[0] == math.factorial(11) - 1 == 39916799, "o39 final value")

# o40: chameleons BFS
start = (6, 9, 13)
seen = {start}; dq = deque([start])
while dq:
    s = dq.popleft()
    for i, j in ((0, 1), (0, 2), (1, 2)):
        if s[i] > 0 and s[j] > 0:
            k = 3 - i - j
            t = list(s); t[i] -= 1; t[j] -= 1; t[k] += 2; t = tuple(t)
            if t not in seen: seen.add(t); dq.append(t)
mono = {(28, 0, 0): "red", (0, 28, 0): "green", (0, 0, 28): "blue"}
reach = [mono[s] for s in mono if s in seen]
ok(reach == ["blue"], "o40 only blue reachable")
# explicit sequence
s = [6, 9, 13]
for _ in range(6): s[0] -= 1; s[1] -= 1; s[2] += 2
ok(s == [0, 3, 25], "o40 step 1")
s[1] -= 1; s[2] -= 1; s[0] += 2
ok(s == [2, 2, 24], "o40 step 2")
for _ in range(2): s[0] -= 1; s[1] -= 1; s[2] += 2
ok(s == [0, 0, 28], "o40 final")

# o41: strengthened bound
tot = Fraction(0)
for n in range(1, 400):
    tot += Fraction(1, n * n)
    ok(tot <= 2 - Fraction(1, n), "o41 n=%d" % n)

# o42: L-tromino tiling by the recursive construction
def tile(size, hole, ox=0, oy=0, out=None):
    if out is None: out = []
    if size == 1: return out
    h = size // 2
    quads = [(ox, oy), (ox + h, oy), (ox, oy + h), (ox + h, oy + h)]
    cells = []
    holes = []
    for (qx, qy) in quads:
        cx = qx + h - 1 if qx == ox else qx
        cy = qy + h - 1 if qy == oy else qy
        inside = qx <= hole[0] < qx + h and qy <= hole[1] < qy + h
        if inside: holes.append(hole)
        else:
            holes.append((cx, cy)); cells.append((cx, cy))
    out.append(cells)
    for (qx, qy), hl in zip(quads, holes):
        tile(h, hl, qx, qy, out)
    return out
def check_tiling(n, hole):
    size = 2 ** n
    L = tile(size, hole)
    cov = set()
    for tr in L:
        pass
    # rebuild: tile returns tromino cell lists only for the central pieces; recount
    return L
def full_tiling(size, hole, ox=0, oy=0):
    if size == 1: return []
    h = size // 2
    quads = [(ox, oy), (ox + h, oy), (ox, oy + h), (ox + h, oy + h)]
    res = []; cells = []; holes = []
    for (qx, qy) in quads:
        cx = qx + h - 1 if qx == ox else qx
        cy = qy + h - 1 if qy == oy else qy
        if qx <= hole[0] < qx + h and qy <= hole[1] < qy + h: holes.append(hole)
        else: holes.append((cx, cy)); cells.append((cx, cy))
    res.append(tuple(cells))
    for (qx, qy), hl in zip(quads, holes):
        res += full_tiling(h, hl, qx, qy)
    return res
for n in range(1, 5):
    size = 2 ** n
    holes_ = [(x, y) for x in range(size) for y in range(size)] if n <= 3 else random.sample([(x, y) for x in range(size) for y in range(size)], 40)
    for hole in holes_:
        T = full_tiling(size, hole)
        allc = [c for t in T for c in t]
        ok(len(allc) == len(set(allc)) == size * size - 1 and hole not in allc, "o42 cover n=%d" % n)
        for t in T:
            xs = sorted(set(c[0] for c in t)); ys = sorted(set(c[1] for c in t))
            if not (len(t) == 3 and len(xs) == 2 and len(ys) == 2 and xs[1] - xs[0] == 1 and ys[1] - ys[0] == 1):
                ok(False, "o42 L shape")
ok(True, "o42 L shapes")

# o43: circle of means has only constant solutions
for n in range(3, 10):
    M = sp.zeros(n, n)
    for i in range(n):
        M[i, i] = 2; M[i, (i - 1) % n] -= 1; M[i, (i + 1) % n] -= 1
    ns = M.nullspace()
    ok(len(ns) == 1 and all(v == ns[0][0] for v in ns[0]), "o43 n=%d" % n)

# o44: tournament king
def has_king(n, beat):
    wins = [sum(beat[a][b] for b in range(n)) for a in range(n)]
    A = max(range(n), key=lambda a: wins[a])
    for B in range(n):
        if B == A or beat[A][B]: continue
        if not any(beat[A][C] and beat[C][B] for C in range(n)): return False
    return True
for n in range(2, 6):
    pairs = list(itertools.combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        beat = [[0] * n for _ in range(n)]
        for k, (a, b) in enumerate(pairs):
            if bits >> k & 1: beat[a][b] = 1
            else: beat[b][a] = 1
        ok(has_king(n, beat), "o44 n=%d" % n) if bits % 37 == 0 else (has_king(n, beat) or ok(False, "o44"))
for _ in range(500):
    n = 9; beat = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if random.random() < .5: beat[a][b] = 1
            else: beat[b][a] = 1
    ok(has_king(n, beat), "o44 random")

# o45: x^2+y^2+z^2 = x^2 y^2
sol = [(x, y, z) for x in range(-60, 61) for y in range(-60, 61) for z in range(-60, 61) if x*x + y*y + z*z == x*x*y*y]
ok(sol == [(0, 0, 0)], "o45 only zero")
sq = {(v * v) % 4 for v in range(4)}
ok(sq == {0, 1}, "o45 squares mod 4")
# mod 4 case analysis from the solution (k=0 case)
for xx in (0, 1):
    for yy in (0, 1):
        for zz in (0, 1):
            if (xx + yy + zz) % 4 == (xx * yy) % 4:
                ok(xx == 0 and yy == 0 and zz == 0, "o45 residue case (x,y,z squares mod4)")

# o46: a^2+b^2+1 = 3ab
u = [1, 1]
while len(u) < 30: u.append(3 * u[-1] - u[-2])
fam = set()
for n in range(len(u) - 1):
    fam.add((u[n], u[n + 1])); fam.add((u[n + 1], u[n]))
LIM = 20000
brute = set()
for a in range(1, LIM):
    # b^2 - 3ab + a^2+1 = 0 -> disc = 5a^2-4
    d = 5 * a * a - 4
    r = math.isqrt(d)
    if r * r == d:
        for sgn in (1, -1):
            num = 3 * a + sgn * r
            if num % 2 == 0 and num > 0 and num // 2 < LIM:
                brute.add((a, num // 2))
ok({p for p in fam if max(p) < LIM} == brute, "o46 family equals brute force")
ok(u[:8] == [1, 1, 2, 5, 13, 34, 89, 233], "o46 sequence")
ok(all(a*a + b*b + 1 == 3*a*b for a, b in fam), "o46 family solves")

# o47: lamps
for n in (3, 5, 7):
    seen = {0}; dq = deque([0])
    while dq:
        s = dq.popleft()
        for i, j in itertools.combinations(range(n), 2):
            t = s ^ (1 << i) ^ (1 << j)
            if t not in seen: seen.add(t); dq.append(t)
    ok(max(bin(s).count("1") for s in seen) == n - 1, "o47 n=%d" % n)
    ok(all(bin(s).count("1") % 2 == 0 for s in seen), "o47 parity")

# o48: factorial remainder
ok(sum(math.factorial(k) for k in range(1, 101)) % 60 == 33, "o48")
ok(all(math.factorial(k) % 60 == 0 for k in range(5, 101)), "o48 tail")

# o49: sums of three cubes mod 9, and 2021
cubes = {pow(v, 3, 9) for v in range(9)}
ok(cubes == {0, 1, 8}, "o49 cubes mod 9")
sums = {(a + b + c) % 9 for a in cubes for b in cubes for c in cubes}
ok(sums == {0, 1, 2, 3, 6, 7, 8}, "o49 sums")
ok(2021 % 9 == 5 and 5 not in sums, "o49 2021")
ok(all((x**3 + y**3 + z**3) != 2021 for x in range(-40, 41) for y in range(-40, 41) for z in range(-40, 41)), "o49 brute")

# o50: x^2 - 8 floor(x) + 5 = 0
sols = []
for n in range(-300, 300):
    Nn = 8 * n - 5
    if Nn < 0: continue
    r = math.isqrt(Nn)
    # positive root sqrt(Nn) in [n, n+1)
    if n * n <= Nn < (n + 1) ** 2: sols.append(("+", n, Nn))
    # negative root -sqrt(Nn) in [n, n+1)
    if Nn <= n * n and Nn > (n + 1) ** 2 and False: sols.append(("-", n, Nn))
ok([s[2] for s in sols] == [3, 35, 43, 51] and [s[1] for s in sols] == [1, 5, 6, 7], "o50 solutions")
for (_, n, Nn) in sols:
    x = sp.sqrt(Nn)
    ok(sp.floor(x) == n and x**2 - 8*n + 5 == 0, "o50 verify")
# fine numeric scan for any missed roots
cnt = 0
prev = None
for i in range(-20000, 20001):
    x = i / 1000
    g = x * x - 8 * math.floor(x) + 5
    # roots occur where g crosses zero within a continuity interval; check sign change inside intervals
    if prev is not None and math.floor(x) == math.floor(x - .001) and (g == 0 or prev[1] * g < 0): cnt += 1
    prev = (x, g)
ok(cnt == 4, "o50 numeric scan finds 4 roots (got %d)" % cnt)

# o51: bugs on boards
def can_shift(R, C):
    cells = [(r, c) for r in range(R) for c in range(C)]
    idx = {c: i for i, c in enumerate(cells)}
    nb = [[idx[(r + dr, c + dc)] for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (r + dr, c + dc) in idx] for r, c in cells]
    used = [False] * len(cells)
    def go(i):
        if i == len(cells): return True
        for j in nb[i]:
            if not used[j]:
                used[j] = True
                if go(i + 1): return True
                used[j] = False
        return False
    return go(0)
ok(not can_shift(3, 3) and not can_shift(3, 5) and can_shift(4, 4) and can_shift(2, 3), "o51 small boards")
ok(sum((r + c) % 2 == 0 for r in range(5) for c in range(5)) == 13, "o51 13 vs 12")

# o52: 1x4 strips on 10x10
cnt = [0] * 4
for i in range(1, 11):
    for j in range(1, 11): cnt[(i + j) % 4] += 1
ok(sorted(cnt) == [24, 25, 25, 26] and cnt[0] == 25 and cnt[1] == 24 and cnt[2] == 25 and cnt[3] == 26, "o52 color counts %s" % cnt)
def tilings_I(R, C):
    # broken-profile DP: state = set of occupied cells ahead (bitmask over next 3R+... cells)
    total = R * C
    from functools import lru_cache
    @lru_cache(None)
    def go(pos, mask):
        # mask bit k = cell pos+k occupied
        while pos < total and mask & 1:
            mask >>= 1; pos += 1
        if pos == total: return 1
        r, c = divmod(pos, C)
        res = 0
        h = 0b1111; v = 1 | 1 << C | 1 << 2 * C | 1 << 3 * C
        if c + 4 <= C and not mask & h:
            res += go(pos, mask | h)
        if r + 4 <= R and not mask & v:
            res += go(pos, mask | v)
        return res
    return go(0, 0)
ok(tilings_I(4, 4) == 2 and tilings_I(8, 8) > 0, "o52 small boards tile")
ok(tilings_I(10, 10) == 0, "o52 10x10 has no tiling (exhaustive)")

# o53: symmetry sum
x = sp.symbols('x')
f = lambda t: 4**t / (4**t + 2)
y = sp.symbols('y', positive=True)
ok(sp.simplify(y/(y+2) + (4/y)/((4/y)+2)) == 1, "o53 identity (y=4^x, 4^(1-x)=4/y)")
val = sum(sp.N(f(sp.Rational(k, 100)), 50) for k in range(1, 100))
ok(abs(val - sp.Rational(99, 2)) < sp.Float(10) ** -40, "o53 numeric sum 99/2")

# o54: no element twice another in 1..n
def maxset_formula(n):
    tot = 0
    m = 1
    while m <= n:
        L = 0; v = m
        while v <= n: L += 1; v *= 2
        tot += (L + 1) // 2; m += 2
    return tot
for n in (10, 16, 20, 22):
    best = 0
    for mk in range(1 << n):
        # bit i represents i+1; bad if i+1 and 2(i+1) both in set
        good = True
        for i in range(1, n // 2 + 1):
            if mk >> (i - 1) & 1 and mk >> (2 * i - 1) & 1: good = False; break
        if good: best = max(best, bin(mk).count("1"))
    ok(best == maxset_formula(n), "o54 brute n=%d" % n)
ok(maxset_formula(100) == 67, "o54 n=100")
from collections import Counter
Ls = Counter()
for m in range(1, 101, 2):
    L = 0; v = m
    while v <= 100: L += 1; v *= 2
    Ls[L] += 1
ok(dict(Ls) == {7: 1, 6: 1, 5: 1, 4: 3, 3: 7, 2: 12, 1: 25}, "o54 chain table")

# o55: CRT construction
for n in range(1, 9):
    ps = list(sp.primerange(2, 60))[:n]
    mods = [p * p for p in ps]; res = [(-i) % (p * p) for i, p in zip(range(1, n + 1), ps)]
    from sympy.ntheory.modular import solve_congruence
    r, M = solve_congruence(*zip(res, mods))
    ok(all((r + i) % (ps[i - 1] ** 2) == 0 for i in range(1, n + 1)), "o55 n=%d" % n)

# o56: Steiner triple system on 15 points
pts = list(range(1, 16))
triples = {frozenset((a, b, a ^ b)) for a in pts for b in pts if a != b}
ok(len(triples) == 35, "o56 35 triples")
ok(all(sum(1 for t in triples if a in t and b in t) == 1 for a, b in itertools.combinations(pts, 2)), "o56 each pair once")
ok(all(sum(1 for t in triples if a in t) == 7 for a in pts), "o56 7 per student")

# o57: Mantel
for n in range(2, 7):
    pairs = list(itertools.combinations(range(n), 2))
    best = 0
    for mk in range(1 << len(pairs)):
        E = [pairs[k] for k in range(len(pairs)) if mk >> k & 1]
        if len(E) <= best: continue
        S = set(E)
        if any((a, b) in S and (b, c) in S and (a, c) in S for a, b, c in itertools.combinations(range(n), 3)): continue
        best = len(E)
    ok(best == n * n // 4, "o57 n=%d" % n)

# o58: domino tilings of 3 x n
def dominoes_3xn(n):
    from functools import lru_cache
    @lru_cache(None)
    def go(col, mask):  # mask: cells of this column already filled (3 bits)
        if col == n: return 1 if mask == 0 else 0
        res = 0
        def fill(row, cur, nxt):
            nonlocal res
            if row == 3:
                res += go(col + 1, nxt); return
            if cur >> row & 1: fill(row + 1, cur, nxt); return
            # horizontal
            fill(row + 1, cur | 1 << row, nxt | 1 << row)
            # vertical
            if row < 2 and not cur >> (row + 1) & 1:
                fill(row + 2, cur | 3 << row, nxt)
        fill(0, mask, 0)
        return res
    return go(0, 0)
ok(dominoes_3xn(12) == 2131, "o58 3x12")
a = {0: 1}; b = {0: 0, 1: 1}
for n in range(1, 13):
    if n >= 2: b[n] = a[n - 1] + b[n - 2]
    a[n] = a[n - 2] + 2 * b[n - 1] if n >= 2 else 0
    ok(a[n] == dominoes_3xn(n), "o58 recursion a_%d" % n)
ok(a[12] == 2131 and b[11] == 780 and b[9] == 209, "o58 table")

# o59: derangements
D = {1: 0, 2: 1}
for n in range(3, 9): D[n] = (n - 1) * (D[n - 1] + D[n - 2])
for n in range(1, 9):
    c = sum(all(p[i] != i for i in range(n)) for p in itertools.permutations(range(n)))
    ok(c == D[n], "o59 n=%d" % n)
ok(D[7] == 1854 and D[6] == 265 and D[5] == 44, "o59 values")

# o60: Ramsey R(3,3)=6
def mono_triangle(n, col):
    return any(col[(a, b)] == col[(a, c)] == col[(b, c)] for a, b, c in itertools.combinations(range(n), 3))
pairs6 = list(itertools.combinations(range(6), 2))
ok(all(mono_triangle(6, dict(zip(pairs6, [(m >> k) & 1 for k in range(15)]))) for m in range(1 << 15)), "o60 every 2-coloring of K6")
pent = {p: 0 for p in itertools.combinations(range(5), 2)}
for a, b in pent:
    pent[(a, b)] = 1 if (b - a) % 5 in (1, 4) else 0
ok(not mono_triangle(5, pent), "o60 K5 counterexample (5-cycle)")

# o61: connectivity threshold
def connected(n, E):
    adj = {i: set() for i in range(n)}
    for a, b in E: adj[a].add(b); adj[b].add(a)
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen) == n
for n in range(3, 7):
    pairs = list(itertools.combinations(range(n), 2))
    maxdis = 0
    for mk in range(1 << len(pairs)):
        E = [pairs[k] for k in range(len(pairs)) if mk >> k & 1]
        if len(E) > maxdis and not connected(n, E): maxdis = len(E)
    ok(maxdis == math.comb(n - 1, 2), "o61 n=%d" % n)
mx = max(math.comb(k, 2) + math.comb(10 - k, 2) for k in range(1, 10))
ok(mx == 36 and math.comb(9, 2) == 36, "o61 n=10")
ok(all((k - 1) * (10 - k - 1) >= 0 for k in range(1, 10)), "o61 product lemma")

print(N, "checks passed")
