t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    i = 0
    count = 0
    while i < n:
        if s[i] == "@":
            count += 1
            try:
                if s[i + 1] == "*" and s[i + 2] == "*":
                    break
                elif s[i + 1] == "*":
                    i += 2
                else:
                    i += 1
            except:
                break

        elif s[i] == "*":
            try:
                if s[i + 1] == "*":
                    break
                else:
                    i += 1
            except:
                break
        else:
            try:
                if s[i + 1] == "*" and s[i + 2] == "*":
                    break
                elif s[i + 1] == "*":
                    i += 2
                else:
                    i += 1
            except:
                break         
    print(count)