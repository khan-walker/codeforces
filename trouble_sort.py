t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l0, l1 = [], []
    for i in range(n):
        if b[i] == 1:
            l1.append(a[i])
        else: 
            l0.append(a[i])

    print(l0, "and", l1)
    if sorted(l0) == l0 and sorted(l1) == l1: 
        print('yes')
    else: 
        print('no')