from collections import deque

if __name__ == '__main__':
    n = int(input())

    results = list()
    q = deque()

    for i in range(n):
        cmd = input().split()
        #print(cmd)

        if cmd[0] == 'push':
            q.append(cmd[1])
        elif cmd[0] == 'front':
            results.append(q[0])
        elif cmd[0] == 'back':
            results.append(q[-1])
        elif cmd[0] == 'size':
            results.append(len(q))
        elif cmd[0] == 'pop':
            if len(q) != 0:
                results.append(q.popleft())
            else:
                results.append(-1)
        elif cmd[0] == 'empty':
            if len(q) == 0:
                results.append(1)
            else:
                results.append(0)

        #print(q)

    for cmd in results:
        print(cmd)