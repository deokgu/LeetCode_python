# https://github.com/python/cpython/blob/main/Lib/bisect.py#L63
# n, x = map(int, input().split())
# nums = list(map(int, input().split())

# n, x, nums = 7, 3, [1,1,2,2,2,2,3]
n, x, nums = 7, 4, [1,1,2,2,2,2,3]

# start = 0
# end = len(a)
# while start <end:
#     mid = (start+end)//2
#     if nums[min] < x:
#         start = mid + 1
#     else:
#         hi = mid

import bisect
index = bisect.bisect_left(nums, x)
right_index = bisect.bisect_right(nums, x)
if right_index == index:
    print(-1)
else:
    print(right_index - index)




