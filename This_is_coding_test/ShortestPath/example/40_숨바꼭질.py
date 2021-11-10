import heapq
from collections import deque
n = int(input())

nodes = [[] for _ in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)
print(nodes)

INF = int(1e9)
distance = [INF] * (n+1)

temp = deque()

for node in nodes[1]:
    temp.append(node)

while temp:
    distance[1] = 1
    node = temp.popleft()
    for i in nodes[node]:
        temp.append(i)
        distance[i] = min(distance[node] +1 , distance[i])
print(distance)
    

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, 1))
#     distance[1] = 0
#     while q:
#         dist, now = heapq.heappushpop(q)
#         if distance[now] < dist:
#             continue
#         for i in nodes[now]:
#             cost = dist + i
#             if 




"""
8
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""