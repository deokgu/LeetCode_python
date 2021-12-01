# https://www.acmicpc.net/problem/1865
import copy
for _ in range(int(input())):
    n, m, w = map(int, input().split()) #node, load, worm

    INF = int(1e9)
    dist = [INF] * (n+1)

    loads = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split()) #start, end, cost
        loads[s].append((e,t))
        loads[e].append((s,t))

    for _ in range(w):
        s, e, t = map(int, input().split()) #start, end, cost
        loads[s].append((e, -t))

    def bf(start, distance = []): 
        distance[start] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                for end, cost in loads[j]:
                    if distance[end] > distance[j] + cost: # 시작점이 주어지 않아 cycle만 체크하면 된다. distance[j] != INF 제거 
                        distance[end] = distance[j] + cost
                        if i == n:
                            return True
        return False

    if bf(1, dist):
        print("YES")
    else:
        print("NO")