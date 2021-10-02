# dist가 큰 친구 부터 차례로 위치 시킴. set 이용하여 모든 취약 지점이 수리 되었는지 확인
def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_list = [()]
    count = 0
    dist.sort(reverse = True) # 움직일 수 있는 거리가 큰 친구 순서대로
  
    # 고칠 수 있는 것들 리스트 작성
    for can_move in dist:
        repairs = [] # 친구 별 고칠 수 있는 취약점들 저장
        count += 1
      
        # 수리 가능한 지점 찾기
        for i, wp in enumerate(weak):
            start = wp # 각 위크 포인트 부터 시작
            ends = weak[i:] + [n + w for w in weak[:i]] # 시작점 기준 끝 포인트 값 저장
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))
          
        # 수리 가능한 경우 탐색
        cand = set()
        for r in repairs: # 새 친구의 수리 가능 지점
            for x in repair_list: # 기준 수리 가능 지점
                new = r | set(x)
                if len(new) == W: # 모두 수리 가능한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        repair_list = cand
      
    return -1
