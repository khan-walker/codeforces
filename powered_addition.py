t = int(input())

while t:
    t -= 1
    input()
    a = list(map(int, input().split()))
    x, m, d = 0, -1e9, 0
    for i in a:
        m = max(m, i)
        d = max(d, m - i)
    while d:
        d //= 2
        x += 1
    print(x)
    