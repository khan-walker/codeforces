from bisect import *
 
R = lambda : map(int, input().split())
 
t, = R()
while t:
    t -= 1
    R()
    a,b=[0],[0]
    m,n = 0,0
    for i in R():
        a.append(max(i,m))
        m = max(m,i)
        b.append(n+i)
        n += i
    ans = []
    for i in R():
        value = bisect(a,i) - 1
        ans.append(b[value])
    print(*ans)
 