m,s=map(int,input().split())
if s>9*m or (s<1 and m!=1):
    print(-1,-1)
else:
    mini = int(10**(m-1)+((s-1)%9+1)*10**((s-1)//9)-1)
    maxi = 10**m-10**(m-(s-1)//9-1)*(9-(s-1)%9)
    print(mini, maxi)