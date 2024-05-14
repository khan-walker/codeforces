t = int(input())

for _ in range(t):
    k = int(input())
    s = input()
    for i in range(k - 2):
        if s[i] == s[i + 2]: k -= 1
    print(k - 1)
 
