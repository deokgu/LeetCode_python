n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))

B = []
for _ in range(n):
    B.append(int(input()))

i = 0
count_list= []
is_fail = False
pass_count = 0
while i < n:
    print(i)
    if A[i] != B[i]:
        count = 1 
        while True:
            if A[i] == B[i]:
                break
            if A[i] in B:
                find_index = B.index(A[i])
                A[find_index], A[i] = A[i], A[find_index]
                count += 1
                if count > n:
                    is_fail = True
                    break
            else:
                is_fail = True
                break
        count_list.append(count)
    if is_fail:
        break
    else:
        i += 1
if (A == B) and not is_fail:
    print(len(count_list), max(count_list))
else:
    print(0, -1)


"""
5
5
1
4
2
3
2
5
3
1
4
"""