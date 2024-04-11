n=int(input())
a={}
p=[]
for _ in range(n):
    n,m=input().split()
    a[n]=a.get(n,0)+int(m)
    p.append([n,a[n]])
m=max(a.values())
for i,j in p:
    if a[i]==m and int(j)>=m:
        print(i)
        break