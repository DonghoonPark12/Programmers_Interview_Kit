#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/*
 - 노드의 갯수 만큼 (벡터, 방문 여부 배열)를 만들어 주는 것이 일반적인가?
*/

int arr[100001];
bool visited[100001];
vector<int> node[100001];

void dfs(int pr) {
	visited[pr] = true;
	for (int i = 0; i < node[pr].size(); i++) {
		int next = node[pr][i];
		if (!visited[next]) {
			arr[next] = pr; //k 옆가지들이 next이며, next의 부모는 'k'
			dfs(next);
		}
	}
}

void bfs(int pr) {
	visited[pr] = true;
	queue<int> qu;
	qu.push(pr);
	while (!qu.empty()) {
		int cur = qu.front();
		qu.pop();
		for (int i = 0; i < node[cur].size(); i++) {
			int next = node[cur][i];
			if (!visited[next]) {
				arr[next] = cur;
				visited[next] = true;
				qu.push(next);
			}
		}
	}
}

int main() {
	int n; cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int x, y; cin >> x >> y;
		node[x].push_back(y);
		node[y].push_back(x);
	}

	//dfs(1);
	bfs(1);
	for (int i = 2; i <= n; i++) {
		//printf("%d\n", arr[i]);
		cout << arr[i] << '\n';
	}
	return 0;
}

/*
1 - 6 - 3 - 5
 |- 4 - 7
     |- 2   
*/