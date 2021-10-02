'''
봄 : 나무가 자신의 나이 만큼 양분을 먹고 나이가 증가. 여러개가 있다면, 나이가 어린 나무 부터 양분을 먹는다.
     양분이 부족하다면, 즉사
     
여름 : 봄에 죽은 나무가 양분으로 변한다. age//2

가을 : 나무 나이가 5n 이면 둘러싼 곳에 번식

겨울 : 양분 주입
'''

from sys import stdin
from collections import deque
input = stdin.readline

ans = 0
dx, dy = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)
N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
#tree = [[deque() for _ in range(N)] for _ in range(N)]
tree = [[ [] for _ in range(N)] for _ in range(N)]
nut = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
    ans += 1

'''
[Intution] 여름을 같이 구현함으로써, 죽은 나무 양부
'''
def spring_summer():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])): # 해당 땅에 나무가 있다면,
                if nut[i][j] >= tree[i][j][k]:
                    nut[i][j] -= tree[i][j][k] # 땅의 양분을 먹는다.
                    tree[i][j][k] += 1
                else:                          # 양분이 없다면 즉사 + 땅에 양분 공급
                    while k < len(tree[i][j]):
                        nut[i][j] += tree[i][j].pop()//2 # 오른쪽에서 제거
                        ans -= 1
                    break

def fall_winter():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])): # 해당 땅에 나무가 있다면,
                if tree[i][j][k] % 5 == 0:
                    for t in range(8):
                        nx, ny = i + dx[t], j + dy[t]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue
                        #tree[nx][ny].appendleft(1) # 나이가 어린 나무(1살)을 먼저 주입
                        tree[nx][ny].insert(0, 1)
                        ans += 1
            nut[i][j] += a[i][j]

def solve():
    for _ in range(K):
        spring_summer()
        fall_winter()
    print(ans)

solve()
