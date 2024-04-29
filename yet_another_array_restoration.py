t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    if n == 2:
        print(x, y)
        continue
    difference = y - x
    d = None
    over = False
    nx, ny = None, None
    for i in range(n, 0, -1):
        for j in range(1, i):
            res = difference / (i - j)
            if res.is_integer() and y - res * (i - 1) > 0:
                d = int(res)
                nx, ny = j, i
                over = True
                break
        if over:
            break

    a1 = y - d * (ny - 1) 
    for i in range(n - 1):
        print(a1 + i * d, end=" ")
    print(a1 + (n - 1) * d)
    
                