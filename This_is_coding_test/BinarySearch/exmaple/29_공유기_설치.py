## https://www.acmicpc.net/problem/2110
# 파라메트릭 서치
n, c = map(int, input().split())

nodes = []
for x in range(n):
    nodes.append(int(input()))   

# n, c ,nodes = 5, 3, [1, 2, 8, 4, 9] # 3

nodes.sort()

start = 1
end = nodes[-1] - nodes[0]

_max = 0
while end >= start:
    gap = (start+end)//2

    # print(f"end {end}, start {start}")
    _count = 1
    node = nodes[0]
    for x in range(1, n):
        if nodes[x] >= gap + node:
            # print(f"{nodes[x]} > = {gap+node} {gap}  {node}")
            node= nodes[x]
            _count += 1

    # if _count >= c:
    #     if gap >= _max:
    #         _max = gap
    # print(f"_count {_count}, c {c}, _max {_max}, gap {gap}")
    
    if _count >= c:
        start = gap +1
        _max = gap
    else:
        end = gap -1
    # import time
    # time.sleep(0.5)
print(_max)

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
