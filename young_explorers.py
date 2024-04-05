t = int(input())

for _ in range(t):
    n = int(input())
    e = list(map(int, input().split()))
    e.sort()
    cnt = 0
    i = 0
    group_size = 0
    maxi = 1
    while i <= n - 1:
        group_size += 1
        maxi = max(maxi, e[i])
        if group_size >= maxi:
            cnt += 1
            group_size = 0
        i += 1   

    print(cnt)
