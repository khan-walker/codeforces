from sys import stdin
import math
n = int(input())
a = list(map(int, stdin.readline().split()))

def is_prime(number):
    if number == 1:
        return False
    count = 0
    if number == 2:
        return True
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
        if count == 1:
            return False
    return True

s = set()
for i in range(1, 10 ** 6 + 1):
    if is_prime(i):
        s.add(i)

for number in a:
    if math.sqrt(number) in s:
        print("YES")
    else:
        print("NO")



