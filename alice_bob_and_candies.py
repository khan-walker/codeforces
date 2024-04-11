for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	X=a[0]
	x=a[0]
	a.pop(0)
	y=0
	Y=0
	moves=1
	while len(a)!=0:
		while Y<=X :
			if len(a)==0:
				break
			Y+=a[-1]
			a.pop(-1)
		moves+=1
		y+=Y
		if len(a)==0:
			break
		X=0
		while X<=Y:
			if len(a)==0:	
				break
			X+=a[0]
			a.pop(0)
		moves+=1
		x+=X
		Y=0
	print(moves,x,y)