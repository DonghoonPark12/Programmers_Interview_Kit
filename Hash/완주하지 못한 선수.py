def solution(participant, completion):
    answer = ''
    c_dict = {}
    for i in participant:
        if i in c_dict:
            c_dict[i] += 1
        else:
            c_dict[i] = 1
            
    for i in completion:
        if i in c_dict:
            c_dict[i] -= 1
    
    for key, val in c_dict.items():
        if(val == 1):
            answer = key
    return answer
