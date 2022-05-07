M, N, K = map(int, input().split())

first = list(map(str, input().split()))
second = list(map(str, input().split()))

first = ''.join(first)
second = ''.join(second)

if first in second:
    print('secret')
else:
    print('normal')