
n, m = map(int, input().split()) # city, bus # 노드, 간선 수
INF = 1e9
q = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = list(map(int,input().split())) # start, end, cost
    q.append([a, b, c])

# 벨만 포드 알고리즘
def bf(start_point):
    dist[start_point] = 0
    for i in range(n):
        for j in range(m):
            node = q[j][0]
            next_node = q[j][1]
            cost = q[j][2]
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # 음수 순환이 존재 확인 
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])

