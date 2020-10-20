'''
bfs 문제이다. 
시작점과 원소인 인접리스트를 쌍으로 묶어 큐에 넣는다.
리스트를 순방하며 방문되지 않았을 경우, 다시 큐에 넣어준다.
visited는 방문 체크겸 동시에 거리 체크가 가능하다.
'''
from collections import deque, defaultdict
def solution(n, edge):
    answer = 0
    vertices = [[] for _ in range(n + 1)]
    #vertices = defaultdict(list)
    visited = [0] * (n + 1)
    for i in edge:
        vertices[i[0]].append(i[1])
        vertices[i[1]].append(i[0])

    q = deque()
    q.append((1, vertices[1])) # 시작점과 인접 리스트를 큐에 넣는다
    visited[1] = 1

    while(len(q) != 0):
        s, li = q.popleft()
        for e in li:
            if visited[e] == 0:
                q.append((e, vertices[e]))
                visited[e] = visited[s] + 1
    cnt = 0
    _max = max(visited)
    for v in visited:
        if v == _max:
            cnt += 1
    return cnt
