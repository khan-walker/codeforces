I = lambda:map(int, input().split());I();c=d=0
for x, y in zip(I(), I()):c,d = max(d +x, c), max(c+y,d)
print(max(c, d))