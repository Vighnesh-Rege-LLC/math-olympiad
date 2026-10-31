#!/usr/bin/env python3
"""Code checks for batch1-hard-a (m25-m49, adapted from MathNet)."""
import itertools, math, random
from fractions import Fraction
from functools import lru_cache
import sympy as sp

ok = []


def check(name, cond):
    assert cond, name
    ok.append(name)


random.seed(12345)

# ---------------- m25 (0gs6) sub-divisors ----------------
def blocks(n):
    s = str(n)
    b = len(s)
    return {int(s[i:j]) for i in range(b) for j in range(i + 1, b + 1)}


def has_subdiv(n, d):
    return any(v % d == 0 for v in blocks(n))


good = True
for d in range(1, 60):
    if math.gcd(d, 10) == 1:
        for _ in range(60):
            L = d + random.randint(0, 5)
            n = random.randint(10 ** (L - 1), 10**L - 1)
            good &= has_subdiv(n, d)
    else:
        good &= not any(has_subdiv(int("1" * L), d) for L in range(1, 40))
check("m25 coprime d always sub-divisor of long numbers; repunits avoid 2,5", good)
A3 = [n for n in range(1, 100000) if not has_subdiv(n, 3)]
check("m25 A_3 contains only numbers with < 3 digits", max(A3) < 100)
check("m25 7-digit numbers all have sub-divisor 7 (sample block)", all(has_subdiv(n, 7) for n in range(10**6, 10**6 + 150000)))
check("m25 example 143", sorted(x for x in range(1, 200) if any(v % x == 0 for v in blocks(143))) == [1, 2, 3, 4, 7, 11, 13, 14, 43, 143])

# ---------------- m26 (017v) rooks with distinct colours ----------------
def graceful_exists(n):
    for f in itertools.permutations(range(1, n + 1)):
        if len({abs(f[k] - (k + 1)) for k in range(n)}) == n:
            assert sum((k + 1) * f[k] for k in range(n)) * 12 == n * (2 * n * n + 9 * n + 1)
            return True
    return False


check("m26 existence only for n = 0,1 mod 4 (n<=9)", all(graceful_exists(n) == (n % 4 in (0, 1)) for n in range(1, 10)))
check("m26 integrality", all(((n * (2 * n * n + 9 * n + 1)) % 12 == 0) == (n % 4 in (0, 1)) for n in range(1, 500)))

# ---------------- m27 (013f) fleas ----------------
start = (1, 2, 3, 4, 5)  # positions of A..E
seen = {start}
frontier = [start]
while frontier:
    nxt = []
    for st in frontier:
        occ = set(st)
        for i in range(5):
            for dlt in (5, -5):
                q = (st[i] - 1 + dlt) % 13 + 1
                if q not in occ:
                    ns = st[:i] + (q,) + st[i + 1:]
                    if ns not in seen:
                        seen.add(ns)
                        nxt.append(ns)
    frontier = nxt
finals = set()
for st in seen:
    if set(st) == {1, 2, 3, 4, 5}:
        word = [None] * 5
        for i, p in enumerate(st):
            word[p - 1] = "ABCDE"[i]
        finals.add("".join(word))
check("m27 reachable orders are the 5 rotations", finals == {"ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD"})
# explicit move list in t-coordinates (segment s <-> t with s = 1 + 5t mod 13)
seg = lambda t: (1 + 5 * t) % 13 or 13
pos = {"A": 0, "C": 3, "E": 6, "B": 8, "D": 11}
check("m27 t-coordinates", all(seg(pos[f]) == "ABCDE".index(f) + 1 for f in "ABCDE"))
moves = [("A", 1), ("A", 2), ("D", 12), ("D", 0), ("B", 9), ("B", 10), ("E", 7), ("E", 8), ("B", 11), ("C", 4), ("C", 5), ("C", 6), ("A", 3)]
valid = True
for f, t in moves:
    valid &= (t - pos[f]) % 13 in (1, 12) and t not in pos.values()
    pos[f] = t
word = "".join(sorted("ABCDE", key=lambda f: seg(pos[f])))
check("m27 explicit sequence gives DEABC", valid and word == "DEABC")

