from bisect import bisect
for _ in range(int(input())):
	n,a,q=int(input()),[0,*map(int,input().split())],int(input())
	for i in range(n):
		a[i+1]+=a[i]
	for _ in range(q):
		l,u=map(int,input().split())
		i=bisect(a,u:=u+a[l-1],l+1)
		print(i-1 if i>n or u*2<a[i-1]+a[i] else i,end=' ')
	print()