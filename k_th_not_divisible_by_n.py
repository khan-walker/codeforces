from sys import stdin
t = int(input())



for _ in range(t):
    n, k = map(int, stdin.readline().split())
    karra = k // (n - 1)
    qoldiq = k - (n - 1) * karra
    number = karra * n + qoldiq
    print(number if qoldiq != 0 else number - 1)