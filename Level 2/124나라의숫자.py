def solution(n):
    answer = ''
    
    dict124 = {1:1, 2:2, 3:4, 4:11, 5:12, 6:14, 7:21, 8:22, 9:24, 10:41}
    
    n = str(n)
    temp = list()
    
    for num in n:
        temp.append(dict124[int(num)])
    
    answer = "".join(map(str,temp))
    
    return answer