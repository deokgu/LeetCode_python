n = int(input())

input_list = []
for _ in range(n):
    input_list.extend(input().split(" ")) # 앞에서 부터 나감 

out_list = sorted(input_list, key = lambda x: (x.split("-")[0], int(x.split("-")[1]))) # 앞에서 부터 확인 

wait_list = [] # 뒤에서 부터 나감
if len(input_list) == 0:
    print("BAD")

while input_list:
    go_str = input_list.pop(0) # 앞에서 부터 나감

    if go_str != out_list[0]:
        wait_list.append(go_str) # 뒤에 추가됨
    else:
        # go_str == out_list[0]:
        out_list.pop(0) # 앞에 사람 나감
        if len(wait_list) >= 1: # 다음 순서가 있을경우 
            while wait_list:
                if len(out_list) >= 1 and wait_list[-1] == out_list[0] :
                    wait_list.pop()
                    out_list.pop(0)
                else:
                    break

if len(wait_list) == 0 and len(out_list) == 0:
    print("GOOD")
else:
    print("BAD")

"""
1
G-555 B-203 A-102 A-44 C-719
"""