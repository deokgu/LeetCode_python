# https://www.acmicpc.net/problem/6051

"""
모범생 현수는 코딩하는 시간을 늘리기 위해 타임 머신을 구매 했다. 현수는 정상적으로 문제를 코딩하거나 (타임 머신을 사용하지 않고), 과거의 임의의 지점으로 시간여행 할 수 있다.  미래로 시간 여행 할 수 없으며, 과거로 가면 새로운 미래가 진행된다.

현수는 자유롭게 문제를 풀거나 과거로 돌아가면서 자신이 푼 문제 목록을 기록한다. 과거로 돌아가면 과거 이전까지 풀었던 문제 목록만 남는다.

현수는  기록 되어 있는 문제 목록 중 가장 최근에 푼 문제 번호를 알고 싶다. (가장 최근에 푼 문제가 없다면 -1을 출력)

매 쿼리마다 문제 목록에 기록되어 있는 가장 최근에 푼 문제를 출력하는 프로그램을 작성하시오.

현수는 개인의 타임라인 관점에서 연속적인 업데이트를 나타내는  N (1 <= N <= 80,000) 개의 쿼리 Qi(1...N) 를 제공한다.

각 쿼리는 한 줄의 입력이다. 각 줄은 하나의 문자 c ( 'a', 's', 't' 중 하나)로 시작한다. c가 'a'또는 't' 이면 c 다음에 공백과 정수 K가 주어진다. (1 <= K <= 1,000,000)

c가 'a' 이면 현수는 문제 번호가 K인 문제를 풀고 문제 목록에 기록 한다.

c가 's' 이면 현수는 가장 최근에 작성한 문제 목록을 삭제한다.

c가 't'이면, 현수는 K 번째 쿼리 직전까지 시간을 거슬러 올라 간다. 즉, 현수는 K-1번째 쿼리와 K번째 쿼리 사이로 시간 여행한다. (입력을 위해 예제 입력 참조). K 쿼리  바로 전에 있던 푼 문제 목록으로 되돌아 간다.

이해를 돕기 위해 아래에 푼 문제 목록과 12개의 쿼리, 각 쿼리에 대한 출력결과가 주어진다.  
"""
import sys
input = sys.stdin.readline

n = int(input())
q_list = list([[-1]])
for _ in range(n):
    input_q_str = input()
    if input_q_str[0]  == "s":
        if q_list:
            temp_list= q_list[-1][:]
            temp_list.pop()
            q_list.append(temp_list)
    else:
        q, num = input_q_str.split(" ")
        if q == "t":
            if q_list:
                temp_list= q_list[int(num)-1][:]
                q_list.append(temp_list)
        else: # q == "a"
            if q_list:
                temp_list= q_list[-1][:]
                temp_list.append(num)
                q_list.append(temp_list)
            else:
                q_list.append([num])
    # print(q_list[-1][-1])
    if len(q_list[-1]) == 0:
        print(-1)
    else:
        print(q_list[-1][-1])



"""
12
a 5
a 3
a 7
s
t 2
a 2
t 4
a 4
s
t 7
s
s
"""