# ---------------- m28 (0113) king ----------------
def adj_pairs(r, c):
    cells = [(i, j) for i in range(r) for j in range(c)]
    return sum(1 for a, b in itertools.combinations(cells, 2) if max(abs(a[0] - b[0]), abs(a[1] - b[1])) == 1)


check("m28 8x8 has 210 adjacent pairs", adj_pairs(8, 8) == 210)


def king_tour_exists(r, c):
    cells = [(i, j) for i in range(r) for j in range(c)]
    nb = {x: [y for y in cells if y != x and max(abs(x[0] - y[0]), abs(x[1] - y[1])) == 1] for x in cells}
    N = len(cells)

    def go(cur, vis, cnt):
        if cnt == N:
            return True
        for y in nb[cur]:
            if y in vis:
                continue
            if cnt >= 2 and sum(1 for z in nb[y] if z in vis) % 2:
                continue
            vis.add(y)
            if go(y, vis, cnt + 1):
                return True
            vis.remove(y)
        return False

    return any(go(s, {s}, 1) for s in cells)


check("m28 small boards with even pair count have no tour", all(adj_pairs(r, c) % 2 == 0 and not king_tour_exists(r, c) for r, c in [(3, 3), (4, 4), (2, 4), (2, 6)]))

# ---------------- m29 (07du) clockwise triangles ----------------
def clockwise_count(lab):
    n = len(lab)
    where = {v: i for i, v in enumerate(lab)}  # positions in clockwise order
    cnt = 0
    for i, j, k in itertools.combinations(range(1, n + 1), 3):
        a, b, c = where[i], where[j], where[k]
        # clockwise if positions a->b->c go around in increasing cyclic order
        if (a < b < c) or (b < c < a) or (c < a < b):
            cnt += 1
    return cnt


check("m29 n=6 all labelings even", all(clockwise_count(p) % 2 == 0 for p in itertools.permutations(range(1, 7))))
check("m29 n=100 random labelings even", all(clockwise_count(random.sample(range(1, 101), 100)) % 2 == 0 for _ in range(3)))
check("m29 n=5 can be odd (parity of n matters)", any(clockwise_count(p) % 2 for p in itertools.permutations(range(1, 6))))

# ---------------- m30 (0761) good subsets ----------------
def t_n(n):
    c = 0
    for mask in range(1, 1 << n):
        s = [i + 1 for i in range(n) if mask >> i & 1]
        if sum(s) % len(s) == 0:
            c += 1
    return c


check("m30 t_n = n mod 2", all((t_n(n) - n) % 2 == 0 for n in range(1, 17)))

# ---------------- m31 (0382) strong tournaments ----------------
def has_cycle_len(n, beats, k):
    for combo in itertools.combinations(range(n), k):
        first = combo[0]
        for perm in itertools.permutations(combo[1:]):
            cyc = (first,) + perm
            if all(beats[cyc[i]][cyc[(i + 1) % k]] for i in range(k)):
                return True
    return False


def strongly_connected(n, beats):
    for s in range(n):
        reach = {s}
        st = [s]
        while st:
            u = st.pop()
            for v in range(n):
                if beats[u][v] and v not in reach:
                    reach.add(v)
                    st.append(v)
        if len(reach) < n:
            return False
    return True


cnt_sc = 0
good = True
for n in range(3, 8):
    for _ in range(150):
        beats = [[False] * n for _ in range(n)]
        for i, j in itertools.combinations(range(n), 2):
            if random.random() < 0.5:
                beats[i][j] = True
            else:
                beats[j][i] = True
        if strongly_connected(n, beats):
            cnt_sc += 1
            good &= all(has_cycle_len(n, beats, k) for k in range(3, n + 1))
check("m31 strong tournaments are pancyclic (random n<=7)", good and cnt_sc > 100)

# ---------------- m32 (06va) blocks ----------------
good = True
for _ in range(400):
    n = random.randint(1, 7)
    w = [1 + random.random() for _ in range(n)]
    # scale extras so that the total is 2n with all weights >= 1
    extra = [x - 1 for x in w]
    s = sum(extra)
    w = [1 + e * n / s for e in extra] if s > 0 else [2.0] * n
    sums = [sum(c) for k in range(n + 1) for c in itertools.combinations(w, k)]
    for i in range(201):
        r = (2 * n - 2) * i / 200
        good &= any(r - 1e-9 <= x <= r + 2 + 1e-9 for x in sums)
