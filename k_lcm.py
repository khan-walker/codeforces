t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if n & 1:
        print(1, n // 2, n // 2)
    else:
        if n % 4 != 0:
            print(n // 2 - 1, n // 2 - 1, 2)
        else:
            print(n // 2, n // 4, n // 4)
