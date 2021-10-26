from collections import deque
from copy import deepcopy
import pprint

def check_pass(board, bx, by, fx = None, fy = None):
    n = len(board)
    if bx <0 or by < 0 or bx >=n or by >=n :
        return False
    if fx is not None:
        if  fx <0 or fy <0 or fx >=n or fy >=n:
            return False
        if board[fx][fy] == 0 and board[bx][by] == 0:
            return True
        else:
            return False
    if board[bx][by] == 0:
        return True
    else:
        return False

def solution(board):
    n = len(board)
    board_true = deepcopy(board)
    move = ((-1,0), (1,0), (0,-1), ((0,1)))
    def bfs(bx, by, fx, fy):
        temp = deque()
        temp.append((bx,by,fx,fy))
        while temp:
            # pprint.pprint(board)
            bx, by, fx, fy = temp.popleft()
            for i in range(8):
                print(f"in i {i}")
                if i < 4:
                    dbx = bx + move[i][0]
                    dby = by + move[i][1]
                    dfx = fx + move[i][0]
                    dfy = fy + move[i][1]
                    if i == 0:
                        if not check_pass(board, dbx, dby, dfx, dfy):
                            continue
                    elif i == 1:
                        if not check_pass(board, dbx, dby, dfx, dfy):
                            continue
                    elif i == 2:
                        if not check_pass(board, dbx, dby):
                            continue
                    elif i == 3:
                        if not check_pass(board, dfx, dfy):
                            continue
                if i >= 4:
                    print("!!!!!!!!!!")
                    import time
                    time.sleep(0.5)
                    if bx == fx:
                        print("~~~~~~")
                        if i == 4 and i == 5: # 위쪽에서 시계, 반시계
                            if board_true[bx-1][by] == 0 and board_true[fx][fy-1] == 0:
                                print("@@@@@@@@") 
                                if i == 4: # 시계
                                    dbx, dby = bx, by
                                    dfx = fy
                                    dfy = fx
                                else: # 반 시계
                                    dfx, dfy = fx, fy
                                    dbx = bx +1
                                    dby = by +1

                        elif i == 6 and i == 7: # 아래쪽에서 좌, 우
                            if board_true[bx+1][by] == 0 and board_true[fx][fy+1] == 0:
                                if i == 6:
                                    dfx, dfy = fx, fy
                                    dbx = by
                                    dby = bx
                                else:
                                    dbx, dby = bx, by
                                    dfx = fx -1
                                    dfy = fy -1 
                    else: # "vartical"
                        if i == 4 and i == 5: # 왼쪽에서 시계, 반시계
                            if board_true[bx][by+1] == 0 and board_true[fx][fy+1] == 0:
                                if i == 4:
                                    dbx, dby = bx, by
                                    dfx = fy
                                    dfy = fx
                                else:
                                    dfx, dfy = fx, fy
                                    dbx = bx +1
                                    dby = by +1
                        elif i == 6 and i == 7: # 오른쪽에서 시계, 반시계
                            if board_true[bx][by-1] == 0 and board_true[fx][fy-1] == 0:
                                if i == 6:
                                    dfx, dfy = fx, fy
                                    dbx = by
                                    dby = bx
                                else:
                                    dbx, dby = bx, by
                                    dfx = fx -1
                                    dfy = fy -1

                if dbx <0 or dby < 0 or dfx <0 or dfy <0 or dbx >=n or dby >=n or dfx >=n or dfy >=n:
                    continue
                pprint.pprint(board)
                # if board[dfx][dfy] == 0 or board[dbx][dby] == 0:

                print(f"IN!!!!")
                board[dbx][dby] = board[bx][by] +1
                board[dfx][dfy] = board[bx][by] +1
                temp.append((dbx, dby, dfx, dfy))
                pprint.pprint(board)
            
    bfs(0,0,0,1)
    answer = board[n-1][n-1]
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7  