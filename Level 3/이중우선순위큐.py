import heapq

def solution(operations):
    answer = []
    heap = []
    
    for o in operations:
        heapq.heapify(heap)
        
        if o[0] == 'I':
            num = o[2:]
            heapq.heappush(heap, int(num))
            
        elif o[0] == 'D':
            if len(heap) == 0:
                continue
                
            # Min heap
            if o[2] == '-':
                x = heapq.heappop(heap)
                print('min', x)
            # Max heap
            else:
                reverse_heap = [-val for val in heap]
                heapq.heapify(reverse_heap)
                heapq.heappop(reverse_heap)
                heap = [-val for val in reverse_heap]
                heapq.heapify(heap)

    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), min(heap)]

    return answer