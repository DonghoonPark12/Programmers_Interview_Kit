'''
h-index는 n회 이상 인용된 논문이 n개 이상일 때, 이 둘을 동시 만족하는 n의 최대 값으로 한다.

힌트: h-index는 항상 논문 갯수보다 작거나 같다.

방법: 리스트의 가장 작은 값이 리스트의 길이보다 더 큰 경우 멈춘다.
'''

def solution(citations):
    answer = 0
    h_index = len(citations)
    citations = sorted(citations,reverse = True)
    print(citations)
    while(len(citations) != 0 ):
        if(h_index <= citations[-1]):
            answer = h_index
            break
        else:
            citations.pop()
            h_index = len(citations)
    return answer




'''
[사견]
h지수가 양적인 기여도 중요시 여기는 지표인 듯하다.
첫 논문이 10000번 인용되어도 h지수는 1이라서, 일부 학자들에겐 억울할 수도 있겠다.
'''
