'''
집합(set)을 value로 가지는 딕셔너리를 만들면 편하다.
e.g. 5번이 2번에게 패해하였다면, 1, 3, 4에게도 패배한 것.
승패 관계를 확실하게 해주는 부분이 Line 17 ~ 22
'''
from collections import defaultdict
def solution(n, results):
    answer = 0
    # wins = [[] for _ in range(n + 1)]
    # loses = [[] for _ in range(n + 1)]
    wins = defaultdict(set)
    loses = defaultdict(set)
    for l, r in results:
        wins[l].add(r)
        loses[r].add(l)

    for i in range(1, n + 1):
        for l in wins[i]:
            loses[l].update(loses[i]) # loses[5] 에 다가 loses[2]를 update 해준다.

        for w in loses[i]:
            wins[w].update(wins[i])

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    return answer
