# import heapq
from collections import deque
import copy 

T = int(input())

INF = int(1e9)
for _ in range(T):
    n = int(input())
    nodes = []
    for _ in range(n):
        nodes.append(list(map(int, input().split())))
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    distance[0][0] = nodes[0][0]
    move = [(-1,0), (1,0),(0, -1), (0,1)]
    def bfs(x, y):
        temp = deque()
        temp.append((x,y))
        while temp:
            x, y = temp.popleft()
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    continue

                if distance[x][y] + nodes[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + nodes[nx][ny]
                    temp.append((nx, ny)) 
                # if 0 <= nx < n and 0 <= ny < y:
    bfs(0,0)
    print(distance[n-1][n-1])

"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""