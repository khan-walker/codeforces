for _ in range(int(input())):
    s=input()
    ds=[-1e9, -1e9, -1e9]
    res=int(1e9)
    for i in range(len(s)):
        ds[int(s[i])-1]=i
        res=min(res, i-min(ds[0], ds[1], ds[2]))
    if res>1e8:
        res=-1
    print(res+1)