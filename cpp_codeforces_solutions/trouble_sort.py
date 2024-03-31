t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if (1 in b and (0 in b)) or sorted(a) == a:
        print('yes')
    else: print('no')