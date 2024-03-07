n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
number = a[k - 1] if k != 0 else a[0] - 1
cnt = sum(a[i] <= number for i in range(len(a)))
if number < 1 or cnt != k:
    print(-1)
else:
    print(number)
