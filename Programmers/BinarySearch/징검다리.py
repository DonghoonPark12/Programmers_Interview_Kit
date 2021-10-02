'''
제거한 갯수(cnt)를 기준으로
n보다 작거나 같으면 left = mid + 1
n보다 크면 right = mid - 1
'''
def solution(distance, rocks, n):
    ans = 0
    rocks.sort()
    
    left = 1
    right = distance
    
    while(left <= right):
        cnt = 0
        prev = 0
        mid = (left + right) // 2
        
        for i in range(len(rocks)):
            if(rocks[i] - prev < mid):
                cnt += 1
            else:
                prev = rocks[i]
                
        if (distance - prev) < mid : 
            cnt += 1
            
        if cnt <= n:
            if mid > ans:
                ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
