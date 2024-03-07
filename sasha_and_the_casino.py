def solve():
    k, x, a = map(int, input().split())

    t = 0

    check = True
    for i in range(x):
        ti = t // (k - 1) + 1
        t += ti
        if (t > a):
            check = False
            break

    if check and (a-t) * k > a:
        print("yes")
    else:
        print("no")

t = int(input())
for _ in range(t):
    solve()
