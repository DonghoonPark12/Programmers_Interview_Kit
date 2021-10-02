from sys import stdin

N, M = map(int, stdin.readline().split())

parent = {}
rank = {}
#mst = []

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(n, m):
    total = 0
    _max = -1
    # graph = []
    # Graph 초기화 ------------------------------------------------ #
    for i in range(1, n+1):
        make_set(i)

    # while(m):
    #     a, b, w = map(int, stdin.readline().split())
    #     graph.append([w, a, b])
    #     m -= 1
    # graph.sort()

    graph = [ tuple(map(int, stdin.readline().split())) for _ in range(m) ]
    graph.sort(key=lambda t: t[2])
    # ------------------------------------------------------------ #


    for g in graph:
        w, a, b= g
        if find(a) != find(b):
            union(a, b)
            #mst.append(g)
            total += w
            _max = max(_max, w)
    return total - _max #[TODO] N - 2가 어떻게 종료 조건이 될 수 있는지??

print(kruskal(N, M))
