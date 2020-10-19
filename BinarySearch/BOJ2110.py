import sys
input=sys.stdin.readline
n, c = map(int, input().split())
a=[]
for _ in range(n):
  a.append(int(input()))
a.sort()
start, end = 0, a[-1]
result = 0
while start <= end:
    mid = (start+end+1)//2
    cnt = 1
    temp = a[0]
    for i in a:
        if i - temp>=mid:
            temp = i
            cnt+=1
    if cnt<c:
        end = mid-1
    else:
        start=mid+1
        if mid>result:
            result=mid
    
print(result)
