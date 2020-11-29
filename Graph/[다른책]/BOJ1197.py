'''
최소 스패닝 트리 문제
'''
from sys import stdin

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, stdin.readline().split())
patent = [0] * (v + 1)
# 간선의 비용을 담는 변수
graph = []
result = 0

for i in range(1, v + 1):
    patent[i] = i # 초기에 노드의 부모는 자기 자신

for _ in range(e):
    a, b, cost = map(int, stdin.readline().split())
    graph.append((cost, a, b))

graph.sort()  # 비용이 적게 나가는 것부터 연결하기 위함

for g in graph:
    cost, a, b = g
    if find_parent(patent, a) != find_parent(patent, b): 
        union_parent(patent, a, b)
        result += cost
print(result)
