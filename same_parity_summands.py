t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 1:
        if k % 2 == 0:
            print("NO")
        else:
            if k <= n:
                print("YES")
                arr = [1] * (k - 1) + [n - (k - 1)]
                print(*arr)
            else:
                print("NO")
    else:
        if k % 2 == 1:
            if k * 2 <= n:
                print("YES")
                if k * 2 == n:
                    arr = [2] * k
                else:
                    arr = [2] * (k - 1) + [n - 2 * (k - 1)]
                print(*arr)
            else:
                print("NO")
        else:
            if k * 2 <= n and k % 2 == 0:
                print("YES")
                if k * 2 == n:
                    arr = [2] * k
                else:
                    arr = [2] * (k - 1) + [n - 2 * (k - 1)]
                print(*arr)
            elif k <= n:
                print("YES")
                if k == n:
                    print(*([1] * k))
                else:
                    arr = [1] * (k - 1) + [n - (k - 1)]
                    print(*arr)
            else:
                print("NO")