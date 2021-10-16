#include <iostream>
#include <vector>
using namespace std;

int main() {
	long long K;
	int P, N; cin >> K >> P >> N;
    N *= 10;
	while (N--) {
		K = (((K % 1000000007) * (P % 1000000007)) % 1000000007);
	}
	cout<<K<<'\n';
	return 0;
}