import collections

def solution(N, stages):
    answer = []
    
    remaining = len(stages)
    temp = dict()
    
    for idx in range(1, N+1):
        if remaining == 0:
            temp[idx] = 0
        else:
            failRate = stages.count(idx) / remaining 
            remaining -= stages.count(idx)
            temp[idx] = failRate
            
    temp = sorted(temp.items(), reverse=True, key=lambda x : x[1])
    
    print(temp) 
    for i in temp:
        answer.append(i[0])
    
    return answer