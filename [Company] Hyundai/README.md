# [HMG softeer.ai](https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=389) 문제 풀이

## [로봇이 지나간 경로(1회 -기출 2번)](https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=577&sw_prbl_sbms_sn=27423)
### 고찰
- 미로 찾기 등등 BFS, DFS 문제로 착각할 수 있는데 그렇지 않다 
- 문제 속에 답이 있다
### 풀이
- (★) 로봇의 시작점을 찾는 것이 핵심 --> '좌,우,상,하' 로 검색하여 '#'가 한번만 나오는 지점을 찾는다.
- (문제 상에 로봇은 '두칸 전진한다' 에서 힌트를 얻을 수 있다. 두 칸 전진하는 것이 아니면 로봇의 시작점을 찾는 조건문이 길어질 수 있다)
- 이웃에 '#'이 있다면 이동한다. 방향이 다르다면, '방향'을 먼저 저장한다.
- (★) 방향이 다른 지점으로 이돌 할 때, 뒤로 가는 경우는 없기 때문에, '좌, 우'만 살피면 된다.
- visited 배열을 두어 방문 체크를 하고, '좌,우,상,하' 검색하여 이동할 공간 없다면, 종료한다.