check("m32 random block sets", good)

# ---------------- m33 (06w4) permutations ----------------
def P(n):
    return sum(1 for a in itertools.permutations(range(1, n + 1)) if all((i + 1) * a[i] <= (i + 2) * a[i + 1] for i in range(n - 1)))


check("m33 equals F_{n+1}", [P(n) for n in range(1, 10)] == [sp.fibonacci(n + 1) for n in range(1, 10)])

# ---------------- m34 (056u) knights ----------------
def max_antichain(n):
    pts = list(itertools.product(range(1, n + 1), repeat=3))
    idx = {p: i for i, p in enumerate(pts)}
    succ = [[idx[q] for q in pts if all(q[t] > p[t] for t in range(3))] for p in pts]
    match_r = [-1] * len(pts)

    def aug(u, seen):
        for v in succ[u]:
            if v in seen:
                continue
            seen.add(v)
            if match_r[v] == -1 or aug(match_r[v], seen):
                match_r[v] = u
                return True
        return False

    m = sum(1 for u in range(len(pts)) if aug(u, set()))
    return len(pts) - m  # Dilworth: min chain cover = N - max matching (relation is transitive)


check("m34 max antichain = 3n^2-3n+1 (n<=5)", all(max_antichain(n) == 3 * n * n - 3 * n + 1 for n in range(1, 6)))

# ---------------- m35 (0ai8) special numbers ----------------
check("m35 2014 factorization", sp.factorint(2014) == {2: 1, 19: 1, 53: 1})
check("m35 x^3+2y^3 = 0 mod 19 only trivially", [(x, y) for x in range(19) for y in range(19) if (x**3 + 2 * y**3) % 19 == 0] == [(0, 0)])
check("m35 2^6 mod 19", pow(-2, 6, 19) == 7)
check("m35 cubes are special", all(Fraction(k**3 + 2 * k**3, 1 + 2) == k**3 for k in range(1, 50)))
vals = {x**3 + 2 * y**3 for x in range(1, 120) for y in range(1, 120)}
check("m35 no small representation of 2014", not any(2014 * (u**3 + 2 * v**3) in vals for u in range(1, 12) for v in range(1, 12)))

# ---------------- m36 (093f) a_{k+1} = a_k^3 + 1 ----------------
good = True
for p in sp.primerange(2, 4000):
    if p % 3 != 2:
        continue
    good &= len({x**3 % p for x in range(p)}) == p
    a, hit = 1, False
    for _ in range(p + 1):
        if a % p == 0:
            hit = True
            break
        a = (a**3 + 1) % p
    good &= hit
check("m36 every prime 2 mod 3 divides a term", good)

# ---------------- m37 (00lz) 2017^a = b^6 - 32b + 1 ----------------
sols = []
for b in range(0, 3000):
    v = b**6 - 32 * b + 1
    if v <= 0:
        continue
    a = 0
    while v % 2017 == 0:
        v //= 2017
        a += 1
    if v == 1:
        sols.append((a, b))
check("m37 solutions", sols == [(0, 0), (0, 2)])
check("m37 2017 mod 64", 2017 % 64 == 33 and 33 * 33 % 64 == 1 and 4**6 - 128 + 1 == 63**2)

# ---------------- m38 (020b) divisors 2k-l ----------------
def prop38(n):
    ds = [d for d in sp.divisors(n) if d < n]
    for k in ds:
        for l in ds:
            if not any(x != 0 and n % abs(x) == 0 for x in (2 * k - l, 2 * l - k)):
                return False
    return True


check("m38 composite solutions are 6, 9, 15", [n for n in range(2, 6000) if prop38(n) and not sp.isprime(n)] == [6, 9, 15])
check("m38 primes work", all(prop38(p) for p in sp.primerange(2, 500)))

