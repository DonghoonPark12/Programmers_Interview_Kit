'''
이분 탐색 문제
while(left <= right):
(...)
left = mid + 1
right = mid - 1
'''
from sys import stdin

N = int(stdin.readline())
req = list(map(int, stdin.readline().split()))
budget = int(stdin.readline())

def binarySearch():
    left = 0
    right = max(req)

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for r in req:
            if r < mid: # 요청이 배정 값 보다 작거나 같으면
                total += r # 요청을 받아 들인다
            else:            # 요청이 배정 값 보다 크면
                total += mid # 상한액 제공

        if total <= budget: # 배정된 예산 총 합이 전체 예산 보다 못 미치면(여유가 있으면)
            left = mid + 1
        else:
            right = mid - 1

    return right

print(binarySearch())
