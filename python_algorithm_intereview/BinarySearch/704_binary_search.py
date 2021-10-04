"""
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums: List[int], target: int) -> int:
    
    start= 0
    end = len(nums) -1
    
    answer =0
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:                 
            end  = mid -1
        else:
            start = mid +1
    return -1

"""
    1. 재귀 풀이
    def binary_search(lieft, right):
        if left <= right:
            mid = (left + rifht) //2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return -1
    return binary_search(0, len(nums) -1)

    2. 이진 검색 모듈
    import bisect
    index = bisect.bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
        
    3. index 풀이
    try:
        return nums.index(target)
    except ValuError:
        return -1
"""