# ---------------- m39 (01hr) avoid difference t ----------------
good = True
for _ in range(2000):
    n = random.randint(1, 8)
    t = Fraction(random.choice([-3, -2, -1, 1, 2, 3]), random.choice([1, 2]))
    a = [Fraction(random.randint(-6, 6), 2) for _ in range(2 * n - 1)]
    T = abs(t)
    cls = [[i for i in range(2 * n - 1) if math.floor(a[i] / T) % 2 == c] for c in (0, 1)]
    big = max(cls, key=len)
    good &= len(big) >= n
    for c in cls:
        good &= all(a[i] - a[j] != t for i in c for j in c)
check("m39 parity-of-floor colouring works", good)

# ---------------- m40 (01bf) diagonal game ----------------
def first_wins(N):
    cells = [(x, y) for x in range(N) for y in range(N)]

    @lru_cache(maxsize=None)
    def win(used_d1, used_d2):
        # used diagonals as bitmasks; player to move wins?
        for x, y in cells:
            d1, d2 = x - y + N - 1, x + y
            if not (used_d1 >> d1 & 1) and not (used_d2 >> d2 & 1):
                if not win(used_d1 | 1 << d1, used_d2 | 1 << d2):
                    return True
        return False

    return win(0, 0)


check("m40 first player wins iff N odd (N<=6)", all(first_wins(N) == (N % 2 == 1) for N in range(1, 7)))

