import sys

N = int(input())

graph = [[0] * cnt for cnt in range(1,N+1)]
cost_table = [[0] * N for _ in range(N)]

for i in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    graph[i] = input

for i, nodes in enumerate(graph):
    for j, _ in enumerate(nodes):
		# 가장 상위 숫자
        if i == 0:
            cost_table[i][j] = graph[i][j]            
        else:
            cost_table[i][j] = max(cost_table[i-1][j-1] + graph[i][j], cost_table[i-1][j] + graph[i][j])

answer = max(cost_table[N-1])

for cost in cost_table:
    print(cost)

print(answer)