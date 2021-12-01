import heapq
from typing import NewType
INF = int(1e9)

# n, m, start, load = 3, 2, 1, [[1,2,4], [1,3,2]]
# print(load)
n, m, start = map(int, input().split())

# grap = [[] for i in range(n+1)]
grap = []
for _ in range(m):
    x, y, z = map(int, input().split())
    # grap[x].append((y,z))
    grap.append((x,y,z))

distance = [INF] * (n+1)

# def dijkstra(start):
#     q = []
#     # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in grap[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# # 수행
# dijkstra(start)

# count = 0
# print(distance)
# max_distanceance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distanceance = max(max_distanceance,d)
    
# print(count -1 , max_distanceance)

def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            node = grap[j][0]
            next_node = grap[j][1]
            cost = grap[j][2]
            if distance[node] != INF and distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node]+ cost
                if i == n-1:
                    return True
    return False   

bf(start)
print(distance)


"""
3 2 1 
1 2 4
1 3 2
"""