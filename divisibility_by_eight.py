import re 
s = input()
for i in range(0, 1000, 8):
    if re.search('.*'.join(str(i)), s):print("YES\n", i); quit();
print("NO") 