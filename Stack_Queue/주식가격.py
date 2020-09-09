def solution(prices):
    size = len(prices)
    answer = [0]*size
    for i in range(0, size):
        for j in range(i, size-1):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                break
    return answer
