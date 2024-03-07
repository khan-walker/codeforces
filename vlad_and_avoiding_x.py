import sys
from itertools import product
 
input = lambda: sys.stdin.readline().rstrip()  # faster!
 
 
def check(g, flag):
    for r in range(1, 6):
        for c in range(1 + (0 if (r + 1) & 1 == flag else 1), 6, 2):
            if g[r][c] == g[r - 1][c - 1] == g[r - 1][c + 1] == g[r + 1][c - 1] == g[r + 1][c + 1] == "B":
                return False
    return True
 
 
def solve(g, blacks, flag):
    if check(g, flag):
        return 0
    best = 50
    for p in product("WB", repeat=len(blacks)):
        for colour, (r, c) in zip(p, blacks):
            g[r][c] = colour
        if check(g, flag):
            best = min(best, p.count("W"))
    return best
 
 
def solve_case():
    g = [list(input()) for _ in range(7)]
    blacks = [[], []]
    for r in range(1, 6):
        for c in range(1, 6):
            if g[r][c] == "B":
                blacks[(r + c) & 1] += [(r, c)]
    return solve(g, blacks[0], 0) + solve(g, blacks[1], 1)
 
 
ans = []
for _ in range(int(input())):
    ans += [str(solve_case())]
print("\n".join(ans))