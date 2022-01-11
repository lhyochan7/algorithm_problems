from collections import deque

def bfs(graph, start):
    
    visited, need_visit = list(), deque()
    
    need_visit.append(start)
    
    layer = []
    
    layer.extend(graph[start])
    count = 1
    
    while need_visit:
        print(need_visit)
        print(visited)
        node = need_visit.popleft()
        
        if node not in visited:
            visited.append([node,count])
            need_visit.extend(graph[node])
            count += 1
    
    
    return visited


def solution(n, edge):
    answer = 0
    
    graph = {node: [] for node in range(1,n+1)}
    
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
        
    print(graph)
    visited = bfs(graph, 1)
    
    print(visited)
    return answer