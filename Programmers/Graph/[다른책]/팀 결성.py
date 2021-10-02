from sys import stdin
n, m = map(int, stdin.readline().split())

parent = {}
rank = {}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

for i in range(n + 1):
    make_set(i)

while(m):
    o, a, b = map(int, stdin.readline().split())
    if(o == 0):
        if(a != b):
            union(a, b)
    else:
        if(find(a) != find(b)):
            print('NO')
        else:
            print('YES')

    m -= 1

