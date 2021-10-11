## Dynamic Programming

- SW 역량 테스트 준비 - 기초 : [다이나믹 프로그래밍](https://www.acmicpc.net/workbook/codeplus/1) 에서 기억에 남는 문제 정리  
   
    - 1로 만들기 : [BOJ 1463](https://www.acmicpc.net/problem/1463) 
    ```
    (좋은 문제)
    i가 3로 나누어 떨어진다면, '3으로 나눠진곳(DP[i/3]) + 1'과 비교한다.
    i가 2로 나누어 떨어진다면, '2으로 나눠진곳(DP[i/2]) + 1'과 비교한다.
    DP[i] = DP[i-1] + 1은 +1 연산은 기본적으로 적용되므로 수행한다.
    ```