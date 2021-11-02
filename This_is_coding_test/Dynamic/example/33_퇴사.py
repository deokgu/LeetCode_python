n = int(input())

sc = []
for _ in range(n):
    sc.append(list(map(int, input().split())))

total = [0 for _ in range(n+1)]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #  sc_time 5, money 50 index 5  i 0
    #   total[index] 0 total[i] 0 money 50  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #  sc_time 4, money 40 index 5  i 1
    #   total[index] 50 total[i] 0 money 40  [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0]
    #  sc_time 3, money 30 index 5  i 2
    #   total[index] 50 total[i] 0 money 30  [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0]
    #  sc_time 2, money 20 index 5  i 3
    #   total[index] 50 total[i] 0 money 20  [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0]
    #  sc_time 1, money 10 index 5  i 4
    #   total[index] 50 total[i] 0 money 10  [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0]
    #  sc_time 1, money 10 index 6  i 5
    #   total[index] 0 total[i] 50 money 10  [0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0]
    #  sc_time 2, money 20 index 8  i 6
    #   total[index] 0 total[i] 60 money 20  [0, 0, 0, 0, 0, 50, 60, 0, 0, 0, 0]
    #  sc_time 3, money 30 index 10  i 7
    #   total[index] 0 total[i] 0 money 30  [0, 0, 0, 0, 0, 50, 60, 0, 80, 0, 0]

sc_time, money = sc.pop()
for i in range(n-1,-1,-1):
    # print(i)
    if i + sc_time > n:
        total[i] = total[i+1]
    else:
        # print(f"sc_time {sc_time} total[i] {total[i]} money {money}  {total}")
        # print(f"sc_time {sc_time} money {money}")
        total[i] = max(money + total[i + sc_time], total[i+1])
        sc_time, money = sc.pop()
print(max(total))

for i, (sc_time, money) in enumerate(sc):
    if i + sc_time <= n:
        index = sc_time+i 
        print(f" sc_time {sc_time}, money {money} index {index}  i {i}")
        for j in range(sc_time, i+1):
            total[index] = max(total[index], total[i] + money)

# print(total[-2])

# total = [0, 0, 0]
# for i, (sc_time, money) in enumerate(sc):
#     if i + sc_time <= n:
#         print(money)
#         _count = 0
#         print(total)
#         time = (max(total[-1], total[-2] + money))


# sc = []
# for _ in range(n):
#     sc.append(list(map(int, input().split())))

# sc_dict = {}
# for i, (date, money) in enumerate(sc): 
#     key = date+i
#     if key in sc_dict.keys():
#         sc_dict[key].append(money)
#     else:
#         sc_dict[key] = [money]
# print(sc_dict)

# dp = [0 for x in range(n)]
# for i in range(n):
#     max_num = 0
#     if i in sc_dict.keys():
#         max_num = max(sc_dict[i])

    
#      = max(max_num, )

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

"""