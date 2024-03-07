t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    l, r = [], []
    for i in range(q):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    