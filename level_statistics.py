
for t in range(int(input())):
    a,b=0,0
    ans="YES"
    for i in range(int(input())):
        c,d=map(int,input().split())
        if c-a<d-b or min(c-a,d-b)<0 :
            ans="NO"
        a,b=c,d
    print(ans)