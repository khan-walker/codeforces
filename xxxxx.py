for _ in range(int(input())):
	n, x = map(int, input().split())
	a =  list(map(int, input().split()))
	s, ans = 0, -1
	for i in range(n):
		s += a[i]
		if s%x: ans = max(ans, n-i-1, i+1)
	print(ans)