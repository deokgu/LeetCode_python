# https://www.acmicpc.net/problem/18353

n = int(input())

powers = list(map(int, input().split()))


# min_num = powers[-1]
# _count = 0
# for i in range(n-1, 0, -1):
#     # print(f"i {i}")
#     # print(f"min_num {min_num}")
#     # print(f"powers[i-1] {powers[i-1]}")
#     # print(f"powers[i] {powers[i]}")
#     if powers[i-1] <= min_num:
#         del powers[i-1]
#         _count += 1
#     else:
#         min_num = powers[i-1]
#     # print(powers)
# print(_count)

# dp = []
# _count = 0
# while len(powers) > 0:
#     power = powers.pop(0)
#     # print(power)
#     # print(f"count {_count}")
#     # print(f"powers {powers}")
#     if len(powers) > 0 and power > max(powers):
#         dp.append(power)
#     else:
#         _count += 1
# print(_count-1)


# _count = 0
# _index = 0
# while _index < len(powers) -1:
#     # print(f"_index {_index}") 
#     # print(f"_count {_count}") 
#     # print(f"powers[_index] {powers[_index]}")
#     if powers[_index] > max(powers[_index+1:]):
#         None
#     else:
#         _count += 1
#     _index+=1
# print(_count)



# print(powers)
dp = [1] * n
# print(f"dp {dp}")

for i in range(1, n):
    for j in range(i):
        if powers[i] < powers[j]:
            dp[i] = max(dp[i], dp[j] +1)
print(n - max(dp))



"""
9
15 11 17 2 1 8 5 4 4 #5 

8
15 11 4 8 5 3 2 4 # 3 

7
15 11 7 7 9 7 7  # 3 
"""