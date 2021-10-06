# x = int(input())
x = 4 

# _list = list(map(int, input().split()))
_list = [1,3,1,5] 

# leetcode 198

d = [_list[0], max(_list[0], _list[1])]

for i in range(2, len(_list)):
    # d.append(max(d[i-1], d[-2] +_list[i]))
    
    # 공강복잡도를 더 낮춘다고 하면?
    d.append(max(d[1], d[0] +_list[i]))
    d.pop(0)

    # list d 를 안쓴다면 # see answer
# a = _list[0]
# b = max(_list[0], _list[1])
#    for 
#   a, b = b, max(b, a+_list[i])
#reutrn b

print(d[1])


