t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(sum(a[i] - a[i - 1] for i in range(1, len(a))))