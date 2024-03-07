n, a, b, c = map(int, input().split())

a, b, c = sorted([a, b, c])[::-1]

ans = 0
for i in range(n // a + 1):
    for j in range(n // b + 1):
        k = (n - i * a - j * b) // c
        if i * a + b * j + k * c == n and k >= 0:
            ans = max(ans, i + j + k)
            break

print(ans)