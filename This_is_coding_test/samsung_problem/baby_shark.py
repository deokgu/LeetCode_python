from collections import deque
n = int(input)

graph = []
eat_list = []
for x in range(n):
    check_list = list(map(int, input().split()))
    for x in eat_list:
        if x == 9 or x == 0:
            continue
        else:
            eat_list.append(x)
    if 9 in check_list:
        nine_index = [x, check_list.index(9)]
    graph.append(check_list)

print(eat_list)
print(nine_index)

temp = deque()
move = [[-1,0], [0, -1], [1,0], [0,1]]

def dfs():
    eating_size = 2
    step = 0
    temp.append(nine_index.append(eating_size, step))
    while temp:
        x, y, size, step = temp.popleft()
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            
            if graph[nx][ny] == 1 or 
dfs()

temp.append(nine_index.append(1))