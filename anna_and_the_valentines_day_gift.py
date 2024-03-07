for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input().split()
    x = 0
    b = []
    for i in a:
        y = len(i)
        x += y
        for j in range(y):
            if i[y - 1 - j] != '0':
                break
        b.append(j)

    b.sort(reverse = True)
    for i in range(0, n, 2):
        x -= b[i]
    if x > m:
        print("Sasha")
    else:
        print("Anna")

        