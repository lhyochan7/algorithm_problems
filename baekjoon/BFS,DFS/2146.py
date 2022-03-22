from collections import deque

from sklearn.utils import check_X_y

def bfs(graph, start, n):
    visited, need_visit = list(), deque()

    need_visit.append(start)

    cx = [-1, 0, 1, 0]
    cy = [0, 1, 0, -1]
    

    while need_visit:
        x, y = need_visit.popleft()

        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            visited.append((x,y))
            need_visit.append((nx, ny))

            print(graph[x][y], end=' ')
            print('-------------------------')


    # while need_visit:
    #     node = need_visit.popleft()

    #     if node not in visited:
    #         visited.append(node)
    #         need_visit.extend(graph[node])

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


#%%
    from collections import deque
    d = deque()

    e = (1,2)

    d.append(e)
    x, y = d.popleft()
    print(x, y)
#%%

    islands = {}

    for i in range(n):
        for j in range(n):
            visited = bfs(graph, (i,j), n)
        #visited = sorted(visited)
        #print(visited)
        #islands.add(visited)

    print(graph)
    print(islands)

# %%
