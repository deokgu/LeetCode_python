from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b)
    
# n, m, k, x, node= 4, 4, 2, 1, [[1,2],[1,3], [2,3], [2,4]]
n= 10
is_= [0 for _ in range(n+1)]

q = deque([x])
q.append(x)
while q:
    s = q.popleft()
    for b in node[s]:
        if is_[b] == 0:
            is_[b] = is_[s] + 1
        q.append(b)


is_find = False
for n in range(len(is_)):
    if is_[n] == k:
        print(n)
        is_find = True
if not is_find:
    print(-1)

"""
import sys
from collections import deque
 
input = sys.stdin.readline
 
n, m, k, x = map(int, input().split())
visited = [False] * (n + 1)
 
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
 
answer = list()
q = deque()
q.append((x, 0))
while q:
    town, count = q.popleft()
    if count == k:
        answer.append(town)
    elif count < k:
        for con in path[town]:
            if not visited[con]:
                visited[con] = True
                q.append((con, count + 1))
 
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)
"""
"""
4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4


4 4 2 1
1 2
1 3
2 3
2 4
"""