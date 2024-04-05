n, k = map(int, input().split())
s = input() + "!"
c = set(input())


count = 0
i = 0
for j in range(n+1):
    if s[j] not in c:
        l = j - i
        count += l * (l + 1) // 2
        i = j + 1

print(count)
