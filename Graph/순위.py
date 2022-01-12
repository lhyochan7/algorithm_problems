def solution(n, results):
    answer = 0
    
    winner_graph = {i: [] for i in range(1,n+1)}
    loser_graph = {i: [] for i in range(1,n+1)}
    
    for winner, loser in results:
        winner_graph[winner].append(loser)
        loser_graph[loser].append(winner)
        
    for i in range(1,n+1):
        # i한테 진 애들은 i를 이긴 애들한테도 진 것
        for winner in winner_graph[i]:
            loser_graph[winner].extend(loser_graph[i])
        # i한테 이긴 애들은 i한테 진애들한테 이긴 것
        for loser in loser_graph[i]:
            winner_graph[loser].extend(winner_graph[i])
            
    # Remove duplicates
    for i in range(1,n+1):
        winner_graph[i] = list(set(winner_graph[i]))
        loser_graph[i] = list(set(loser_graph[i]))
        
        
    print("winner graph = ", winner_graph)
    print("loser graph = ", loser_graph)
    
    for i in range(1,n+1):
        # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
        if len(winner_graph[i]) + len(loser_graph[i]) == n-1:   
            answer += 1
    
    return answer