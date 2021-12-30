import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) > 1:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            t = x + y*2
            heapq.heappush(scoville, t)
            answer += 1
        else:
            return -1
    
    return answer