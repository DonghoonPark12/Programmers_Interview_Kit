def solution(scoville, K):
    answer = 0
    heap = []
    heapq.heapify(heap)
    # or
    #for i in scoville:
    #    heapq.heappush(heap, i)
    while(heap[0] < K):
        if len(heap) ==1 :
            return -1
        a = heap[0]
        heapq.heappop(heap)
        b = heap[0]
        heapq.heappop(heap)
        heapq.heappush(heap, a + b*2)
        answer+=1
    return answer
