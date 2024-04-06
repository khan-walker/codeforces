for _ in range(int(input())):
    n = int(input())
    s = input()
    z = [0] * n
    z[0] = int(s[0])
    for i in range(1, n): z[i] = z[i] + int(s[i])
    for i in range(n - 1, 0, - 1):
        z[i - 1] += z[i] // 10
        z[i] %= 10

    print(''.join(map(str, z)).lstrip('0'))