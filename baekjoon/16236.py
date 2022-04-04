if __name__ == "__main__":
    
    n = int(input())

    graph = [[] for _ in range(n)]

    for i in range(n):
        tmp = map(int, input().split())
        graph[i].extend(tmp)

    print(graph)
