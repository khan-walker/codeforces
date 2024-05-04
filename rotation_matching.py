n = int(input())
ad = {int(x): i for i, x in enumerate(input().split())}
bd = {int(x): i for i, x in enumerate(input().split())}
shifts = [0] * n
for i in range(1, n + 1):
    shifts[(ad[i] - bd[i]) % n] += 1
print(max(shifts))