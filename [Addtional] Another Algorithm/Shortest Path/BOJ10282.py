'''
10282.해킹
Dijkstra 문제
'''
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(node):
    distances = [float('inf')] * (n + 1)
    distances[node] = 0
    queue = []
    heapq.heappush(queue, [node, 0])
    
    while queue:
        current_node, current_distance = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for adj, w in graph[current_node]:
            new_distance = current_distance + w
            
            if distances[adj] > new_distance:
                distances[adj] = new_distance
                heapq.heappush(queue, [adj, new_distance])
                
    return distances

t = int(input())
for _ in range(t):
    n, m, start = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        x, y, w = map(int, input().split())
        graph[y].append([x, w])
        
    distances = dijkstra(start)
    
    cnt = 0
    max_distance = 0
    for distance in distances:
        if distance != float('inf'):
            cnt += 1
            if distance > max_distance:
                max_distance = distance
                
    print(cnt, max_distance)
