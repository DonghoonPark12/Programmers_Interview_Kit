'''
최대 2명 밖에 타지 못한다는 조건이 있다.
몸무게로 정렬하여, 가장 무거운 사람이 가장 가벼운 사람과 같이 탈 수 있는지 조사한다.
같이 탈 수 있다면 : st++, end--
같이 탈 수 없다면 : end--
'''
def solution(people, limit) :
    people.sort()
    cnt = 0
    st = 0
    end = len(people)-1
    while st <= end:
        cnt += 1
        if people[end] + people[st] <= limit :
            st+=1
        end -= 1
    return cnt
