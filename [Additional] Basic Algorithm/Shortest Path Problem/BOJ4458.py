'''
Dijkstra 문제
- Single Source Shortest Path Problem
'''
import heapq
from sys import stdin, maxsize
INF = maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dij(cnt):
    d, qu = [[INF] * n for _ in range(n)], []
    heapq.heappush(qu, [arr[0][0], 0, 0]) # 현재 위치 가중치, (초기 위치)를 큐에 저장
    d[0][0] = 0
    while qu:
        w, x, y = heapq.heappop(qu) # 현재 위치 weight
        if x == n-1 and y == n-1:
            print("Problem {}: {}".format(cnt, w))
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 경계 조건
                nw = w + arr[nx][ny] # 현재 가중치 + 다음 가중치를 더했을 때
                if nw < d[nx][ny] : #기존 가중치에 비해 더 작아진다면
                    d[nx][ny] = nw
                    heapq.heappush(qu, [nw, nx, ny])
                

cnt = 1
while 1:
    n = int(stdin.readline())
    if n == 0:
        break
    else:
        arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
        dij(cnt)
        cnt += 1


