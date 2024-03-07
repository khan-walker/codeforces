from math import ceil, log

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    years = [a[0]]
    
    for i in range(1, len(a)):
        c = (years[-1] / a[i])
        if c.is_integer():
            c += 1
            c = int(c)
        else:
            c = ceil(c)

        now = a[i] * c
        years.append(now)


    print(years[-1])
