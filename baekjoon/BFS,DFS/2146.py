from collections import deque

if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n)]

    for i in range(n):
        temp = input().split()
        graph[i].extend(temp)

    print(graph)

'''
    for x in range(n):
        for y in range(n):
            if 
'''