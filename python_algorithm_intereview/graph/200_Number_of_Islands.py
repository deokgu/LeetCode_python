"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
 return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

import time
# 312ms, 16.9 MB
def numIslands(grid: list[list[str]]) -> int:
    # FIX: 예외 처리    
    if not grid:
        return 0

    def dfs(x, y):
        # if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) \
        #     or grid[x][y] != "1":
        #     return

        # grid[x][y] = "0"
        # dfs(x+1, y)
        # dfs(x-1, y)
        # dfs(x, y+1)
        # dfs(x, y-1)
        # Fix leet code :  264ms, 16.9MB tey, expte로 구현가능함
        grid[x][y] = "0"
        if x+1 < len(grid) and grid[x+1][y] == "1":
            dfs(x+1, y)
        if x-1 >= 0 and grid[x-1][y] == "1":
            dfs(x-1, y)
        if y+1 < len(grid[0]) and grid[x][y+1] == "1":
            dfs(x, y+1)
        if y-1 >= 0 and grid[x][y-1] == "1":
            dfs(x, y-1)

    answer = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "1":
                dfs(x, y)
                answer += 1

    return answer

if __name__ == "__main__":
    print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


