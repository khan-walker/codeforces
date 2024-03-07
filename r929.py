from sys import stdin
from collections import Counter, defaultdict

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = sum(abs(x) for x in a)
    print(s)