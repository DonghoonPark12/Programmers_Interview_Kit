'''
Stack을 이용한 풀이.
Stack top보다 큰수를 만다면, k가 소진되기 전까지 값을 뺀다.
'''
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
        
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer
