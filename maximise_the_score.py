def max_final_score(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        arr = sorted(test_cases[i][1], reverse=True)
        score = 0
        for j in range(1, 2 * n, 2):
            score += min(arr[j - 1], arr[j])
        results.append(score)
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

results = max_final_score(t, test_cases)
for result in results:
    print(result)
