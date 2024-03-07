def main():
	n = int(input())
	a = list(map(int,input().split()))
	
	x = [a[i]+i+1 for i in range(n)]
	
	x.sort(reverse=True)
	
	ans = []
	
	for i in range(1,n):
		x[i] = min(x[i], x[i-1]-1)
	
	print(*x)
	
	
for _ in range(int(input())):
	main()