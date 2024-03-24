import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = []
for i in range(n):
    l.append(a[i] - b[i])
l.sort()
i = 0
j = n - 1
ans = 0
while i < j:
    if l[i] + l[j] > 0:
        ans += j - i
        j -=1 
    else: i += 1
print(ans)