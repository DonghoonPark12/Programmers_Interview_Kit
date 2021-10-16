## LIS(Longest Increasing Subsequence)
  

가장 긴 증가하는 부분 수열 : [BOJ 11053](https://www.acmicpc.net/submit/11053/15543958)
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