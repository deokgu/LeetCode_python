# https://www.acmicpc.net/problem/18243


n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    # graph[i+1][i+1] = 0
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)
for i in range(1, n+1):
    graph[i][i] = 0

for j in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])
# print(graph)

temp_str = ""
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] > 6:
            temp_str = "Big World!"
if len(temp_str) == 0:
    print("Small World!")
else:
    print(temp_str)
