from math import ceil 
t = int(input())

def solve(n, k):
    all = n * 2
    grids = 4 * n - 2

    if k <= grids - 2:
        return ceil(k / 2)
    elif k <= grids - 1:
        return all - 1
    else:
        return all



for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))