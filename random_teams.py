n,m=map(int,input().split())
r=n//m
print(m*r*(r-1)//2+n%m*r,(n-m+1)*(n-m)//2)