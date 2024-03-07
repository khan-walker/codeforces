t = int(input())

for _ in range(t):
    n = int(input())
    x = input()
    s1 = ''
    s2 = ''
    t = True
    for i in range(n):
        if x[i] == '2':
            if t:
                s1 += '1'
                s2 += '1'
            else:
                s1 += '0'
                s2 += '2'
        elif x[i] == '0':
            s1 += '0'
            s2 += '0'
        else:
            if t:
                s1 += '1'
                s2 += '0'
            else:
                s1 += '0'
                s2 += '1'
            t = False
    print(s1, s2, sep = "\n")
