from collections import deque

# Solve using DFS
def dfs(graph, start):
    visited, need_visit = list(), deque()
    
    need_visit.append(start)
    
    while need_visit:
        # print("visited = ", visited)
        # print("need visit = ", need_visit)
        node = need_visit.pop()
        
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    print(visited)
    return visited


def solution(n, computers):
    answer = 0
    
    # node의 idx 번호를 key로 dict 만들고 value는 빈 list로 초기화
    graph = {node: [] for node in range(n)}
    
    # 자신을 제외하고 그래프로 추가
    for i, computer in enumerate(computers):
        for j, conn in enumerate(computer):
            if i!=j and conn == 1:
                graph[i].append(j)
                
    print(graph)
    
    # 모든 node를 출발점으로 한번씩 순회 하고, 순회 경로 정렬 (같은 경로를 파악하기 위해)
    paths = map(sorted, [dfs(graph,node) for node in graph])
    
    # string으로 만듬을 통해서 중복 값(경로) 제거
    x = len(set(["".join(map(str, path)) for path in paths]))
    
    print(x)
    return answer
    
    
