import collections

n, m = map(int, input().split())
input()

INF = 1e9
maps = [[INF] * (n+1) for _ in range(n+1)]

maps_dict = collections.defaultdict(list)

for _ in range(m):
    start, end, cost = map(int, input().split())
    maps[start][end] = cost
    maps[end][start] = cost 
    


#     maps_dict[start].append(end)
#     maps_dict[end].append(start)

# index_list = [range(1, n+1)]

# result = []
# def dfs(index, path, cost, in_list):
#     if len(path) == 4:
#         return result.append(cost)

#     for end in maps_dict[index].values:
        


# dfs(1, [1], 0, index_list)