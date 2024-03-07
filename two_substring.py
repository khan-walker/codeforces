s = input()
n = len(s)

def find_occurrence(substring, start_index):
    try:
        index = s.index(substring, start_index)
        return index + 2
    except ValueError:
        return -1

# Check for "AB" followed by "BA"
index_AB = find_occurrence("AB", 0)
if index_AB != -1 and index_AB < n - 1:
    index_BA = find_occurrence("BA", index_AB)
    if index_BA != -1:
        print("YES")
        exit()

# Check for "BA" followed by "AB"
index_BA = find_occurrence("BA", 0)
if index_BA != -1 and index_BA < n - 1:
    index_AB = find_occurrence("AB", index_BA)
    if index_AB != -1:
        print("YES")
        exit()

print("NO")
