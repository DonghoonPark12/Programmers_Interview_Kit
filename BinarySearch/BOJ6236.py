from sys import stdin

N, M = map(int, stdin.readline().split())
arrN = [int(stdin.readline()) for _ in range(N)]

def binarySearch():
    moneySum = sum(arrN)
    left = max(arrN) #최소는 max(arrN) 항상 M은 N이 된다.
    right = moneySum #최대는 돈의 총합. 항상 M은 0이 된다.
    while(left <= right):
        mid = (left + right) // 2 # 인출할 돈 (가정)
        cnt = 1                   # 최초 한번 출금
        le = mid                  # 남은 돈
        for ele in arrN:
            if le < ele:          # 만약 남은 돈이 모자라다면
                le = mid          # 남은 돈 갱신
                cnt += 1          # 출금 카운트 갱신
            le -= ele

        if (M >= cnt):
            right = mid - 1
        else:
            left = mid + 1
    return left

print(binarySearch())
