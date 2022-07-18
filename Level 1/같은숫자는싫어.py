def solution(arr):
    
    answer = []
    
    for idx, value in enumerate(arr):
        if idx == 0:
            answer.append(value)
        else:
            if answer[-1] != value:
                answer.append(value)
                
    return answer