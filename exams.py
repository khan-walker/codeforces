n = int(input())
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))

ab.sort()
now = ab[0][1]
mini = float("-inf")

for i in range(n):
    now = min(ab[i])
    if now >= mini:
        mini = now
    else:
        mini = ab[i][0]
    
print(mini)