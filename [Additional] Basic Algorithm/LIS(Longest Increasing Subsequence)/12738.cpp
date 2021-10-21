#include <cstdio>
#include <algorithm>
using namespace std;

int _lower_bound(int st, int end, int *arr, int target){
    int mid;
    while(end - st > 0){ // st == end 이면 종료
        mid = (st + end) / 2; 
        
        if(arr[mid] < target)
            st = mid + 1; //찾고자 하는 값보다 중간 값이 작으면, 중간값 + 1
        else
            end = mid;    // 찾고자 하는 값보다 중간 값이 크면 Lower Bound 갱신
    }
    return end + 1;
}

int main()
{
    int i, n, j = 0;
    int cnt = 0;
    int dp[1000001];  //수열의 크기 10^6
    int arr[1000001]; //수열의 크기 10^6
    scanf("%d", &n);
 
    for (i = 0; i<n; ++i)
        scanf("%d", &arr[i]);

    i = 0;
    dp[i] = arr[i];
    for(int i=1; i<n; i++){
        //dp의 가장 큰 값보다 더 큰 값이 들어오면
        if(dp[j] < arr[i])
        {
            dp[j + 1] = arr[i]; //dp배열에 arr[i] 값 추가
            j++;
        }
        else{
            int ans = _lower_bound(0, j, dp, arr[i]);
            dp[ans - 1] = arr[i];
        }
    }

    printf("%d", j + 1);
}