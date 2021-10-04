import sys

# n, m, nl = sys.stdin.readlines().strip()
n, m, nl = 4, 6, [19, 15, 10, 17]

end = max(nl)
start = 0

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2 # 오버플로우 발생할 수 있는 버그가 있다.  start + (end- start)//2를 사용 할것, 즉 자료형을 초과하지 않는 중앙 위치 계산
    for x in nl:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid -1
    else:
        print(mid)
        result = mid
        start = mid +1
    
print(result)