#include <iostream>
#include <vector>
using namespace std;

char map[25][25];
bool visitied[25][25];
int H, W;

int dx[4]  = { -1, 0, 1, 0 };  //L, U, R, D
int dy[4]  = { 0, -1, 0, 1 };
char order[4] = { '<', '^', '>','v' };

int main() {
	char dir;  // 최초 방향을 저장
	int n, prev_n;

	cin >> H >> W;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cin >> map[i][j];
		}
	}

	// (1) 시작지점 찾기
	int stx = -1, sty = -1;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (map[i][j] == '#') {
				int cnt = 0;
				for (n = 0; n < 4; n++) {
					if (i + dy[n] < 0 || i + dy[n] < 0 >= H || j + dx[n] < 0 || j + dx[n] >= W)
						continue;
					/////
					if (map[i + dy[n]][j + dx[n]] == '#')
						cnt++;
					/////
				}
				if (cnt == 1) {
					sty = i, stx = j;
				}
			}
		}
	}

	//(2) 지나온 경로 추적
	vector<char> v;
	int cy = sty, cx = stx; 

	int cnt; //종료를 결정
	
	// 최초 방향 정함
	for (n = 0; n < 4; n++) {
		if (cy + dy[n] < 0 || cy + dy[n] < 0 >= H || cx + dx[n] < 0 || cx + dx[n] >= W)
			continue;
		if (map[cy + dy[n]][cx + dx[n]] == '#') {
			dir = order[n];
			prev_n = n;
			break;
		}
	}

	visitied[cy][cx] = true;
	while (1) {
		cnt = 0;
		cy += (dy[prev_n]);	cx += (dx[prev_n]);	visitied[cy][cx] = true;
		cy += (dy[prev_n]);	cx += (dx[prev_n]);	visitied[cy][cx] = true;
		v.push_back('A');

		for ( n = 0; n < 4; n++) {
			if (cy + dy[n] < 0 || cy + dy[n] < 0 >= H || cx + dx[n] < 0 || cx + dx[n] >= W)
				continue;
			// 여기서 최소한의 방향을 저장해야, 방문 안되었고, '#' 이며, 방향이 다르다면
			if ((!visitied[cy + dy[n]][cx + dx[n]]) && (map[cy + dy[n]][cx + dx[n]] == '#')){
				if (n != prev_n) {
					if ((prev_n + 1) % 4 == n)
						v.push_back('R');
					else
						v.push_back('L');
					prev_n = n;
				}
				cnt++;
				break;
			}
		}
		if (cnt == 0)
			break;
	}

	// (3) 출력
	cout << sty + 1 << ' ' << stx + 1 << '\n';
	cout << dir << '\n';
	for (int i = 0; i <v.size(); i++) {
		cout << v[i];
	}

	return 0;
}