t=int(input())
s="Ashishgup","FastestFinger"
for i in range(t):
    n=int(input())
    r=0
    while n%2<1:n,r=n//2,r+1
    if r==1:
        z=n>1
        for j in range(3,int(n**.5)+1,2):
            if n%j<1:
                z=0
                break
        print(s[z])
    else:print(s[n<2])