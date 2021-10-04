#include <iostream>
#include <queue>
using namespace std;

struct shark {
	int dis, x, y;
	bool operator < (const shark &sh) const {
		if (dis == sh.dis) {     //거리가 같다면
			if (x == sh.x)
				return y > sh.y; //y가 더 작은 것. 즉, 위에 있는 것
			else
				return x > sh.x; //x가 더 작은 것. 즉, 왼쪽에 있는 것
		}
		else {
			return dis > sh.dis; //거리가 같지 않다면, 더 가까운 것
		}
	}
};

int n, ans;
int body; //상어의 크기
int eat; //물고기 먹은 횟수
int map[20][20];
priority_queue<shark> pq;
const int dy[4] = { -1, 0, 1, 0 }; //U, L, D, R
const int dx[4] = { 0, -1, 0, 1 };

bool visited[20][20];

void bfs() {
	while (!pq.empty()) {
		int dis = pq.top().dis, x = pq.top().x, y = pq.top().y;
		pq.pop();
		if (0 < map[x][y] && map[x][y] < body) {
			map[x][y] = 0;
			eat++;
			if (eat == body) {
				body++; eat = 0;
			}
			ans += dis;
			// Initializing distance, visited check, and queue.
			dis = 0;
			memset(visited, false, sizeof(visited));
			while (!pq.empty()) pq.pop();
		}

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			// Cannot pass if fish is bigger than shark, or already visited.
			if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
			if (visited[nx][ny]) continue;
			if (0 < map[nx][ny] && map[nx][ny] > body) continue;

			// Update next moving.
			pq.push({ dis + 1, nx, ny });
			visited[nx][ny] = true;
		}
	}
}

void solve() {
	bfs();
	printf("%d\n", ans);
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 9) {
				pq.push({ 0, i, j });
				map[i][j] = 0;
			}
		}
	}
    body = 2;
	solve();
	return 0;
}
