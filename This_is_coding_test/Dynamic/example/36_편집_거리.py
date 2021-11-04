import copy

str_A = list(input())
str_B = list(input())

dp = [0] * len(str_B)
print(str_A, str_B)
for x in range(-1, -len(str_B), -1):
    if str_A[x] != str_B[x]:
        index = x
        break

print(index)
cindex = index
def dfs(_str, index, cindex, count, type ="insert"):
    print(f"len(str_A) {len(str_A)} index {index} cindex {cindex} count {count} type {type}")
    if -len(str_A) == cindex:
        return count
    elif -len(str_A) > cindex and len(_str) == 0:
        count = int(1e9)
        return count

    count = + 1
    if type == "insert":
        _str.insert(index +1, str_A[cindex])
        cindex -= 1
        index -= 1
    elif type == "remove":
        _str.remove(_str[index])
        index += 1
    elif type == "replace":
        _str[index] = str_A[index]
        cindex -= 1
        index -=1 
    print(_str)
    dfs(copy.deepcopy(_str), index, cindex, count ,"insert")
    dfs(copy.deepcopy(_str), index, cindex, count ,"remove")
    dfs(copy.deepcopy(_str), index, cindex, count ,"replace")

start_insert = dfs(copy.deepcopy(str_B), index, cindex, 0 ,"insert")
start_remove = dfs(copy.deepcopy(str_B), index, cindex, 0 ,"remove")
start_replace = dfs(copy.deepcopy(str_B), index, cindex, 0 ,"replace")

print(min(start_insert, start_remove, start_replace))

"""
cat
cut

sunday
saturday

"""