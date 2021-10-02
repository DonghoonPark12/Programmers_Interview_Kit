'''
  s가 1000 이하므로, 문자열을 자르는 단위를 바꿔 가면서 압축 최소화 여부를 점검한다.
'''
def solution(s):
    LENGTH = len(s)
    cand = [LENGTH]  # 1 ~ len까지 압출했을 때 길이 값

    for size in range(1, int(LENGTH/2) + 1): # 문자열 절반 길이 이상이 반복 될 수 없으므로 수행을 줄일 수 있다.
        compressed = ""
        splited = [s[i:i + size] for i in range(0, LENGTH, size)]
        cnt = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                cnt += 1
            else:
                compressed += (str(cnt) + prev) if cnt > 1 else prev #길이가 1이면 '1'생략
                cnt = 1  # 초기화
        
        # LENGTH 길이로 잘리지 않는 마지막 문자열 경우 
        # e.g.'ded', 'e'
        if cnt > 1: compressed += (str(cnt)) + splited[-1]
        else: compressed += splited[-1]
          
        cand.append(len(compressed))

    return min(cand)
