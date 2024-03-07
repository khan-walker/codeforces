from sys import stdin

n, m, a, b = map(int, stdin.readline().split())

minimum_sum = float('inf')

for i in range(0, n + 1):
    for j in range(0, n + 1):
        summa = i * a + b * j
        if summa < minimum_sum and (i + j * m) >= n:
            minimum_sum = summa
            break

print(minimum_sum)
        
