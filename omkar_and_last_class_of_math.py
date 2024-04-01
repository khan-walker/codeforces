import math

t = int(input())

for _ in range(t):
    n = int(input())
    ul = int(math.sqrt(n))
    for p in range(2, ul + 1):
        if (n / p).is_integer():
            k = n // p
            print(k, n - k)
            break
    else: 
        print(1, n - 1)

        