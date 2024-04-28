t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()
    if n == 2:
        print(b[0], b[0])
        continue
    now = 0
    add = n - 1
    res = []
    while now <= n * (n - 1) // 2 - 1:
        res.append(b[now])
        now += add
        add -= 1
    res.append(b[-1])
    print(*res)
        
