from math import sqrt

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            a = i
            break
    else:
        print("NO")
        continue
    b = n // a
    for i in range(a + 1, int(sqrt(b)) + 1):
        if b % i == 0:
            c = i
            break
    else:
        print("NO")
        continue
    d = n // a // c

    if d != a and d != c and d != 1:
        print("YES")
        print(a, c, d)
    else:
        print("NO")

