from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

a.sort()
b.sort()
res = 0
for i in range(n):
    for j in range(m):
        if abs(a[i] - b[j]) <= 1:
            b[j] = 1000
            res += 1
            break
print(res)