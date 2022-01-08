from collections import deque

def bfs(graph, start):
    visited, need_visit = [], deque()

    need_visit.append(start)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}

ans = bfs(graph, 'A')
print(ans)