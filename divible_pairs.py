def solve():
    n, x, y = map(int, input().split())
    a = [int(x) for x in input().split()]
    cnt = dict()
    ans = 0
    for e in a:
        xx, yy = e % x, e % y
        ans += cnt.get(((x - xx) % x, yy), 0)
        cnt[(xx, yy)] = cnt.get((xx, yy), 0) + 1
    print(ans)
    
    
for _ in range(int(input())):
    solve()