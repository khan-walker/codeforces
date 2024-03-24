for _ in range(int(input())):
    n = int(input())
    if n == 5 or n == 8:
        print(3)
    else:
        arr = [0,1,2,1,2,1,1,2,2,2,1,2,2,2,3]
        print(n//15 + arr[n%15])