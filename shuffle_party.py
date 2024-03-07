t = int(input())

def ld(number):
    for divisor in range(number // 2, 0, -1):
        if number % divisor == 0:
            return divisor
        
def binary_search(arr, target = 1):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == 1:
            return mid 
        elif mid_element < 1:
            low = mid + 1  
        else:
            high = mid - 1 

    return -1

a = list(range(1, 1000000001))
res = [1]
for i in range(2, 1000000001):
    d = ld(i)
    a[d - 1], a[i] = a[i], a[d - 1]
    pos = binary_search(a, 1)
    res.append(pos)



for _ in range(t):
    n = int(input())
    print(res[n - 1])