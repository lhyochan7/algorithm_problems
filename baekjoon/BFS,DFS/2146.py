from collections import deque

from sklearn.utils import check_X_y

def bfs(graph, start, n):
    visited, need_visit = list(), deque()

    need_visit.append(start)

    # Left Down Right Up
    cx = [-1, 0, 1, 0]
    cy = [0, 1, 0, -1]
    
    while need_visit:
        x, y = need_visit.popleft()

        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if [nx, ny] not in visited and graph[nx][ny] == 1:
                visited.append([nx,ny])
                need_visit.append([nx, ny])
                #print(graph[x][y], end=' ')

    return visited

#%%
if __name__ == '__main__':
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        temp = map(int, input().split())
        a = []
        a.extend(temp)

        for j, value in enumerate(a):
            graph[i][j] = value

    islands = {}

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                visited = bfs(graph, [i,j], n)
                visited = sorted(visited)
                print(visited)
                islands.update(visited)

    print(graph)
