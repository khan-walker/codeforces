for _ in range(int(input())):
    s = input()
    ans = [s.count('0'), s.count('1')]
    f = [0, 0]

    for i in s:
        f[int(i)] += 1
        ans.append(f[0] + ans[1] - f[1])
        ans.append(f[1] + ans[0] - f[0])
    print(min(ans))