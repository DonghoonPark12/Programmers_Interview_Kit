'''
PyPy3으로 선택해야 통과된다.
'''
from sys import stdin
from collections import deque

n, l = map(int, stdin.readline().split())
arrN = [int(e) for e in stdin.readline().split()]
de = deque([])       # 덱에는 배열 인덱스를 넣어준다
for i in range(n):
    while (len(de) != 0) and (de[0] <= i - l):
        de.popleft() # 윈도우 범위를 벗어나는 인덱스는 덱에서 제거해 준다.
    while (len(de) != 0) and (arrN[de[len(de) - 1]] >= arrN[i]):
        de.pop()     # 새로 들어 오는 값이, 덱에 있는 원소들 보다 작다면 덱 원소들을 빼준다
    de.append(i)
    print(arrN[de[0]], end=' ')