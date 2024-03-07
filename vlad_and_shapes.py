t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        s = input()
        grid.append(s)
    count = 0
    res = []
    for i in range(len(grid)):
        c = 0
        for j in range(len(grid)):
            if grid[i][j] == "1":
                c += 1
        
        if c > 0:
            count += 1
            res.append(c)
        if count == 2:
            if res[0] == res[1]:
                print('SQUARE')
                break
            else:
                print("TRIANGLE")
                break