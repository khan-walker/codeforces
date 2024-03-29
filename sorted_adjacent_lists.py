for i in range(int(input())): 
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while a: print(a.pop(len(a) // 2), end=" ")
    print()