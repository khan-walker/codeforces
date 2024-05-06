a=list(input())
n=len(a)
x=-1
for i in range(n):
	if int(a[i])%2!=0:
		continue
	else:
		x=i
	if a[i]<a[-1]:
		break
if x!=-1:
	a[x],a[-1]=a[-1],a[x]
	print(''.join(a))
else:
	print(x)