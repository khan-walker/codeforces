import sys
input = sys.stdin.readline
INF = 1 << 61
 
def solve():
    n = int(input())
    par = [-1] + [int(x) - 1 for x in input().split()]
    s = input().rstrip()
 
    dp0 = [0] * n
    dp1 = [0] * n
 
    for i in range(n - 1, -1, -1):
        if s[i] == "S":
            dp1[i] = INF
        elif s[i] == "P":
            dp0[i] = INF
        
        p = par[i]
        
        if p >= 0:
            dp0[p] += min(dp0[i], 1 + dp1[i])
            dp1[p] += min(1 + dp0[i], dp1[i])
 
    ans = min(dp0[0], dp1[0])
    return ans
 
T = int(input())
out = [solve() for _ in range(T)]
print("\n".join(map(str, out)))