import sys

N, M, K = map(int, input().split())

first = list(input().split())
second = list(input().split())

# DP inital table
table = [[0]*M for _ in range(N)]

max_num = 0

for i in range(N):
    for j in range(M):
        if first[i] == second[j]:
            # if first row or column (no previous number)
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                # add 1 to the previous max num in cost table
                table[i][j] = table[i-1][j-1] + 1
            
            # update max length
            if table[i][j] > max_num:
                max_num = table[i][j]

print(max_num)

