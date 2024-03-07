from sys import stdin
from collections import defaultdict, Counter
import math


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
q = list(map(int, stdin.readline().split()))

s = sum(a)
i = 0
res = []
k = 0
while i < n:
    while a[i] > 0:
        k += 1
        res.append((k, i))
        a[i] -= 1
    i += 1

def binary_search(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if array[mid][0] == target:
            return mid
        if array[mid][0] > target:
            r = mid - 1
        else:
            l = mid + 1
    return None

for query in q:
    index = binary_search(res, query)
    print(res[index][1] + 1)