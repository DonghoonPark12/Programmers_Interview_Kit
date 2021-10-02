def solution(skill, skill_trees):
    answer = 0
    #skill_list = [ skill[i] for i in range(len(skill))]

    for ski in skill_trees:  #"BACDE"
        tmp = []
        for i in range(len(ski)): # 5
            if(ski[i] in skill): #B
                tmp.append(ski[i])

        Flag = True
        for j in range(len(tmp)):
            if tmp[j] != skill[j]:
                Flag = False
                break
        if(Flag):
            answer += 1
    return answer
