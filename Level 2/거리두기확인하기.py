import queue

# 상 하 좌 우
D = ((-1,0), (1,0), (0,-1), (0,1))

def bfs(place,row,col):
    visited = [[False for _ in range(len(place))] for _ in range(len(place))]
    q = queue.Queue()
    visited[row][col] = True
    q.put((row,col,0))
    
    while q:
        curr = q.get()
    
        # 거리가 2를 넘으면 manhattan distance을 초과하면 무시하라
        if curr[2] > 2:
            continue
        # 시작 위치가 아니면서, 다른 P를 만났을 때
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P' :
            return False
    
        for i in range(4):
            new_row = curr[0] + D[i][0]
            new_col = curr[0] + D[i][1]
            
            if new_row < 0 or new_row > 4 or new_col < 0 or new_col > 4:
                continue
            if visited[new_row][new_col]:
                continue
            if place[new_row][new_col] == 'X':
                continue
                
            visited[new_row][new_col] = True
            q.put((new_row,new_col, curr[2]+1))
            
            
    return True
            
    
def check(place):
    for r in range(len(place)):
        for c in range(len(place)):
            if place[r][c] == 'P':
                # 거리두기를 안할 경우 하나라도 있으면 
                if bfs(place,r,c) == False:
                    return False
                
    return True
                
    
    

def solution(places):
    answer = []
    
    for place in places:
        
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer