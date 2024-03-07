from math import ceil
n=int(input())
s=list(map(int,input().split()))
a=s.count(4)
b=s.count(3)
c=s.count(2)
d=s.count(1)
p=a+b
if d<=b:
    p=p+ceil(c/2)
else :
    p=p+ceil((d-b+2*c)/4)
print(p)