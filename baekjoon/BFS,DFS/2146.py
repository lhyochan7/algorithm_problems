from collections import deque

def bfs(graph, start, n):
    visited, need_visit = list(), deque()

    need_visit.append(start)
    
    for x in range(n):
        for y in range(n):
            if y < 0 or y >= n or x < 0 or x >= n:
                continue

            print(graph[i][j], end=' ')
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
            # idx += 1
            # num = (i*n) + idx
            # print("n = %d  (%d, %d) = %d / num = %d" %(n, i, idx, j, num))
            # graph[num].append(j)

    islands = {}

    for i in range(n):
        for j in range(n):
            
            visited = bfs(graph, node, n)
        #visited = sorted(visited)
        #print(visited)
        #islands.add(visited)
            
    print(graph)
    print(islands)

# %%
