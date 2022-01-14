def solution(number, k):
    answer = list()
    
    for num in number:
        #print(answer)
        # Stack이 비워있을때
        if len(answer) == 0:
            answer.append(num)
            continue
        
        # Stack이 비어있지 않을 때 그리고 k 남은 숫자가 있을떄
        if k > 0:
            # Stack 마지막과 들어올 숫자를 비교하여
            # 보다 작은 숫자가 있으면 제거 후 삽입
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        
        answer.append(num)
    
    # k > 0 이상이면 스택에서 k개 삭제 후 join해서 결과 값 반환 예시) 999, 3 => 9
    if k > 0:
        answer = answer[:-k]
    else:
        answer
    
    answer = "".join(answer)
    
    return answer