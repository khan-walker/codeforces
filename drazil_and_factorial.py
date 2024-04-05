n = int(input())
a = input()

index = 0
for i in range(n):
    if a[i] != "0":
        index = i
        break

d = {"2":[2], "3": [3], "4":[2, 2, 3], 
     "5": [5], "6":[5, 3], "7": [7], 
     "8":[7,2, 2, 2], "9":[7,2,3,3]}
res = []
for i in range(index, n):
    if a[i] == "0" or a[i] == "1":
        continue
    else:
        res += d[a[i]]

res.sort(reverse=True)
res = "".join(map(str, res))
print(res)
