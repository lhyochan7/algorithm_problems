# 
# ## My Method
# 
# from collections import deque

# def dfs(graph, start):
#     visited, need_visit = list(), deque()
#     need_visit.append(start)
    
#     while need_visit:
#         print("visited = %s    need_visit = %s" %(visited, need_visit))
        
#         airport = need_visit[-1]
        
#         if airport not in graph:
#             visited.append(need_visit.popleft())
#             continue
        
#         if airport not in visited:
#             visited.append(need_visit.pop())
            
#             temp = ["".join(x) for x in graph[airport]]
#             temp.sort(reverse=True)
            
#             need_visit.extend(temp)
#         else:
#             visited.append(need_visit.pop())
            
    
    
#     return visited
    

    
# def solution(tickets):
#     answer = []
    
#     tickets.sort(key=lambda x: (x[0], x[1]))
    
#     graph = {ticket[0]: [] for ticket in tickets}
    
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
        
#     for key in graph.keys():
#         graph[key].sort(reverse=True)
#     print(graph)
    
#     answer = dfs(graph, "ICN")
        
#     return answer


from collections import deque

def dfs(graph, start):
    visited, need_visit = list(), deque()
    need_visit.append(start)
    
    while need_visit:
        print("visited = %s    need_visit = %s" %(visited, need_visit))
        
        airport = need_visit[-1]
        print(need_visit[-1])
        
        if airport not in graph or not graph[airport]:
            print(need_visit[-1])
            visited.append(need_visit.pop())
        else:
            x = graph[airport].pop()
            print(x)
            need_visit.append(x)
            
    
    print(visited)
    return visited[::-1]
    

    
def solution(tickets):
    answer = []
    
    tickets.sort(key=lambda x: (x[0], x[1]))
    
    graph = {ticket[0]: [] for ticket in tickets}
    
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        
    for key in graph.keys():
        graph[key].sort(reverse=True)
        
    print(graph)
    
    answer = dfs(graph, "ICN")
        
    return answer