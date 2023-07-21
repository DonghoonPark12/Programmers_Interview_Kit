
[톱니바퀴 : BOJ 14891](https://www.acmicpc.net/problem/14891)
```
- 문제를 분리한다. (시계 회전, 반 시계 회전, 값 연산 부분을 따로 만든다)
- 톱니를 회전하면서 체크하면 '회전된 톱니의' 옆 톱니는 회전 되지 않은 상태에서 
  '회전된 톱니와' 비교하게 된다. 따라서, '회전 될지 여부를 판단하는 배열'을 따로
  만들어서 추후에 회전시켜 준다.
```

[감시 : BOJ 15683](https://www.acmicpc.net/problem/15683)
```
본인의 경우 CCTV 가 방향별로 시야를 보고, 큐에 담으려고 하였으나 담는 방법이 떠오르지 않았다.  
하지만, 본 문제는 2차원 배열 상태를 각각의 경우의 수로 가지므로 메모리 효율을 위해 DFS를 사용하는 것이 낫다
dfs, 2차원 배열 백업함수, 그려주는 함수 로 구분해야 함을 알 수 있다.
각각 회전이 가능한 경우는 rot_size 배열로 두는 것이 편리하다.
참조 : https://na982.tistory.com/95 
```

[아기상어 : BOJ 16236](https://www.acmicpc.net/problem/16236)
```
기존의 bfs 문제와는 많이 다르다.
상어의 이동은 bfs로 나타내고, 물고기를 만났을 때는 새로운 시작점이 되므로 '방문 여부 체크 배열(visited)와 큐(pq)를 모두 초기화 해준다.
ans는 물고기를 만났을 때만 더해준다. 그렇게 함으로써 물고기를 찾으러 나설 때는 시간 업데이트가 되지 않게 한다.
물고기는 같은 거리라도 '우선순위'가 존재하여 두가지 물고기를 모두 먹을 수 있는 경우의 수는 존재하지 않는다(본인이 실수 했던 부분)
물고기 먹는 처리를 push 할 때 처리하지 않고, pop할 때 처리한다.
참조 : https://rebas.kr/714 
```