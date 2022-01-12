from collections import deque

def bfs(graph, start):
    
    visited, need_visit = list(), deque()
    
    # 시작 노드와 1번째 노드에서부터의 거리 설정
    need_visit.append([start,1])
    
    # 방문 여부 확인 0이면 미방문
    visit = [0] * len(graph)
    
    while need_visit:

        # print(need_visit)
        # print(visited)
        node, count = need_visit.popleft()
        
        # 미방문했던 node 일 경우
        if visit[node-1] == 0:
            # 방문으로 변경
            visit[node-1] = 1

            # 방문에 노드와 root 노드에서부터의 거리 저장
            visited.append([node, count])   

            # adjacent node들 모두 추가
            layer = []
            layer.extend(graph[node])
            
            count += 1
            for l in layer:
                need_visit.append([l, count])
    
    return visited


def solution(n, edge):
    answer = 0
    
    graph = {node: [] for node in range(1,n+1)}
    
    # 양방향 그래프 설정
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
        
    visited = bfs(graph, 1)
    
    # 1번째 노드에서부터의 거리를 list에 저장
    temp = list()
    for visit in visited:
        temp.append(visit[1])
        
    # list에서 최대 거리 숫자 세기
    for t in temp:
        if t == max(temp):
            answer += 1
    
    return answer