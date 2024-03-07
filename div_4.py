from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    a = 0
    b = 0
    for char in s:
        if char == "B":
            b += 1
        else:
            a += 1
    if b > a:
        print("B")
    else:
        print("A")