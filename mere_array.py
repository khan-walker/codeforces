from math import gcd
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    b = a.copy()
    b.sort()
    odp = 'YES'
    for i in range(n):
        if a[i] % m != 0:
            if a[i] != b[i]:
                odp = 'NO'
    print(odp)

