

def check_map(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0
    else:
        return node[x][y]

for y in range(1, m):
    for x in range(n):
        node[x][y] = max(check_map(x, y), check_map(x-1, y))

n = int(input())
