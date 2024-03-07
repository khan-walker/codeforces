for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mapa={}
    ans=0
    b=2**31-1
    for i in a:
        c=b-i
        if(mapa.get(i,0)==0):
            ans+=1
            mapa[c]=mapa.get(c,0)+1
        else:
            mapa[i]-=1
    print(ans)        
        