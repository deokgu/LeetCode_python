# class Solution:

def twoSum(nums: "list(int)", target: int) -> list[int]:
    # # print(dir(list))
    # for index, num in enumerate(nums):
    #     if (target-num) in nums[index+1:]:
    #         return index, (nums[index+1:].index(target-num)) +index+1
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

if __name__ == "__main__":
    print(twoSum([3,3], 6)) # (0,1)
    print(twoSum([3, 2, 4], 6)) # (1,2)
    print(twoSum([2, 7, 11, 15], 9)) # (0,1)

"""
    시간 복잡도: O(n) -> O(n2) in의 시간 복잡도가 O(n)이라 전체 시간 복잡도는 O(n^2)이다
    공간 복잡도: O(n)

    Runtime: 660 ms, faster than 35.62% of Python3 online submissions for Two Sum.
    Memory Usage: 14.7 MB, less than 98.26% of Python3 online submissions for Two Sum.

    1. 브루트 포스로, Brute-Force(모든 조합을 더해서 일일이 확인해 보는) / 시간 복잡도 O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    2. in을 이용한 탐색 / 시간 복잡도  O(n^2)
        for index, num in enumerate(nums):
            if (target-num) in nums[index+1:]:
                return index, (nums[index+1:].index(target-num)) +index+1

    3. 첫 번째 수를 뺀 결과 키 조회 / 시간 복잡도 O(n)
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target_num]

    4. #3 구조 개선(하나의 for 문) / 시간 복잡도 O(n)
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

    5. 투 포인터 이용
        left, rgith = 0, len(nums) -1
        while not left == right:
        if nums[left] + nums[right] < target:
            left += 1 
        elif nums[elft] + nums[right] > target:
            right -= 1
        else:
        return left, right 
        
        
        

"""
