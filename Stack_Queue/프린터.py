from collections import deque
from queue import PriorityQueue

def solution(priorities, location):
    answer = 0
    de = deque([])
    pq = PriorityQueue()
    pSize = len(priorities)
    for i in range(pSize):
        if i == location:
            de.append([priorities[i], 1])
        else:
            de.append([priorities[i], 0])
        pq.put(-priorities[i]) # 최대 힙을 만들려면 -1을 곱해줘야 하는 불편함... 'import heapq'도 마찬가지

    cnt = 0
    tmp = []
    while(de):
        if(de[0][0] < -pq.queue[0]): # 원해 원소를 보기 위해서 -를 곱해줘야하는 불편함...
            tmp = de[0]
            de.append(tmp)
            de.popleft()
        else:
            cnt += 1
            if(de[0][1] == 1):
                answer = cnt
                break
            de.popleft()
            pq.get()


    return answer
