'''
최소 비용으로 모든 정점을 연결하는 최소 스패닝(MST) 트리 문제이다.
'''
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # Cost 기준 정렬
    mst = set([costs[0][0]]) # Set
    while len(mst) != n:
        for i, cost in enumerate(costs):
            # 사이클을 형성하는 경우 패스
            if (cost[0] in mst) and (cost[1] in mst):
                continue
            if (cost[0] in mst) or (cost[1] in mst):
                mst.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer

#---------------------------------------------------------------------------------------------------------------------------#
# My comment. Ignore it!
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 만약, C++ 이라면 (정점, 정점, 가중치)를 담는 새로운 struct를 만들어서 정렬해야 할 듯.
    mst = set([costs[0][0]]) # Set STL 사용. #인접 리스트나, 인접 행렬의 경우 정렬이 힘들다. 
    while len(mst) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in mst) and (cost[1] in mst):
                continue
            if (cost[0] in mst) or (cost[1] in mst):
                mst.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer
