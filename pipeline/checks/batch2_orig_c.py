import itertools, random, math
from fractions import Fraction
from collections import deque
import sympy as sp

N = 0
def ok(cond, msg):
    global N
    assert cond, "FAILED: " + msg
    N += 1

random.seed(7)

# o87: Hamiltonian paths on 3x3 grid from edge-middle cell; none; from centre exists
cells = [(r, c) for r in range(3) for c in range(3)]
def ham(start):
    cnt = 0
    def dfs(p, seen):
        nonlocal cnt
        if len(seen) == 9:
            cnt += 1; return
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            q = (p[0]+dr, p[1]+dc)
            if q in cells and q not in seen:
                dfs(q, seen | {q})
    dfs(start, {start})
    return cnt
ok(ham((0, 1)) == 0, "o87 no path from top-middle")
ok(ham((1, 1)) > 0, "o87 path from centre exists (so start matters)")
ok(sum((r+c) % 2 == 0 for r, c in cells) == 5, "o87 5 corner-coloured cells")

# o88: max number of distinct positive ints with sum 100
def maxcount(total):
    best = 0
    def rec(rem, minv, cnt):
        nonlocal best
        if rem == 0:
            best = max(best, cnt); return
        v = minv
        while v <= rem:
            rec(rem - v, v + 1, cnt + 1)
            v += 1
    # partitions into distinct parts: use DP on count instead
    dp = {(0, 0)}  # (sum, count)
    for v in range(1, total + 1):
        dp |= {(s + v, c + 1) for s, c in dp if s + v <= total}
    return max(c for s, c in dp if s == total)
ok(maxcount(100) == 13, "o88 max count 13")
ok(sum(range(1, 13)) + 22 == 100 and 22 > 12, "o88 construction")
ok(13*14//2 <= 100 < 14*15//2, "o88 bounds")

# o89: no graph on 5 vertices with degree sequence 4,4,3,2,1
pairs5 = list(itertools.combinations(range(5), 2))
seqs = set()
for m in range(1 << 10):
    deg = [0]*5
    for i, (a, b) in enumerate(pairs5):
        if m >> i & 1:
            deg[a] += 1; deg[b] += 1
    seqs.add(tuple(sorted(deg, reverse=True)))
ok((4, 4, 3, 2, 1) not in seqs, "o89 no graph with degrees 4,4,3,2,1")
ok(sum((4, 4, 3, 2, 1)) % 2 == 0, "o89 parity does not rule out")
ok((4, 4, 2, 2, 2) in seqs, "o89 sanity: other sequence realizable")

# o90: change for 50 cents
cnt = {q: sum(1 for d in range(6) for n in range(11) if 25*q + 10*d + 5*n <= 50) for q in range(3)}
ok(cnt == {0: 36, 1: 12, 2: 1}, "o90 case counts")
ok(sum(1 for q in range(3) for d in range(6) for n in range(11) for p in range(51)
       if p + 5*n + 10*d + 25*q == 50) == 49, "o90 total 49")

# o91: sum of n<100 coprime to 100
S91 = [n for n in range(1, 100) if math.gcd(n, 100) == 1]
ok(sum(S91) == 2000 and len(S91) == 40, "o91 sum 2000, 40 terms")
ok(all(100 - n in S91 for n in S91), "o91 closed under n -> 100-n")

# o92: 30 students, 3 clubs each, 10 members per club -> 9 clubs; construction
membership = {(s, 3*(s//10) + j) for s in range(30) for j in range(3)}
clubs = {c for _, c in membership}
ok(len(clubs) == 9, "o92 nine clubs")
ok(all(sum(1 for (s2, c) in membership if s2 == s) == 3 for s in range(30)), "o92 each student in 3 clubs")
ok(all(sum(1 for (s, c2) in membership if c2 == c) == 10 for c in clubs), "o92 each club has 10 members")

# o93: compositions of 10 into parts 1,2,3
def comps(n):
    if n == 0: return 1
    return sum(comps(n - k) for k in (1, 2, 3) if n - k >= 0)
ok([comps(n) for n in range(0, 11)] == [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274], "o93 table")
ok(sum(1 for L in range(1, 11) for t in itertools.product((1, 2, 3), repeat=L) if sum(t) == 10) == 274, "o93 brute force")

# o94: unit-fraction construction
ds = [2, 3, 6]
for n in range(3, 9):
    ok(len(ds) == n and len(set(ds)) == n and sum(Fraction(1, d) for d in ds) == 1, f"o94 n={n}")
    m = ds[-1]
    ds = ds[:-1] + [m + 1, m * (m + 1)]
ok([2, 3, 7, 42] == [2, 3, 6 + 1, 6 * 7] and 43 * 42 == 1806, "o94 examples quoted")
ok(sum(Fraction(1, d) for d in (2, 3, 7, 43, 1806)) == 1, "o94 n=5 example")

# o95: 7x7 board, 1x3 tiles, one hole
from collections import Counter
cells7 = [(i, j) for i in range(1, 8) for j in range(1, 8)]
ok(Counter((i + j) % 3 for i, j in cells7) == {0: 16, 1: 16, 2: 17}, "o95 colour counts i+j")
ok(Counter((i - j) % 3 for i, j in cells7) == {0: 17, 1: 16, 2: 16}, "o95 colour counts i-j")
def tile_hole(hole):
    occ = {hole}
    def go():
        for r in range(1, 8):
            for c in range(1, 8):
                if (r, c) not in occ:
                    for dr, dc in ((0, 1), (1, 0)):
                        t = [(r + k*dr, c + k*dc) for k in range(3)]
                        if all(1 <= x <= 7 and 1 <= y <= 7 and (x, y) not in occ for x, y in t):
                            occ.update(t)
                            if go(): return True
                            occ.difference_update(t)
                    return False
        return True
    return go()
possible = {h for h in cells7 if tile_hole(h)}
ok(possible == {(i, j) for i in (1, 4, 7) for j in (1, 4, 7)}, "o95 exact set of holes")
# explicit constructions from the solution
def check_tiling(tiles, hole):
    cov = [c for t in tiles for c in t]
    return len(cov) == 48 and len(set(cov)) == 48 and set(cells7) - set(cov) == {hole} and all(
        len(t) == 3 and (len({x for x, y in t}) == 1 or len({y for x, y in t}) == 1) for t in tiles)
for b in (1, 4, 7):
    tiles = []
    left = list(range(1, b)); right = list(range(b + 1, 8))
    for blk in (left, right):
        for k in range(0, len(blk), 3):
            tiles.append([(1, y) for y in blk[k:k+3]])
    for col in range(1, 8):
        tiles.append([(r, col) for r in (2, 3, 4)]); tiles.append([(r, col) for r in (5, 6, 7)])
    ok(check_tiling(tiles, (1, b)), f"o95 construction (1,{b})")
pin = []
for c in range(1, 5): pin.append([(r, c) for r in (1, 2, 3)])
for r in range(1, 5): pin.append([(r, c) for c in (5, 6, 7)])
for c in range(4, 8): pin.append([(r, c) for r in (5, 6, 7)])
for r in range(4, 8): pin.append([(r, c) for c in (1, 2, 3)])
ok(check_tiling(pin, (4, 4)), "o95 pinwheel construction")

# o96: max-cut split has the property (all graphs on 5 vertices, random on 8)
def good_split(n, edges, mask):
    for v in range(n):
        same = other = 0
        for a, b in edges:
            if a == v or b == v:
                w = b if a == v else a
                if (mask >> w & 1) == (mask >> v & 1): same += 1
                else: other += 1
        if same > other: return False
    return True
def cut(edges, mask):
    return sum(1 for a, b in edges if (mask >> a & 1) != (mask >> b & 1))
n5 = 5
for m in range(1 << 10):
    edges = [pairs5[i] for i in range(10) if m >> i & 1]
    best = max(range(1 << n5), key=lambda mk: cut(edges, mk))
    ok(good_split(n5, edges, best), f"o96 maxcut good, graph {m}")
for _ in range(200):
    n8 = 8
    edges = [e for e in itertools.combinations(range(n8), 2) if random.random() < 0.5]
    best = max(range(1 << n8), key=lambda mk: cut(edges, mk))
    ok(good_split(n8, edges, best), "o96 random maxcut good")

# o97: min degree >= 3 => even cycle; also verify the proof's three-cycle construction
def longest_path(adj):
    best = []
    def dfs(path):
        nonlocal best
        if len(path) > len(best): best = path[:]
        for w in adj[path[-1]]:
            if w not in path:
                path.append(w); dfs(path); path.pop()
    for s in adj: dfs([s])
    return best
def check_graph97(n, edges):
    adj = {v: set() for v in range(n)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    if min(len(adj[v]) for v in adj) < 3: return False
    P = longest_path(adj)
    assert all(w in P for w in adj[P[0]])
    nb = sorted(P.index(w) for w in adj[P[0]])
    assert nb[0] == 1 and len(nb) >= 3
    i, j = nb[1], nb[2]
    lens = [i + 1, j + 1, j - i + 2]
    assert any(l % 2 == 0 for l in lens) and all(l >= 3 for l in lens)
    return True
cnt97 = 0
for n in (4, 5, 6):
    prs = list(itertools.combinations(range(n), 2))
    for m in range(1 << len(prs)):
        edges = [prs[k] for k in range(len(prs)) if m >> k & 1]
        if check_graph97(n, edges): cnt97 += 1
ok(cnt97 > 0, f"o97 exhaustive n<=6 ({cnt97} graphs with min degree>=3)")
for _ in range(100):
    n = 9
    edges = [e for e in itertools.combinations(range(n), 2) if random.random() < 0.4]
    check_graph97(n, edges)
ok(True, "o97 random n=9")

# o98: 4 unit fractions summing to 1
sols98 = []
for a in range(1, 5):
    for b in range(a, 60):
        for c in range(b, 400):
            rem = 1 - Fraction(1, a) - Fraction(1, b) - Fraction(1, c)
            if rem > 0 and rem.numerator == 1 and rem.denominator >= c:
                sols98.append((a, b, c, rem.denominator))
ok(len(sols98) == 14, "o98 count 14")
ok(sols98 == [(2,3,7,42),(2,3,8,24),(2,3,9,18),(2,3,10,15),(2,3,12,12),(2,4,5,20),(2,4,6,12),(2,4,8,8),(2,5,5,10),(2,6,6,6),(3,3,4,12),(3,3,6,6),(3,4,4,6),(4,4,4,4)], "o98 list matches solution")
ok(Fraction(1, 3) - Fraction(1, 6) == Fraction(1, 6) and Fraction(3, 10) - Fraction(1, 6) == Fraction(2, 15), "o98 b=5,c=6 arithmetic")
ok(Fraction(5, 12) - Fraction(1, 4) == Fraction(1, 6), "o98 (3,4,4,6)")
# brute force over larger range to confirm bounds are not missing anything
cnt = 0
for a in range(1, 8):
    for b in range(a, 100):
        for c in range(b, 100):
            rem = 1 - Fraction(1, a) - Fraction(1, b) - Fraction(1, c)
            if rem > 0 and rem.numerator == 1 and rem.denominator >= c:
                cnt += 1
ok(cnt == 14, "o98 wider search still 14")

# o99: round-table non-adjacent seating game; second player wins for even n >= 4
from functools import lru_cache
def first_wins(n):
    @lru_cache(None)
    def f(mask):
        for i in range(n):
            if not (mask >> i & 1) and not (mask >> ((i + 1) % n) & 1) and not (mask >> ((i - 1) % n) & 1):
                if not f(mask | 1 << i): return True
        return False
    return f(0)
for n in range(4, 23, 2):
    ok(not first_wins(n), f"o99 second player wins n={n}")
# antipodal strategy legal for n=2024 on random symmetric positions
n99 = 2024; h = n99 // 2
for _ in range(200):
    T = set()
    for _ in range(random.randint(0, 300)):
        x = random.randrange(n99)
        if x in T or (x + 1) % n99 in T or (x - 1) % n99 in T or (x + h) % n99 in T: continue
        # build a symmetric position by adding x and x' together
        if all(y not in T for y in (x + h, (x + h + 1) % n99, (x + h - 1) % n99)):
            T |= {x, (x + h) % n99}
    # any legal x for Alice -> x' legal for Bob
    for x in random.sample(range(n99), 50):
        if x in T or (x + 1) % n99 in T or (x - 1) % n99 in T: continue
        xp = (x + h) % n99
        U = T | {x}
        ok(xp not in U and (xp + 1) % n99 not in U and (xp - 1) % n99 not in U, "o99 mirror reply legal")

# o100: Zarankiewicz z(7,7;2,2)=21
rows_all = list(range(1 << 7))
best100 = 0
# DFS over rows (as nondecreasing masks), pairwise popcount(a&b)<=1
def pc(x): return bin(x).count("1")
cands = [m for m in rows_all if pc(m) <= 7]
def search(k, start, chosen, total):
    global best100
    best100 = max(best100, total)
    if k == 7: return
    # simple bound: remaining rows could each add at most max popcount compatible, prune by 7*(7-k)
    if total + 7 * (7 - k) <= best100: return
    for idx in range(start, len(cands)):
        m = cands[idx]
        if total + pc(m) * (7 - k) <= best100: break
        if all(pc(m & c) <= 1 for c in chosen):
            search(k + 1, idx, chosen + [m], total + pc(m))
cands.sort(key=lambda m: -pc(m))
search(0, 0, [], 0)
ok(best100 == 21, "o100 brute force max 21")
T = [[1 if (c - i) % 7 in (0, 1, 3) else 0 for c in range(7)] for i in range(7)]
ok(sum(map(sum, T)) == 21, "o100 construction has 21 ones")
ok(all(sum(T[i][c] & T[j][c] for c in range(7)) == 1 for i in range(7) for j in range(i)), "o100 any two rows share exactly one column")
ok(sum(r * (r - 1) // 2 for r in [4,3,3,3,3,3,3]) == 24, "o100 24 for 22 ones")
ok({(b - a) % 7 for a in (0, 1, 3) for b in (0, 1, 3) if a != b} == {1, 2, 3, 4, 5, 6}, "o100 difference set")

# o101: Erdos-Szekeres, 10 = 3^2+1 -> monotone subsequence of length 4
def ab(perm):
    n = len(perm)
    a = [1]*n; b = [1]*n
    for j in range(n):
        for i in range(j):
            if perm[i] < perm[j]: a[j] = max(a[j], a[i] + 1)
            else: b[j] = max(b[j], b[i] + 1)
    return a, b
for perm in itertools.permutations(range(1, 8)):
    a, b = ab(perm)
    assert len(set(zip(a, b))) == 7
ok(True, "o101 pairs distinct (all perms of 7)")
for _ in range(20000):
    p = random.sample(range(1, 11), 10)
    a, b = ab(p)
    assert len(set(zip(a, b))) == 10 and (max(a) >= 4 or max(b) >= 4)
ok(True, "o101 random perms of 10")
# exhaustive check of the statement for n=10 via LIS/LDS DP on all 10! would be slow; do all perms of 10 with first element fixed set sampling
import bisect
def lis(seq):
    t = []
    for x in seq:
        i = bisect.bisect_left(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)
allok = True
for perm in itertools.permutations(range(1, 10)):
    for ins in range(0, 10, 3):
        p = list(perm[:ins]) + [10] + list(perm[ins:])
        if lis(p) < 4 and lis([-x for x in p]) < 4:
            allok = False
ok(allok, "o101 many perms of 1..10 have monotone subsequence of length 4")
ok(any(lis(p) < 4 and lis([-x for x in p]) < 4 for p in [[3,2,1,6,5,4,9,8,7]]), "o101 sharpness: 9 elements can avoid length 4")

# __APPEND__
print(N, "checks passed")
