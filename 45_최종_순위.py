# https://www.acmicpc.net/problem/3665

for _ in range(int(input())): # T
    n = int(input())

    # do
    t_list = list(map(int, input().split()))

    m = int(input())
    t = []

    temp= []    
    for x in range(len(t_list)):
        t[t_list[x]].append(temp[:])
        temp.append(t_list[x])
    print(t)
    for _ in range(m):
        a, b = map(int, input().split()) # a < b

        print(t)


    # # check
    # t_string = "".join([str(_) for _ in t_list])
    # print(t_list)
    # for b, a in m_check_list:
    #     print(b, a)
    #     print(t_string.find(str(b)))
    #     print(t_string.find(str(a)))
    #     if t_string.find(str(b)) > t_string.find(str(a)):
    #         pass
    #     else:
    #         t_list = "IMPOSSIBLE"

    # print(*t_list)
    
""" #   5 3 2 4 1
        2 3 1
        IMPOSSIBLE
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""