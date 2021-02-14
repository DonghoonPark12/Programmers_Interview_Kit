'''
[풀이]
- N은 최대 2000이므로 2중 for문을 돌려도 된다.
- Pivot을 기준으로 시간차를 구해서 1s 이내로 처리될 수 있는 것이 몇개인지 파악한다
- 리스트에 1개만 담겨 있다면, (완료 여부 관계 없으니) 1s에 1개가 처리가 무조건 가능하므로 최소 갯수는 1이다.
- (주의) 2s, 2.0s 등 문자열 파싱할 때 디테일한 처리가 일부 필요
- (주의) 시간이 60을 넘어가게 되면 반대로 빼줘야 하는 부분 처리가 필요하다.
- s 단위의 경우 처리시간(T)를 고려하여 ms 단위로 계산하였다.

https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
'''
def Time_Interval(t1, t2, t2T):
    '''
        t1 - (t2 - t2T + 0.001) 이 1s 미만인지 파악
        음수일 수도 있다.
    '''
    pt2T = int(t2T[0]) * 1000
    if t2T[1] != 's':
        res = 3 - len(t2T[2:-1])
        tmp = int(t2T[2:-1])
        if res:
            tmp *= pow(10, res)
        pt2T += tmp
    
    t1h = int(t1[:2])
    t1m = int(t1[3:5])
    t1s = int(t1[6:8] + t1[9:])
    t2h = int(t2[:2])
    t2m = int(t2[3:5])
    t2s = int(t2[6:8] + t2[9:])
    if (t2h - t1h) == 1:
        if(t2m + 60 - t1m > 1):
            return False
        else:
            #t2 - t1을 해야 한다.
            if(t2s + 60000 - pt2T + 1 - t1s < 1000):
                return True
            else:
                return False
    elif (t2h - t1h) == 0:
        #t2 - t1를 해야 한다.
        if(t2m - t1m > 1):
            return False
        elif (t2m - t1m == 1):
            # t1s - t2s 해야 한다
            if(t2s + 60000 - pt2T + 1 - t1s < 1000):
                return True
            else:
                return False            
        else:
            if(t2s - pt2T + 1 - t1s < 1000):
                return True
            else:
                return False 
    else:
        return False
    
    
def solution(lines):
    mpps = 1 
    if(len(lines) == 1):
        return mpps
    
    for i in range(len(lines)):
        S = lines[i].split(' ')[1]
        cnt = 1
        for j in range(i+1, len(lines)):
            Sn = lines[j].split(' ')[1]
            Sn_T = lines[j].split(' ')[2]
            if Time_Interval(S, Sn, Sn_T):
               cnt += 1 

            mpps = max(cnt, mpps)            
    return mpps
