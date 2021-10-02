'''

'''
from sys import stdin

n, k = map(int, stdin.readline().split())
graph = [[0] * 401 for _ in range(401)]

while(k):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1-1][v2-1] = 1
    k -= 1

for i in range(n):
    for j in range(n):
        if graph[j][i] != 1:
            continue
        for k in range(n):
            graph[j][k] |= graph[j][i] & graph[i][k]

s = int(stdin.readline())
while(s):
    v1, v2 = map(int, stdin.readline().split())
    if graph[v1-1][v2-1]:
        print(-1)
    elif graph[v2-1][v1-1]:
        print(1)
    else:
        print(0)

    s -= 1
