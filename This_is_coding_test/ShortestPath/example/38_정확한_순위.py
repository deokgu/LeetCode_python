import pprint
n, m = map(int, input().split())

INF = int(1e9)
nodes = [ [INF] * (n+1) for _ in range(n+1)]

for x in range(n+1):
    nodes[x][x] = 1

for _ in range(m):
    x, y = map(int, input().split())
    nodes[x][y] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            nodes[a][b] = min(nodes[a][b], nodes[a][k] + nodes[k][b])

# pprint.pprint(nodes, depth=3,)

result_count = 0
for a in range(1, n+1):
    _count = 0
    for b in range(1, n+1):
        if nodes[a][b] != INF or nodes[b][a] != INF:
            _count +=1
    if _count == n:
        result_count +=1 
print(result_count)
"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
