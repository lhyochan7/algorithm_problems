from collections import deque

def bfs1(graph, start):
    visited, need_visit = list(), deque()

    need_visit.append(start)

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n)]

    for i in range(n):
        temp = input().split()
        graph[i].extend(temp)
    

    print(graph)

'''
    for x in range(n):
        for y in range(n):
            if 
'''