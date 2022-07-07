from collections import deque

def solution(numbers, target):
    answer = 0
    
    n = len(numbers)
    queue = deque()
    
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    
    while queue:
        print(queue)
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    
    return answer

'''

def solution(numbers, target):
    answer = 0
    
    table = [[] for _ in range(len(numbers))]

    # 첫 숫자의 + - 추가
    table[0].append(-numbers[0])
    table[0].append(+numbers[0])
    for idx, num in enumerate(numbers):
        # 전 숫자의 + - 의 숫자들을 다음 숫자의 + - 구하기
        for tot in table[idx-1]:
            table[idx].append(tot-num)
            table[idx].append(tot+num)

    #print(table)
    # 마지막 결과에서 target 숫자와 일치하는 개수 구하기
    for i in table[-1]:
        if i == target:
            answer += 1
    
    return answer 
'''