#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>
using namespace std;


vector<int> solution(vector<string> operations) {
    vector<int> answer;
    deque<int> que;
    string temp;
    
    for (int i = 0; i < operations.size(); i++) {
        if (operations[i][0] == 'I') {
            temp = operations[i].substr(2, string::npos);
            int a = stoi(temp);
            que.push_back(a);
        }
        else if (operations[i][0] == 'D') {
            temp = operations[i].substr(2, string::npos);
            int a = stoi(temp);
        if(!que.empty())
        if (a == -1) {
         que.pop_front();
        }
    else if(a == 1) {
     que.pop_back();
    }
    }
    }
 sort(que.begin(), que.end());

 if (que.empty())
  return { 0,0 };
 answer.push_back(que[que.size() - 1]);
 answer.push_back(que[0]);

 return answer;
}
