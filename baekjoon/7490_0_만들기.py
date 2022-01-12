c = int(input())

def calc_values(temp_list, num_list):
    for i in range(len(num_list)-1):
        if i == 0:
            _str = str(num_list[i]) + temp_list[i] + str(num_list[i+1])
        else:
            _str = _str + temp_list[i] + str(num_list[i+1])
    return eval(_str.replace(" ", "")), _str

for _ in range(c):
    N = int(input())
    num_list = [x for x in range(1, N+1)]
    
    def dfs(temp_list):
        if len(temp_list) > N-1: # dfs 예외
            return

        if len(temp_list) == N-1: # 빽트레킹 포인트
            num, _str = calc_values(temp_list, num_list)
            if num == 0:
                result.append(_str)
                return

        for temp in ["+", "-", " "]:
            temp_list.append(temp)
            dfs(temp_list)
            temp_list.pop()

    temp_list = []
    result = []
    dfs(temp_list)
    for temp in sorted(result):
        print(temp)
    print()