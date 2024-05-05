from collections import Counter
for _ in range(int(input())):
	N,K=list(map(int,input().split()))
	arr=Counter(map(lambda x: int(x)%K,input().split()))
	mx=0
	for i in arr:
		r=K-i
		if(r==K): continue
		mx=max(mx, r+K*(arr[i]-1))
	print(mx+1 if mx else 0)