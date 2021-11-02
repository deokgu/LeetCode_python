# T = int(input())

# n, m = [], []

# maps = []

n, m = 3, 4

maps = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]

node = [[0 for x in range(m)] for x in range(n)]
for y in range(n):
    node[y][0] = maps[y][0]

def check_map(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0
    else:
        return node[x][y]

for y in range(1, m):
    for x in range(n):
        node[x][y] = maps[x][y] + max(check_map(x-1, y-1), check_map(x, y-1), check_map(x+1, y-1))

print(node[n-1][m-1])