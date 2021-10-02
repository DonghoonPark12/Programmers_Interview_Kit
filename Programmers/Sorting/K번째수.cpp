#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int>::iterator it = array.begin();
    vector<int> tmp;
    for(int i=0;i<commands.size();i++){
        tmp.assign(it + commands[i][0]-1, it + commands[i][1]);
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp.at(commands[i][2] - 1));
    }
    return answer;
}
