import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

list_food = []
for _ in range(n):
    list_food.append(list(map(int, input().split())))
list_now_food = [[5 for _ in range(n+1)] for _ in range(n+1)] # 처음 양분은 5만큼

list_is_tree = [[ [] for _ in range(n+1)] for _ in range(n+1)] # # 현재 나무가 위치한 x, y
for _ in range(m):
    x, y, z = map(int, input().split())
    list_is_tree[x][y].append(z)

for _ in range(k):
    for x in range(n):
        for y in range(n):
            is_tree = list_is_tree[x][y]
            num_temp_food = list_now_food[x][y]

            for i in range(is_tree):
                need_food = is_tree[i]
        
            if num_temp_food >= need_food:
                list_tree[x][y][i] += 1
                num_temp_food -= need_food
                list_now_food[x][y] = num_temp_food
            else:
                remove_tree.extend(list_tree[x][y][i:])
                _count = len(list_tree[x][y][i:])
                list_tree[x][y] = list_tree[x][y][:i]
                for _ in range(_count):
                    list_is_tree.remove((x, y))
                break
        # 여름
        if remove_tree:
            list_now_food[x][y] += sum(remove_tree)//2

    # 가을
    if list_is_tree:
        add_tree = []
        for x, y in list_is_tree:
            if any([(x % 5)==0 for x in list_tree[x][y]]) is True:
                move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]
                for dx, dy in move:
                    mx, my = x + dx, y + dy
                    if mx > 0 and my > 0 and mx <= 5 and my <= 5:
                        list_tree[mx][my].append(1)
                        add_tree.append((mx,my))
        list_is_tree.extend((add_tree))

    # 겨울
    for x in range(n):
        for y in range(n):
            list_now_food[x+1][y+1] += list_food[x][y]
print(len(list_is_tree))

"""
5 2 4
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
"""


