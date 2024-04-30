t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print((n ** k) % (10 ** 9 + 7))