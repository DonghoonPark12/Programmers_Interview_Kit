#include <iostream>
#include <vector>
using namespace std;

int score[1000001];
int sum_score[1000001];

int main() {
	int n, k; cin >> n >> k;
	int tmp;
	for (int i = 1; i <= n; i++) {
		cin >> score[i];
		if (i == 1) {
			sum_score[i] = score[i];
		}
		else {
			sum_score[i] = sum_score[i - 1] + score[i]; //O(N)
		}
	}

	int st, end;
	while (k--) {
		float avg = 0;
		cin >> st >> end;
		avg = sum_score[end] - sum_score[st - 1];

		printf("%.2f\n", avg /(end - st + 1));
	}
	return 0;
}