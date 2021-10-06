"""
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        a = nums[0]
        b= max(a, nums[1])
        
        for x in range(2, len(nums)):
            a, b = b, max(b, a + nums[x])
        return b