for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n - 1):
        if a[i + 1] - a[i] < a[ans + 1] - a[ans]:
            ans = i
    print(a[ans], *a[ans + 2:], *a[:ans], a[ans + 1])