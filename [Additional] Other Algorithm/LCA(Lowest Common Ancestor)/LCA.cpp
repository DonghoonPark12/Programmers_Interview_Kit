#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
 
#define swap(a,b){int t = a; a = b; b = t;}
#define MAX_NODE 100001

using namespace std;

int depth[MAX_NODE];    // depth :: 노드의 깊이(레벨)
int ance[MAX_NODE][20]; // ance[x][y] :: x의 2^y번째 조상을 의미

typedef pair<int, int> pii;
vector<int> graph[MAX_NODE];
 
int max_level;

// DP(ance)를 만드는 과정
void getTree(int here, int parent){
    depth[here] = depth[parent] + 1;        // here의 깊이는 부모 노드의 깊이 + 1
    ance[here][0] = parent;                 // here의 1번째 조상은 부모노드
    max_level = (int)floor(log2(MAX_NODE)); // MAX_NODE에 log2를 씌어 내림을 해준다.

    for(int i=1; i<=max_level; i++){
        /*
            here의 2^i 번째 조상은 tmp의 2^(i-1) 번째 
            예를 들어,
            i=3일때 hear의 8번째 조상은 tmp의 4번째 조상과 같다.
            i=4일때 hear의 16번째 조상은 tmp의 8번째 조상과 같다.
        */
       int tmp = ance[here][i-1];
       ance[here][i] = ance[tmp][i-1];
    }

    //dfs 알고리즘
    int len = graph[here].size();
    for(int i=0; i<len; i++){
        int there = graph[here][i];
        if(there != parent)
        getTree(there, here);
    }
}

int main(){
    int n, m;
    scanf("%d", &n);

    //양방향 그래프 형성
    for(int i=1;i<n;i++){
        int from, to;
        scanf("%d %d", &from, &to);
        graph[from].push_back(to);
        graph[to].push_back(from);
    }

    depth[0] = -1; // make_tree에 1,0이 들어가기때문에 0은 -1로 지정

    getTree(1, 0); // 루트 노드인 1번 노드부터 트리 형성
    
    scanf("%d", &m); // 쿼리문 시작

    while(m--){
        
    }

}