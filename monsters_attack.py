t = int(input())

def solve(n, k, a, x):
    x = list(map(abs, x))
    zippo = list(zip(x, a))
    zippo.append((0, 0))
    zippo.sort()
    d = {}
    for cor, health in zippo:
        if cor in d:
            d[cor] += health
        else:
            d[cor] = health
    bullet = 0
    key_list = list(d.keys())
    for i in range(1, len(key_list)):
        if d[key_list[i]] > (key_list[i] - key_list[i - 1]) * k + bullet:
            return "NO"
        bullet = (key_list[i] - key_list[i - 1]) * k + bullet - d[key_list[i]]
        
    return "YES"

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print(solve(n, k, a, x))
