# https://www.acmicpc.net/problem/16234
import copy 
import pprint
from sys import meta_path
n, L, R = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

maps_is_true = [[0 for _ in range(n)] for _ in range(n)]
# pprint.pprint(maps_is_true)
# import sys
# sys.exit()
move = [(-1,0), (1,0), (0,-1), (0,1)]
def dfs(x, y, index):
    print(x,y,index)
    if x >= n or y >= n or x < 0 or y < 0:
        return
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            return
        pepoles = abs(maps[x][y] - maps[dx][dy])
        if L <= pepoles <= R:
            pprint.pprint(maps_is_true)
            maps_is_true[x][y] = index
            maps_is_true[nx][ny] = index
            dfs()
            # dfs(x, y+1, index))


def find_true():
    sum = 0 
    maps_trues = []
    for x in range(n):
        for y in range(n):
            if maps_is_true[x][y] == True:
                sum += maps_is_true[x][y]
                maps_trues.append

    mean = sum / len(maps_trues)
    for x, y in maps_trues:
        pass

answer = 0
for x in range(n):
    index = x+1
    for y in range(n):
        dfs(x, y, index)
    break
pprint.pprint(maps_is_true)  
pprint.pprint(maps)  

"""
2 20 50
50 30
20 40
"""