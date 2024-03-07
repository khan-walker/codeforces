from sys import stdin

x = stdin.readline().strip()

res = []

for digit in x:
    rev = 9 - int(digit)
    if rev < int(digit):
        res.append(str(rev))
    else:
        res.append(digit)
    
if res[0] == '0':
    res[0] = '9'

print(''.join(res))