# ---------------- m41 (0a95) factor game ----------------
def first_wins_factor(start):
    @lru_cache(maxsize=None)
    def win(state):
        nums = list(state)
        moves = set()
        for i, x in enumerate(nums):
            rest = nums[:i] + nums[i + 1:]
            for a in sp.divisors(x):
                if 1 < a <= x // a and x // a > 1:
                    moves.add(tuple(sorted(rest + [a, x // a])))
        for x in set(nums):
            if nums.count(x) >= 2:
                r = list(nums)
                r.remove(x)
                moves.add(tuple(r))
                r.remove(x)
                moves.add(tuple(r))
        return any(not win(m) for m in moves)

    return win((start,))


check("m41 first player wins from 10^m (m<=4)", all(first_wins_factor(10**m) for m in range(1, 5)))

# ---------------- m42 (03mi) prefix sums ----------------
def construct42(n):
    return [i if i % 2 else n + 1 - i for i in range(1, n + 1)]


def ok42(a):
    n = len(a)
    s = [0] + list(itertools.accumulate(a))
    return sorted(a) == list(range(1, n + 1)) and len({x % (n + 1) for x in s}) == n + 1


check("m42 construction for odd n", all(ok42(construct42(n)) for n in range(1, 300, 2)))
check("m42 even n impossible (n<=8)", not any(ok42(p) for n in range(2, 9, 2) for p in itertools.permutations(range(1, n + 1))))

# ---------------- m43 (0da9) |a_i - i| = k ----------------
def feasible43(N, k):
    used = [False] * (N + 1)

    def go(i):
        if i > N:
            return True
        for v in (i - k, i + k):
            if 1 <= v <= N and not used[v]:
                used[v] = True
                if go(i + 1):
                    return True
                used[v] = False
        return False

    return go(1)


check("m43 small N: k works iff 2k | N", all(feasible43(N, k) == (N % (2 * k) == 0) for N in range(2, 25) for k in range(1, N + 2)))
divs500 = sp.divisors(500)
good = len(divs500) == 12
for k in divs500:
    a = [0] * 1001
    for i in range(1, 1001):
        a[i] = i + k if ((i - 1) // k) % 2 == 0 else i - k
    good &= sorted(a[1:]) == list(range(1, 1001)) and all(abs(a[i] - i) == k for i in range(1, 1001))
check("m43 block construction for k | 500", good)
check("m43 2k | 1000 iff k | 500", [k for k in range(1, 1001) if 1000 % (2 * k) == 0] == divs500)

# ---------------- m44 (02er) dancing ----------------
good = True
tested = 0
for _ in range(3000):
    m, w = random.randint(1, 5), random.randint(1, 5)
    D = [[random.random() < 0.5 for _ in range(w)] for _ in range(m)]
    if not all(any(D[i][j] for i in range(m)) for j in range(w)):
        continue
    if any(all(D[i]) for i in range(m)):
        continue
    tested += 1
    good &= any(D[M][W] and D[M2][W2] and not D[M][W2] and not D[M2][W]
                for M in range(m) for M2 in range(m) for W in range(w) for W2 in range(w))
check("m44 random parties", good and tested > 300)

# ---------------- m45 (0gmz) teachers and students ----------------
good = True
for _ in range(3000):
    S, T = random.randint(1, 12), random.randint(1, 5)
    K = [[random.random() < 0.4 for _ in range(T)] for _ in range(S)]
    for j in range(S):
        if not any(K[j]):
            K[j][random.randrange(T)] = True
    a = [sum(K[j][i] for j in range(S)) for i in range(T)]
    b = [sum(K[j]) for j in range(S)]
    best = max(Fraction(a[i], b[j]) for j in range(S) for i in range(T) if K[j][i])
    good &= best >= Fraction(S, T)
check("m45 some pair has ratio >= S/T", good and Fraction(2006, 14) == Fraction(1003, 7))

# ---------------- m46 (01yy) equal eccentricities ----------------
def eccs(n, edges):
    adj = {v: set() for v in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    res = []
    for s in range(n):
        dist = {s: 0}
        q = [s]
        for u in q:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
        if len(dist) < n:
            return None
        res.append(max(dist.values()))
    return res


def construct46(n, m):
    if m == 1:
        return list(itertools.combinations(range(n), 2))
    E = [(i, (i + 1) % (2 * m)) for i in range(2 * m)]
    extras = list(range(2 * m, n))
    for u in extras:
        E += [(u, 0), (u, 1), (u, 2 * m - 1)]
    E += list(itertools.combinations(extras, 2))
    return E


check("m46 construction", all(set(eccs(n, construct46(n, m))) == {m} for n in range(2, 14) for m in range(1, n // 2 + 1)))
good = True
for n in range(2, 7):
    pairs = list(itertools.combinations(range(n), 2))
    ms = set()
    for mask in range(1 << len(pairs)):
        e = eccs(n, [pairs[i] for i in range(len(pairs)) if mask >> i & 1])
        if e and len(set(e)) == 1:
            ms.add(e[0])
    good &= ms == set(range(1, n // 2 + 1))
check("m46 brute force n<=6", good)

# ---------------- m47 (01h8) ab/(a+b) | N ----------------
def count47(N):
    c = 0
    for a in range(1, N * N + N + 2):
        for m in sp.divisors(N):
            if a > m and (m * m) % (a - m) == 0:
                c += 1
    return c


def brute47(N):
    lim = N * N + N + 1
    return sum(1 for a in range(1, lim + 1) for b in range(1, lim + 1) if (a * b) % (a + b) == 0 and N % ((a * b) // (a + b)) == 0)


check("m47 brute force N<=12", all(brute47(N) == sp.divisor_count(N) ** 2 for N in range(1, 13)))
check("m47 via (a-m)(b-m)=m^2, N<=60", all(count47(N) == sp.divisor_count(N) ** 2 for N in range(1, 61)))

# ---------------- m48 (0dr9) ----------------
def admissible(N):
    return all(sp.isprime(k) for k in range(3, N, 2) if math.gcd(k, N) == 1)


adm = [N for N in range(1, 4000, 2) if admissible(N)]
check("m48 largest admissible is 105", max(adm) == 105)
qs = list(sp.primerange(3, 2000))
check("m48 q_{j+1}^2 < q_1...q_j for j>=4 (checked numerically)", all(qs[j] ** 2 < math.prod(qs[:j]) for j in range(4, len(qs))))
check("m48 j=3 fails", not (qs[3] ** 2 < math.prod(qs[:3])))

# ---------------- m49 (0eu6) 1+4^x+4^y=z^2 ----------------
sols = [(x, y) for x in range(1, 60) for y in range(1, 60) if math.isqrt(1 + 4**x + 4**y) ** 2 == 1 + 4**x + 4**y]
check("m49 solutions", sorted(sols) == sorted({(t, 2 * t - 1) for t in range(1, 31)} | {(2 * t - 1, t) for t in range(1, 31)}))
check("m49 z value", all(math.isqrt(1 + 4**t + 4 ** (2 * t - 1)) == 2 ** (2 * t - 1) + 1 for t in range(1, 30)))

print(f"{len(ok)} checks passed")
