#include <iostream>
#include <algorithm>
using namespace std;

int arr[100000];

void binary_search(int n, int key){
	int st = 0;
	int _end = n - 1; //ex) n = 5 , arr[0] ~ arr[4]
	int mid;
	while (_end - st >= 0){
		mid = (st + _end) / 2;
		if (arr[mid] == key){
			cout << '1' << '\n'; return;
		}
		else if (arr[mid] > key)
			_end = mid - 1;
		else
			st = mid + 1;
	}
	cout << '0'<<'\n'; return;
}

int main(){
	int n, m, input;
    cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}
	sort(arr, arr + n);
	cin >> m;
	for (int i = 0; i < m; i++){
		cin >> input;
		binary_search(n, input);
	}
}
