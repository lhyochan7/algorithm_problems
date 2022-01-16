from itertools import combinations

def solution(people, limit):
    answer = 0
    
    # 무거운 순으로 정렬
    people = sorted(people, reverse=True)

    # 앞과 뒤 사람 위치 (앞 = 무거운, 뒤 = 가벼운)
    f = 0
    b = len(people)-1
    
    # 두 사람이 같은 사람이 되지 않을 때 까지
    while b >= f:
        # 두 사람의 몸무게가 limit 아래 있을시 둘다 탑승, f 한칸 움직이고 b 땡긴다
        if people[f] + people[b] <= limit:
            answer += 1
            f += 1
            b -= 1
        # 몸무게가 초과되면 무거운 사람만 탑승
        else:
            answer += 1
            f += 1
    
    return answer