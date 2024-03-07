t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    odd = 0
    even = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd <= 0:
        print("NO")
    else:
        if x <= even + 1:
            print("YES")
        else:
            if (x - even - 1) % 2 == 1:
                print("NO")
            else:
                print("YES")
