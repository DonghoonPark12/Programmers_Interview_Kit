from sys import stdin
import copy

N = int(stdin.readline())

adj_list = [ [] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)
queue = []
result = []

for n in range(1, N + 1): #n은 과목 번호
    l = list(map(int, stdin.readline().split()))
    time[n] = l[0]
    for _in in l[1:]:
        if _in == -1: break
        adj_list[_in].append(n)
        indegree[n] += 1

def topologicalSort():
    queue = [v for v in range(1, N + 1) if indegree[v] == 0]
    result = copy.deepcopy(time)

    while queue:
         cur = queue.pop(0)

         for adj in adj_list[cur]:
             result[adj] = max(result[adj], result[cur] + time[adj])
             indegree[adj] -= 1
             if indegree[adj] == 0:
                 queue.append(adj)

    for i in range(1, N + 1):
        print(result[i])
topologicalSort()
