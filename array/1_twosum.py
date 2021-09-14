# class Solution:

def twoSum(nums: "list(int)", target: int) -> list[int]:
    # print(dir(list))
    for index, num in enumerate(nums):
        if (target-num) in nums[index+1:]:
            return index, (nums[index+1:].index(target-num)) +index+1

if __name__ == "__main__":
    print(twoSum([3,3], 6)) # (0,1)
