from collections import deque

def bfs(graph, cost_table, K, start):
    visited, need_visit = list(), deque()
    
    need_visit.append(start)
    
    while need_visit:
        start, cost = need_visit.popleft()
        
        print("start, cost = ", start ,cost)
        for end, new_cost in graph[start]:
            if cost + new_cost <= K and cost + new_cost < cost_table[end-1]:
                cost_table[end-1] = cost + new_cost
                need_visit.append((end, cost_table[end-1]))
            print("end, new cost = ", end, cost_table[end-1])
    
    print(cost_table)
    
    return cost_table

def solution(N, road, K):
    answer = 0
    graph = {id: [] for id in range(1, N+1)}

    cost_table = [1000000000 for _ in range(N)]
    
    for start, end, cost in road:
        graph[start].append((end,cost))
        graph[end].append((start,cost))
        
    #print(cost_table)
    #print(graph)
    
    new_table = bfs(graph, cost_table, K, (1,0))
    
    for i in new_table:
        if i != 1000000000:
            answer += 1
        
    return answer