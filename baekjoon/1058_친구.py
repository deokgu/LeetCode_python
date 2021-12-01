
n = int(input()) # people

INF = int(1e9)
graph = [[INF]*(n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0
    temp = [0 if x=="N" else 1 for x in list(input())]
    for j, temp_num in enumerate(temp):
        if temp_num == 1:
            graph[i][j] = 1

for j in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])
            
answer= 0
for temp in graph:
    answer = max(answer, temp.count(1)+ temp.count(2))
print(answer)