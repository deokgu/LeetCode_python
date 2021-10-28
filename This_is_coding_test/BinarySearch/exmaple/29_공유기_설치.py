## https://www.acmicpc.net/problem/2110

# n, c = map(int, input().split())

# nodes = []
# for x in range(n):
#     nodes.append(int(input()))   

n, c ,nodes = 5, 3, [1, 2, 8, 4, 9] # 3

nodes.sort()

start = nodes[1] - nodes[0]
end = nodes[-1] - nodes[0]

while start <= end:
    mid_gap = start + (end-start)//2

    _count = 0
    for x in range(len(nodes)):
        if nodes[x] >= mid_gap + nodes[0]:
            _count += 1

    print(_count)
    print(mid_gap)
    if _count <= c:
        _max = mid_gap

    if mid_gap < _max:
        end = mid_gap -1
    elif mid_gap > _max :
        start = mid_gap +1
        
    values = nodes[0]
    print(f"end {end}, start {start}")
    print(values)
    break
print(mid_gap)

# node_gap = []
# for x in range(0, len(nodes)-1):
#     node_gap.append(nodes[x+1]-nodes[x])

# set_wifi = []
# for _ in range(c-1):
#     gap__max = node_gap.index(_max(node_gap))
#     set_wifi.insert(0, gap__max + 1)
#     node_gap[gap__max] = 0

# print(nodes[set_wifi[0]] - nodes[0])


# start = 0
# end = len(nodes) - 1
