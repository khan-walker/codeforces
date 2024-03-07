from sys import stdin

n, t = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
r = 0
summa = 0
ans = 0
for i in range(n):
    while r < n and summa + a[r] <= t:
        summa += a[r]
        r += 1
    ans = max(ans, r - i)
    summa -= a[i]

print(ans)