n = int(input())
s = {0}
for _ in range(n):
    a = int(input())
    x1 = set((x - a) % 360 for x in s)
    x2 = set((x + a) % 360 for x in s)
    s = x2 | x1

print("YES" if 0 in s else "NO") 