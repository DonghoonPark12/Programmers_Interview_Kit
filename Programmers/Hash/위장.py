def solution(clothes):
    answer = 1
    dic = {}
    num = []
    for name, cate in clothes:
        if cate in dic:
            dic[cate].append(name)
        else:
            dic[cate] = [name] #dictionary 원소를 리스트로 만든다.
    
    for key in dic.keys():
        num.append(len(dic[key])) #각 values 값을 리스트로
    cnt = 0
    for i in dic.values():
        answer *= len(i) # 2 * 1 = 2
        cnt += len(i)
    answer += cnt
    
    return answer
