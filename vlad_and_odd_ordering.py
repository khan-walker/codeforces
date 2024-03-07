def f(n, k):
    if k <= (n + 1) // 2:
        return 2 * k - 1
    return 2 * f(n // 2, k - (n + 1) // 2)

def solve():
    n, k = map(int, input().split())
    print(f(n, k))

tt = int(input())

for _ in range(tt):
    solve()