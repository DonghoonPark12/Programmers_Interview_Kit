'''
공유기 사이 거리가 mid 이상 일때,
c이상 설치할 수 있다면 간격을 늘려주고,
없다면 간격을 좁혀준다.
'''
from sys import stdin
n, c = map(int, stdin.readline().split())
arrN = [int(stdin.readline()) for _ in range(n)]
arrN.sort()
start, end = 1, arrN[n-1] - arrN[0]# 최소 거리는 1, 최대 거리는 처음 집과 마지막 사이 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prev = arrN[0]
    for i in arrN:
        if i - prev >= mid:
            prev = i
            cnt += 1
    if cnt < c:
        end = mid - 1
    else:
        start = mid + 1
        result = max(result, mid)
print(result)
