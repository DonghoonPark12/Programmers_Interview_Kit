from sys import stdin

n, m = map(int, stdin.readline().split())
arrN = [int(e) for e in stdin.readline().split()]
cnt = 0

left, right = 0, 0
sum = 0

while (1):
    if sum < m:
        if right == n: # right 포인터가 범위를 넘어가면 종료
            break
        sum += arrN[right]
        right += 1
    else:
        sum -= arrN[left]
        left += 1
    if sum == m:       # 포인터 이동과 동시에 값을 확인한다.
        cnt += 1
print(cnt)
