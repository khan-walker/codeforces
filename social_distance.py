t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input() + '0' * k
    i = 0
    count = 0
    while i < n:
        try:
            if s[i] == '0':
                for j in range(1, k + 1):
                    if s[i + j] == '1':
                        i += j + k + 1
                        break
                else:
                    count += 1
                    i += k + 1
            else:
                i += k + 1
        except:
            break

    print(count)
