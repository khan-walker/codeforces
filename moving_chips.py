from collections import deque
t = int(input())

def solve(a, n):
    # a = deque(a)
    # for i in range(n):
    #     if a[i] == 0:
    #         a.popleft()
    #     else:
    #         break
    # for j in range(len(a) - 1, -1, -1):
    #     if a[j] == 0:
    #         a.pop()
    #     else:
    #         break
    l, r = 0, n - 1
    for i in range(n):
        if a[i] == 1:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            r = i
            break
    if l == r:
        return 0
    count = 0
    for i in range(l, r):
        if a[i] == 0:
            count += 1

    return count

    





for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a, n))