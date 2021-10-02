'''
  [Insight]
  정수를 이어 붙여 가장 큰 수를 만들고자 했을 때,
  같은 수를 string으로 변환한 뒤 이어 붙여주고 정렬하면,
  원하는 방향으로 정렬이 가능하다.
'''

def solution(numbers):
    l = []
    for number in numbers:
        original = str(number)
        number = list(str(number))
        i = 0

        while len(number) <= 3:
            number.append(original[i])
            i = (i + 1) % len(original)

        number = int("".join(number))
        l.append([number, original])

    l = sorted(l, reverse=True)
    return str(int("".join([item[1] for item in l])))
