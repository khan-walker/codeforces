import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
	n,h = map(int,input().split())
	a = list(map(int,input().split()))
	a.append(10**20)
	l,r = 0,10**19
	while r-l>1:
		k = (l+r)//2
		cnt = 0
		for i in range(n):
			cnt += min(a[i+1]-a[i],k)
		if cnt<h: l = k
		else: r = k
	print(r)
