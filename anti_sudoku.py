# t = int(input())

# for _ in range(t):
#     a = []
#     for i in range(9):
#         l = list(input())
#         a.append(l)
#     for i in range(9):
#         for j in range(9):
#             if a[i][j] == "2":
#                 a[i][j] = "1"

            
#     [print("".join(s)) for s in a]

for i in range(int(input())*9):
    print(input().replace("1", "2"))