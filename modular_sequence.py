INF=(1<<61)-1
t=int(input())
size=200010
dp=[INF]*size
bef=[0]*size
dp[0]=0
for i in range(1,size):
    for j in range(1,size):
        if i-j*(j+1)//2<0:
            break
        if dp[i-j*(j+1)//2]+j+1<dp[i]:
            dp[i]=dp[i-j*(j+1)//2]+j+1
            bef[i]=j
for _ in range(t):
    n,x,y,s=map(int,input().split())
    add=x%y
    x-=add
    s-=add*n
    if s%y!=0:
        print("NO")
        continue
    ans=[]
    ans.append(x)
    s-=x
    yn="NO"
    for i in range(n):
        if s<0:
            break
        if dp[s//y]<=n-i-1:
            yn="YES"
            while len(ans)<n:
                pos=s//y
                ans.append(0)
                for j in range(bef[pos]):
                    ans.append(ans[-1]+y)
                    s-=ans[-1]
            break
        ans.append(ans[-1]+y)
        s-=ans[-1]
    print(yn)
    if yn=="YES":
        for i in range(n):
            ans[i]+=add
        print(*ans)