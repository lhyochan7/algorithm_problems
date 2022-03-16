from collections import deque

def bfs(graph, start):
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
    k = int(input())

    graph = {key:[] for key in range(1, n+1)}

    for _ in range(k):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)

    #print(graph)

    answer = bfs(graph, 1)
    
    print(len(answer) - 1)