"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(nums : list[int]): # -> list(list(int) 
    if len(nums) < 3:
        return []

    for num in nums:
        _list = []
        _list.append(num)
        _nums = nums[:]
        _nums.remove(num)
        i = 0
        while i < len(_nums)-1:
            _list.append(_nums[i])
            

            find_zero = nums[left] + nums[right]
        
if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
