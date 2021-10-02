/*
dfs로 그래프 탐색하면서 방문되었을 경우 visit 배열을 trigger 시킨다.
e.g.
첫번재 dfs 탐색에서 모든 노드가 방문되었다면, 1을 리턴한다.
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool visit[200];

void dfs(int start, vector<vector<int>> &computers, int n) {
    visit[start]=1;
    for(int i=0;i<n;i++)
    {
        if(!visit[i] && computers[start][i])
            dfs(i, computers, n);
    }

}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i=0; i<n; i++) //모든 노드를 시작점으로 하여 dfs 탐색 시행
    {
        if(!visit[i])
        {
            answer++;
            dfs(i, computers, n);
        }
    }
    return answer;
}
