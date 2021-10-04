#include <iostream>
#include <queue>
using namespace std;



struct CCTV {
	int type, y, x;
};

int n, m, ret;
int map[8][8];
int cctv_size;
CCTV cctv[8];

const int rot_size[] = { 4, 2, 4, 4, 1 };

void map_copy(int desc[8][8], int src[8][8]) {
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < m; x++) {
			desc[y][x] = src[y][x];
		}
	}
}

void update(int dir, CCTV cctv) {
	dir = dir % 4;

	//right
	if (dir == 0) {
		for (int x = cctv.x + 1; x < m; ++x) {
			if (map[cctv.y][x] == 6) break;
			map[cctv.y][x] = -1;
		}
	}
	//up
	if (dir == 1) {
		for (int y = cctv.y - 1; y >= 0; --y) {
			if (map[y][cctv.x] == 6) break;
			map[y][cctv.x] = -1;
		}
	}
	//left
	if (dir == 2) {
		for (int x = cctv.x - 1; x >=0 ; --x) {
			if (map[cctv.y][x] == 6) break;
			map[cctv.y][x] = -1;
		}
	}
	//down
	if (dir == 3) {
		for (int y = cctv.y + 1; y < n; ++y) {
			if (map[y][cctv.x] == 6) break;
			map[y][cctv.x] = -1;
		}
	}
}

void dfs(int cctv_index) {
	if (cctv_index == cctv_size) {
		int value = 0;
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < m; x++) {
				if (map[y][x] == 0)
					++value;
			}
		}
		if (ret > value)
			ret = value;
		return;
	}

	int backup[8][8];
	int type = cctv[cctv_index].type;
	for (int dir = 0; dir < rot_size[type]; dir++) {
		//1. Map backup
		map_copy(backup, map);

		//2. draw map
		switch (type)
		{
		case 0:
			update(dir, cctv[cctv_index]); // dir : 0 ~ 3
			break;
		case 1:
			update(dir, cctv[cctv_index]); //(0, 2), (1, 3)
			update(dir + 2, cctv[cctv_index]);
			break;
		case 2:
			update(dir, cctv[cctv_index]); //(0, 1), (1, 2), (2, 3), (3, 0)
			update(dir + 1, cctv[cctv_index]);
			break;
		case 3:
			update(dir, cctv[cctv_index]); //(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)
			update(dir + 1, cctv[cctv_index]);
			update(dir + 2, cctv[cctv_index]);
			break;
		case 4:
			update(dir, cctv[cctv_index]);
			update(dir + 1, cctv[cctv_index]);
			update(dir + 2, cctv[cctv_index]);
			update(dir + 3, cctv[cctv_index]);
			break;
		}


		dfs(cctv_index + 1);
		//3. Map restore
		map_copy(map, backup);
	}
}

int main()
{
	cin >> n >> m;
	int tmp;
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < m; x++) {
			cin >> tmp;
			map[y][x] = tmp;

			if (map[y][x] != 0 && map[y][x] != 6) {
				cctv[cctv_size].y = y;
				cctv[cctv_size].x = x;
				cctv[cctv_size].type = map[y][x] - 1;
				++cctv_size;
			}
		}
	}
	ret = 100;
	dfs(0);
	cout << ret << '\n';
	return 0;
}