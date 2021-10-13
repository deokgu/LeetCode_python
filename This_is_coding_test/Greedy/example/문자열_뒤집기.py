
# s = input()
# s  = "0001100"
s  = "10101010111001"

temp = s[0]
_count = {temp: 1}
for x in s[1:]:
    if temp == x:
        continue
    else:
        temp = x
        _count[x] = _count.get(x, 0) + 1

print(min(_count.values()))
