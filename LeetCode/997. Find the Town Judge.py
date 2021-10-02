class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ans = -1
        arr = [ [0] * (N + 1)  for _ in range(N+1) ] # 한칸 더 크게 만들어야 index 참고 가능
        
        for t in trust:
            arr[t[0]][t[1]] = 1 # 인접 행렬
        
        #print(arr)
        
        for i in range(1, N+1):
            cnt = 0
            for j in range(1, N+1):
                if i != j: # town judge는 믿음을 당하면서(cnt로 체크), 믿지는 않아야 한다
                    if arr[j][i] == 1 and arr[i][j] != 1:
                        cnt += 1
                    else: # 만약에 한명의 믿음도 받지 않으면 바로 break
                        break
                    
            if cnt == N - 1:
                ans = i
                return ans
            
        return ans
