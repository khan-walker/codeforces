n=int(input());l=[[*map(int,input().split())]for _ in[0]*n]
s=2
for i in range(1,n-1):
 x,h=l[i]
 if x-h>l[i-1][0]:s+=1
 elif x+h<l[i+1][0]:s+=1;l[i][0]+=h
print(s if n>1 else 1)