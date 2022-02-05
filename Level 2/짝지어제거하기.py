# Method using stack

def solution(s):
    answer = -1
    
    stck = []

    for i in s:
        # if stack is empty
        if len(stck) == 0:
            stck.append(i)
            continue

        b = stck[-1]
        
        # remove from stack if pair
        if i == b:
            stck.pop()
        # add onto stack if not pair
        else:
            stck.append(i)
            
    if len(stck) == 0:
        answer = 1
    else:
        answer = 0
    
    return answer