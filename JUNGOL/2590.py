# 색종이
import sys

paper = [0]
cnt = 0
for _ in range(6):
    a = int(sys.stdin.readline())
    paper.append(a)

# 6*6은 판 1개 소모
cnt += paper[6]

# 5*5는 판 1개에 부착하고 1*1을 최대한 많이 부착
while paper[5] > 0:
    paper[5] -= 1
    paper[1] -= 11
    if paper[1] < 0:
        paper[1] = 0 
    cnt += 1

# 4*4는 판에 부착하고 2*2를 최대한 많이 부착하는게 최선
while paper[4] > 0:   
    paper[4] -= 1

    if paper[2] >= 5:
        # 5개보다 많이 있다면 붙인다
        paper[2] -= 5
    else:
        # 5개보다 적다면

        # 5개 2*2가 붙을수 있는 공간을 제외한 1*1 공간에
        # 1*1 붙여준다. 즉,(5 - paper[2]) * 4
        paper[1] -= ((5 - paper[2]) * 4)
        # 위에서 (5*5) 다썼던 말든, 음수라면 0으로 해준다
        if paper[1] < 0: paper[1] = 0  

        paper[2] = 0 # 2*2는 일단 다 소진한 것
    cnt += 1       

# 여기까지 4*4를 다 소진

while paper[3] > 0:
    if paper[3] >= 4:
        paper[3] -= 4

    elif paper[3] == 3:
        paper[3] = 0  # 3*3 다쓰고
        
        if paper[2] >= 1:
            paper[2] -= 1 # 2*2 한개 밖에 안써진다
            paper[1] -= 5
        else:
            paper[1] -= 9

        # 어김 없이 등장하는 1*1 종이 처리
        if paper[1] < 0: paper[1] = 0 

    elif paper[3] == 2:
        paper[3] = 0  # 3*3 다쓰고

        if paper[2] >= 3:
            paper[2] -= 3
            paper[1] -= 6

        elif paper[2] == 2:
            paper[2] = 0
            paper[1] -= 10
        
        elif paper[2] == 1:
            paper[2] = 0
            paper[1] -= 14
        
        else: # paper[2] == 0
            paper[1] -= 18
        
        # 어김 없이 등장하는 1*1 종이 처리
        if paper[1] < 0: paper[1] = 0         

    else: # paper[3] == 1:
        paper[3] = 0  # 3*3 다쓰고

        if paper[2] >= 5:
            paper[2] -= 5
            paper[1] -= 7
        else:
            paper[1] -= ((5 - paper[2]) * 4 + 7)
            paper[2] = 0

        if paper[1] < 0: paper[1] = 0   
    cnt += 1

# 여기까지 3*3를 다 소진

while paper[2] > 0:
    if paper[2] >= 9:
        paper[2] -= 9
    else:
        paper[1] -= (9 - paper[2]) * 4
        paper[2] = 0

    if paper[1] < 0: paper[1] = 0 
    cnt += 1

while paper[1] >0:
    paper[1] -= 36
    cnt += 1

# temp = paper[2] * 4 + paper[1]
# if (temp % 36 == 0):
#     cnt += temp // 36
# else:
#     cnt += temp // 36 + 1

print(cnt)
