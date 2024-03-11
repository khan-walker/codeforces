from itertools import permutations
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    for i in range(n):
        if (k <= i):
            break
        k = k - i
    print("a" * (n - i - 1) + "b" + "a" * (i - k) + "b" + "a" * (k - 1))