x1, y1, x2, y2 = map(int, input().split())
if (x1 != x2 and y1 != y2) and abs(x2 - x1) != abs(y2 - y1):
    print(-1)
elif (x1 != x2 and y1 != y2):
    print(x1, y2, x2, y1)
elif x1 == x2:
    a = abs(y2 - y1)
    if x1 + a <= 1000:
        print(x1 + a, y1, x2 + a, y2)
    else:
        print(x1 - a, y1, x2 - 1, y2)
elif y1 == y2:
    a = abs(x2 - x1)
    if y1 + a <= 1000:
        print(x1, y1 + a, x2, y2 + a)
    else:
        print(x1, y1 - a, x2, y2 - a)
