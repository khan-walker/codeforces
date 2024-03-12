n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            if (i + j) & 1:
                arr[i][j] = "W"
            else:
                arr[i][j] = "B"
[print("".join(x)) for x in arr]
