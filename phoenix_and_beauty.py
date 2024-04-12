
for _ in range(int(input())) :
    n, k = map(int, input().split())
    data = list(set(map(int, input().split())))
    if len(data) > k : 
        print(-1)
    else :
        print(n * k)
        print(*(data + [1] * (k - len(data))) * n)