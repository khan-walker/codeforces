from collections import*
for item in[*open(0)][2::2]:c=Counter(map(int,item.split()));print(max(sum(min(c[x],c[s-x])for
x in c)for s in range(101))//2)