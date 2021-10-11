## Tree

### 트리의 입력
1. Vector로 입력 받는 방법(Graph와 동일)
```c++
for (int i = 0; i < n ; i++) {
    int x, y; cin >> x >> y;
    node[x].push_back(y);
    node[y].push_back(x);
}
```
  

- 트리 순회 : [BOJ 1991](https://www.acmicpc.net/problem/1991)  
- 트리의 부모 찾기 : [BOJ 11725](https://www.acmicpc.net/problem/11725)  


