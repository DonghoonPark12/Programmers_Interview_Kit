def solution(n, lost, reserve):
    answer = 0
    count =0
    lostman=list(set(lost)-set(reserve))
    rentman=list(set(reserve)-set(lost))

    for element in lostman:
        if element-1 in rentman:
            count += 1
            rentman.remove(element-1)
        elif element+1 in rentman:
            count +=1
            rentman.remove(element+1)

    answer = n-(len(lostman)-count)    
    return answer
