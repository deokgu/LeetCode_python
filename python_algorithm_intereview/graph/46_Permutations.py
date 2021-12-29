"""
Given an array nums of distinct integers, return all the possible permutations.
 You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
""" 

# 36ms, 14.3 mb
def permute(nums: "list[int]") -> list[list[int]]:
    result = []
    pre_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(pre_elements[:])
        
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            pre_elements.append(e)
            dfs(next_elements)
            pre_elements.pop()

    dfs(nums)
    return result

    # 28 ms 
    # res = []
    # l = len(nums)
    # def helper(cur = []):
    #     if len(cur) == l:
    #         res.append(cur.copy())
    #         return
    #     for i in nums:
    #         if i not in cur:
    #             cur.append(i)
    #             helper(cur)
    #             cur.pop()
    # helper()
    # return res
    
    # import itertools
    # list(map(list, tiertools.permutations(nums)))


if __name__ == "__main__":
    print(permute([1,2,3]))