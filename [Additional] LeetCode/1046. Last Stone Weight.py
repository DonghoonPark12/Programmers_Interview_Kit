import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            heapq.heappush(heap, -1 * stones[i])
            
        while(len(heap) >1):
            a = -1 * heapq.heappop(heap)
            b = -1 * heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -1 * (a - b) )
            else:
                continue
                
        if len(heap) == 0:
            return 0
        else:
            return -1 * heap[0]
            
