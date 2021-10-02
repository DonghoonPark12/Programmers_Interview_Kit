'''
리스트를 value로 둔다.
'알파벳 순서가 앞서는 경로를 return' 이라는 조건으로 인하여, value를 역순으로 정렬한다.
스택 top을 기준으로 value가 있을 경우 push 한다. 
'''
from collections import defaultdict
def solution(tickets):
    t = defaultdict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])  # 시작점 : [도착점] 쌍을 만든다.
        else:
            t[ticket[0]] = [ticket[1]]
    for k in t.keys():
        t[k].sort(reverse=True)  # 도착점 리스트를 역순으로 정렬

    st = ['ICN']  # 스택에 'ICN' 먼저 넣는다
    answer = []
    while st:
        top = st[-1]
        # top 이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우, 스택에서 꺼내와 path에 저장한다.
        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(t[top][-1])
            t[top].pop()
    answer.reverse()
    return answer
