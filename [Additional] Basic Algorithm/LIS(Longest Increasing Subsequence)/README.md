## LIS(Longest Increasing Subsequence)
  

가장 긴 증가하는 부분 수열 : [BOJ 11053](https://www.acmicpc.net/problem/11053)  
```C++
// O(N^2)
int _max = 1;
dp[0] = 1;
for(int i=1; i<n; i++){
    dp[i] = 1;
    for(int j=0; j<i; j++){
        if(arr[i] > arr[j] && dp[j] + 1 > dp[i]) {
            dp[i] = dp[j] + 1;
        }
    }
    if(_max < dp[i])
        _max = dp[i];
}
```
가장 긴 증가하는 부분 수열2 : [BOJ 12015](https://www.acmicpc.net/problem/12015)  
- 이 방식은 LIS 길이는 이분 탐색으로 빠르게 구할 수 있지만, 정확한 LIS 배열을 구하는 것은 아니다(★★)
```C++
// O(nLogn) 
dp[0] = array[0];
int idx = 0;
for(int i=0; i<n; i++){
    if(dp[idx] < array[i]) {
        dp[++idx] = array[i];
    }
    else {
        int j = lower_bound(idx, array[i]);
        dp[j] = array[i];
    }
}
// ans는 idx + 1
```
