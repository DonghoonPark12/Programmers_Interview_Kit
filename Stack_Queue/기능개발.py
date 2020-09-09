def solution(progresses, speeds):
    answer = []
    present_progresses = []
    size = len(progresses)
    for i in range(size):
        present_progresses.append(progresses[i])

    while(1):
        tmp = 0
        pSize = len(present_progresses)
        if pSize == 0:
            break

        for i in range(pSize):
            present_progresses[i] += speeds[i]

        for i in range(pSize):
            if pSize == 0:
                break

            if present_progresses[0] >= 100:
                tmp += 1
                del present_progresses[0]
                del speeds[0]
            else:
                break

        if tmp != 0:
            answer.append(tmp)

    return answer
