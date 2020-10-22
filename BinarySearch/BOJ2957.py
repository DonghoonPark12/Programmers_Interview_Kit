from bisect import bisect_left, bisect_right

tree = [0, 300001]
depth = [-1, -1] # 각 위치별 깊이도 리스트로 저장
answer = 0
for _ in range(int(stdin.readline())):
    val = int(stdin.readline())
    idx = bisect_left(tree, val)
    depth_idx = max(depth[idx-1], depth[idx]) + 1

    tree.insert(idx, val)
    depth.insert(idx, depth_idx)
    answer += depth_idx
    print(answer)
    
'''
bisect_left(a, x) : a에 x를 삽입할 위치를 찾는다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞.
bisect_right(a, x) : a에 있는 x의 기존 항목 뒤(오른쪽)에 오는 삽입 위치를 반환.
'''
