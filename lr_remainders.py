t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    l = 0
    r = n - 1
    b = []
for c in s:
    if c == "L":
        b.append(a[l])
        l += 1
    if c == "R":
        b.append(a[r])
        r -= 1
vas = 1
c = []
for i in range(n):
    vas = vas * b[n - 1 - i] % m
    c.append(vas)
print(*reversed(c))