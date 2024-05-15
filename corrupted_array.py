for _ in [0] * int(input()):
    n = int(input())
    a = sorted(map(int, input().split()))
    s = sum(a)
    if s - a[-1] == 2 * a[-2]: print(*a[:-2]); continue
    if s - 2 * a[-1] in a[:-1]:
        m = a[:-1].index(s - 2 * a[-1])
        print(*[a[i] for i in range(n + 1) if i != m])
        continue

    print(-1)
