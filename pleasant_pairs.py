s = int(input())
for _ in range(s):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(a[i] - i - 2, n, a[i]):
            if i + j + 2 == a[i] * a[j] and i < j:
                count += 1
    print(count)