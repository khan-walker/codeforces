from math import comb
a, b = input(), input()
n = b.count('?')
r = a.count("-") - b.count("-")
print(0 if n < r or r < 0 else comb(n, r) / (2 ** n))