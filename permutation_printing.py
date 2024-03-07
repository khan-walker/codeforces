from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    a = deque()
    maxi = n
    mini = 1
    while len(a) != n:
        if len(a) % 2 == 0:
            a.append(maxi)
            maxi -= 1
        else:
            a.append(mini)
            mini += 1
    print(*a)