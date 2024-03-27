t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = n - 1
    while k > 0 and a[k - 1] >= a[k]: k-=1
    while k > 0 and a[k - 1] <= a[k]: k -= 1
    print(k)
