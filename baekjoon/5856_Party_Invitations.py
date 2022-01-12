n, g = map(int, input().split())

cows_list = []
for _ in range(g):
    _, *cows = map(int, input().split())
    cows_list.append(cows)

cows_list.sort(key = lambda x: len(x))

in_cows = []
result = []

def dfs(in_cows, cows_list):
    print(in_cows, cows_list)
    if len(in_cows) >= g:
        result.append(len(in_cows))
        
    temp_list = cows_list[:]
    for cows in cows_list:
        in_cows.extend(cows)
        in_cows = list(set(in_cows))
        temp_list.remove(cows)
        dfs(in_cows, temp_list)

dfs([], cows_list)
print(min(result))


"""
10 4
2 1 3
2 3 4
6 1 2 3 4 6 7
4 4 3 2 1
"""