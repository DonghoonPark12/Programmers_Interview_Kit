'''
최소 비용으로 모든 정점을 연결하는 최소 스패닝(MST) 트리 문제이다.
'''
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # Cost 기준
    mst = set([costs[0][0]]) # Set
    while len(mst) != n:
        for i, cost in enumerate(costs):
            # 이미 두 간선이 집합에 있는 경우 패스
            if (cost[0] in mst) and (cost[1] in mst):
                continue
            if (cost[0] in mst) or (cost[1] in mst):
                mst.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer
