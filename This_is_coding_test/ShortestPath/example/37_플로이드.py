n = int(input())
m = int(input())

nodes = [[int(1e9)]*(n+1) for _ in range(n+1)]
for x in range(1, n+1):
    nodes[x][x] = 0

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    if c < nodes[a][b]:
        nodes[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            nodes[a][b] = min(nodes[a][b], nodes[a][k] + nodes[k][b])

for node in nodes[1:]:
    for x in range(1, len(node)):
        x = node[x]
        if x == int(1e9):
            print(0, end =" ")
        else:
            print(x, end= " ")
    print()



"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""