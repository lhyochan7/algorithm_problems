num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def solution(s):
    answer = 0
    
    for i, (k,v) in enumerate(num.items()):
        
        s = s.replace(k, str(v))
    
    
    answer = int(s)
    
    return answer