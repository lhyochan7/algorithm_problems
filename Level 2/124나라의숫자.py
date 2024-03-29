# 124 나라의 숫자
def solution(n):
    answer = ''
    
    #우선 n이 3의 배수가 아니라면 3진법을 구하는 것과 동일하게 3으로 나눈 나머지를 저장하고, n을 3으로 나눈 몫으로 저장한다.
    #n이 3의 배수라면 무조건 4를 추가하고, n을 3으로 나눈 몫에서 1을 뺀 값을 저장한다.
    while n:
        # 3의 배수가 아닐떄
        if n % 3:
            answer += str(n % 3)
            n //= 3
        # 3의 배수
        else:
            answer += "4"
            n = n//3 - 1
    
    #역순으로 반환
    return answer[::-1]