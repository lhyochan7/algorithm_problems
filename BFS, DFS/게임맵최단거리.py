from collections import deque

def dfs(visited, maps, row, col):
    need_visit = deque()
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[row][col] = True
    need_visit.append((row, col))
    
    cnt = 1
    
    while need_visit:
        x, y = need_visit.pop()
        
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
                    
            # row ( len(maps) ), col ( len(maps[0]) ) length overflow
            if newX <= -1 or newX >= len(maps) or newY <= -1 or newY >= len(maps[0]):
                continue

            if not visited[newX][newY] and maps[newX][newY] == 1:
                visited[newX][newY] = True
                print(newX, newY)
                need_visit.append((newX, newY))
                cnt += 1
                
    return cnt
    

def solution(maps):
    answer = 0
    
    visited = [[False] * len(maps) for _ in range(len(maps[0]))]
    
    cntList = []
    for rowIdx in range(len(maps)):
        for colIdx in range(len(maps[0])):
            if not visited[rowIdx][colIdx] and maps[rowIdx][colIdx] == 1:
                #print(rowIdx, colIdx)
                cntList.append(dfs(visited, maps, rowIdx, colIdx))
    
    print(cntList)
    
    #answer = min(cntList)
    #print(maps)
    #print(visited)
    
    return answer