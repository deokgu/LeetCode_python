
# n = map(int, input().split())
# nums = list(map(int, input().split())
n, nums = 5, [-15,-6, 1,3,7] # 3 
# n, nums = 7, [-15,-4, 2, 8, 9, 13, 15] # 2
n, nums = 7, [-15, -4, 3, 8, 9, 13, 15] # -1
start = 0
end = len(nums)-1

while start <= end:
    is_end = True
    mid = start + (end-start)//2
    if nums[mid] == mid:
        break
    elif nums[mid] < mid:
        start = mid+1
    else:
        end = mid -1
    is_end = False
if not is_end:
    print(-1)
else:
    print(mid)
