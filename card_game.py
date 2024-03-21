for _ in range(int(input())):
    n=int(input())
    t=input().strip()
    d={'C':[],'S':[],'D':[],'H':[]}
    for i in sorted(i[::-1] for i in input().split()):
        d[i[0]].append(i[::-1])
    if sum(len(d[i])%2 for i in d if i!=t)>len(d[t]):print('IMPOSSIBLE');continue
    a=[]
    for i in d:
        if i!=t:
            a+=d[i]
            if len(d[i])%2:a+=[d[t].pop()]
    print(*(a+d[t]))