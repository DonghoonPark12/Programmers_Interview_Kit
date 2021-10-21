#include <iostream>
using namespace std;

int arr[1001];
int dp[1001];

int main() {
	int n; cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	int _max = 1;
	dp[0] = 1;//처음의 길이는  1

	for (int i = 1; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j] && dp[j] + 1 > dp[i]) {//i번째 원소(마지막이라고 가정하는 원소)가 j번째 원소보다 크고, j번째 원소까지의 부분 수열에
				dp[i] = dp[j] + 1;					   //i번째 원소를 추가해주는 것이므로 dp[i]에 dp[j]+1을 넣어준다. 
			}
		}
		if (_max < dp[i])
			_max = dp[i];
	}
	cout << _max << endl;

	return 0;
}
