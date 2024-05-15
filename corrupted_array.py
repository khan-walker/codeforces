t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()
    if n < 3:
        print(-1)
        continue        
    for i in [1, 2, 3]:
        maxi = b[-i]
        over = False
        summa = sum(b[:-i])
        if i == 1:
            for j in range(0, n - 1):
                if summa - b[j] == maxi:
                    print(*(b[:j] + b[j + 1:-1]))
                    over = True
                    break
        elif i == 2:
            if summa == b[-2]:
                print(*b[:-2])
                break
        elif i == 3:
            print(-1)
            break
        if over:
            break




            
