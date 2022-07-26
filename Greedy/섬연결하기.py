from collections import deque

def dfs(graph, start):
    visited, need_visit = list(), deque()
    need_visit.append(start)
    
    cost = 0
    
    while need_visit:
        node = need_visit.popleft()
        
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
        
    return visited


def solution(n, costs):
    answer = 0
    
    graph = {node : [] for node in range(n)}

    for line in costs:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    
    print(graph)
    
    temp = [dfs(graph, start) for start in graph]
    
    print(temp)
    
    return answer