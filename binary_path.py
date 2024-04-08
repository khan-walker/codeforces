for _ in range(int(input())):
    n=int(input())
    a=input()+'2'
    b=input()
    idx=-1
    idx_1=-1
    for i in range(n):
        if a[i+1]>b[i]:idx=i;break
    for i in range(idx-1,-1,-1):
        if a[i+1]<b[i]:idx_1=i;break
    print(a[:idx+1]+b[idx:])
    print(idx-idx_1)