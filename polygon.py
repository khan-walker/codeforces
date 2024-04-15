t = int(input())

for _ in range(t):
    n = int(input())
    a = list()
    for i in range(n):
        ai = input()
        a.append(ai+"1")
    a.append("1"*(n + 1))
    ok = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == '1':
                if a[i][j + 1] == '1' or a[i + 1][j] == '1':
                    continue
                else:
                    print('NO')
                    ok = False
                    break
        if ok:
            continue
        else:
            break
    else:
        print('YES')
    

    