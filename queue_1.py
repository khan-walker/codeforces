n = int(input())
t = list(map(int, input().split()))
t.sort()
cnt = 0
wait = 0
for i in range(len(t)):
    if t[i] >= wait:
        wait += t[i]
        cnt += 1
print(cnt)

