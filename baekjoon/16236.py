from collections import deque

def bfs(x, y, n, board):

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    visited, need_visit = list(), deque()

    need_visit.append([x,y])
    board[x][y] = 0

    while need_visit:
        i, j = need_visit.popleft()

        for n in range(4):
            tmp_x = i + mx[n]
            tmp_y = j + my[n]

            if tmp_x < 0 or tmp_y < 0 or tmp_x >= n or tmp_y >= n:
                continue


    print(board)


if __name__ == "__main__":
    
    n = int(input())

    board = [[] for _ in range(n)]

    for i in range(n):
        tmp = map(int, input().split())
        board[i].extend(tmp)

   
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                x, y = i, j
        

    bfs(x, y, n, board)