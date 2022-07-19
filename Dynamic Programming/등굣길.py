def solution(m, n, puddles):
    answer = 0
    
    table = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                table[i][j] = 1
            else:
                if [j, i] in puddles:
                    continue
                else:    
                    table[i][j] = table[i-1][j] + table[i][j-1] 
                
    print(table[-1])
    answer = max(table[-1])
    
    return answer % 1000000007