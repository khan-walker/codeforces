t = int(input())
a = [1, 3, 6, 10, 15]
dp = [float('inf')] * 1_000_000_001
dp[0] = 0
for i in range(1, 1_000_000_002):
    for coin in a:
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

for _ in range(t):
    n = int(input())
    print(n)

    

