/*
    1. dp 배열에 아무 값이 없다면 배열(arr)의 첫번째 값을 넣는다.
    2. dp 배열의 가장큰 값(가장 오른쪽에 있는 값, dp[idx]) 보다 
       현재 보고 있는 값(array[i])이 크다면 dp배열에 array[i] 값을 추가한다.
    3. 그 외에는 lower_bound(작거나 같은 원소)를 이용하여 dp 위치에 넣어준다.
*/

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
    for(int i=1; i<n; i++) {
        //dp의 가장 큰 값보다 더 큰 값이 들어오면
        if(dp[j] < arr[i]) {
            dp[++j] = arr[i]; //dp배열에 arr[i] 값 추가
        }
        else{
            int ans = _lower_bound(0, j, dp, arr[i]);
            dp[ans - 1] = arr[i];
        }
    }

    printf("%d", j + 1);
}


#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int _lower_bound(int st, int end, int *arr, int target) {
	int mid;
	while (end - st > 0) { // st == end 이면 종료
		mid = (st + end) / 2;

		if (arr[mid] < target)
			st = mid + 1; //찾고자 하는 값보다 중간 값이 작으면, 중간값 + 1
		else
			end = mid;    // 찾고자 하는 값보다 중간 값이 크면 Lower Bound 갱신
	}
	return end + 1;
}

int main()
{
	int i, n, j = 0;
	vector<int> vt;
	scanf("%d", &n);

	int val;
	for (i = 0; i < n; ++i) {
		scanf("%d", &val);
		vt.push_back(val);
	}

	vector<int> dp(n + 1, 1000001);

	for (int i = 0; i < n; i++) {
		auto it = lower_bound(dp.begin(), dp.end(), vt[i]) - dp.begin(); //인덱스로 만든다.
		dp[it] = vt[i];
	}
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (dp[i] != 1000001)
			cnt++;
	}

	printf("%d", cnt);
	return 0;
}