def solution(jobs):
    answer = 0
    time = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1] # 처리시간을 미리 더해준다
                answer += time - jobs[i][0] # 기다리는 시간 + 처리 시간
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                time += 1

    return answer // length
