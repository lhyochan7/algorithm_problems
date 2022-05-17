from itertools import combinations

def solution(orders, course):
    answer = []
    tmp_list = list()
    
    for order in orders:
        for l in range(2, len(order)+1):
            tmp_list.append(list(combinations(order, l)))
            print("order", order, "c", l)
            
    for tmp in tmp_list:
        print(tmp)
    
    
    return answer