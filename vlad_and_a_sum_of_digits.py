pg = [0]
for i in range(1, 200100):
    pg.append(pg[i - 1] + sum(map(int, str(i))))

for _ in range(int(input())):
    print(pg[int(input())])