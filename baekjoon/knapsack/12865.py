if __name__ == "__main__":

    N, K = map(int, input().split())

    items = [[0,0] for _ in range(N+1)]
    knapsack = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        w, v = map(int, input().split())
        items[i][0] = w
        items[i][1] = v

    for i in range(1, N+1):
        for j in range(1, K+1):
            w = items[i][0]
            v = items[i][1]

            if j < w:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
            
    #print(knapsack)

    print(knapsack[N][K])