for _ in range(int(input())):
    n = int(input())
    s = list(input())
 
    children = []
    for bruh in range(n):
        u,v = map(int,input().split())
        children.append((u-1,v-1))
 
    theList = [0]
    pointer = 0
 
    while pointer < len(theList):
        theList += list({*children[theList[pointer]]}-{-1})
        pointer += 1
    
    solved = dict()
    def solve(node):
        if node in solved: return solved[node]
        if children[node] == (-1,-1):
            solved[node] = 0
            return 0
        elif -1 in children[node]:
            if children[node][0] != -1:
                ook = solve(children[node][0]) + (s[node] != "L")
                solved[node] = ook
                return ook
            else:
                ook = solve(children[node][1]) + (s[node] != "R")
                solved[node] = ook
                return ook
        else:
            cool = 99999999999999
            cool = min(cool,solve(children[node][0]) + (s[node] != "L"))
            cool = min(cool,solve(children[node][1]) + (s[node] != "R"))
            solved[node] = cool
            return cool
 
    while theList:
        u = theList.pop()
        solve(u)
    
    print(solve(0))