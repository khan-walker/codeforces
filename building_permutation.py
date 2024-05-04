input(); k, j = 0, 1
for i in sorted(map(int, input().split())):k+= abs(i - j); j+= 1
print(k)