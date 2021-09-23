"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, 
    compute how much water it can trap after raining.

    exmaple:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
        In this case, 6 units of rain water (blue section) are being trapped.
"""

def trap(height):
    answer = 0 
    start_pointm = 0
    mem_start = height[start_point]
    end_point = len(height) -1
    mem_end = height[end_point]
    
    while start_point != end_point:
        # start를 기준으로 줘 보자! 
        print(f" start_point != end_point {start_point != end_point}/ {start_point},{end_point}")
        if height[start_point] <= height[end_point]:
            mem_end = height[end_point]
            start_point += 1 
        else:
            mem_start = height[start_point]
            end_point -=1

        if mem_start > height[start_point] and mem_start != 0:
            answer += mem_start-height[start_point]

        if mem_end < height[end_point] and mem_end != 0:
            answer += height[end_point] - mem_end
        
    return answer

if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(trap([4,2,0,3,2,5])) # 9
    print(trap([0,2,0])) # 0

"""
    1. 투 포인터를 최대로 이동 O(n)
    volume = 0
    left, right = 0, len(height) -1
    left_max, right_max = height[left], height[right]
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if left_max <= right_max:
            volume += left_max - height[left]
            left +=1 
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
    2. 스택 쌓기
    stack = []
    volume = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                braek
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
        stack.append(i)
    return volume
"""