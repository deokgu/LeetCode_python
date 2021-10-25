# https://www.acmicpc.net/problem/14888
from itertools import combinations
n = int(input())

nums = list(map(int, input().split()))

calc = list(map(int, input(). split()))

# 식 List 만들기
plus = lambda x, y : x+y
sub = lambda x, y : x-y # subtraction
multi = lambda x, y : x*y
div = lambda x, y : x/y

calcs = []
for i, calc_temp in zip(calc, [plus, sub, multi, div]):
    for _ in range(i):
        calcs.append(calc_temp)
print(calcs)
for x in list(combinations(calcs, 2)):
    print(x)


# answer = []
# def 
# while True:
#     for calc in range(calcs):
#         temp = 

