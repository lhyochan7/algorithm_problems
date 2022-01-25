# 재귀로 풀시 시간초과
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return (fib(n - 1) + fib(n - 2)) % 1234567


def solution(n):
    
    Table = [0 for c in range(n+1)]
    Table[1] = 1
    
    for i in range(2, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1234567

    return Table[i]