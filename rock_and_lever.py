for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    c = {}
    for x in a:
        h = x.bit_length()
        c[h] = c.get(h, 0) + 1
    print(sum(v * (v - 1) // 2 for v in c.values()))
