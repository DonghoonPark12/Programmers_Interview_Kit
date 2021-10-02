/*
dfs가 아닌 재귀로 해결
traget을 목표로 뺐을때와 더했을 때 경우를 나누어서 탐색
*/
#include <string>
#include <vector>

using namespace std;

int ans = 0;
int sum;
int id;
void target_number(vector<int> numbers, int target){
    if(id == numbers.size()){
        if(target == 0) {
            ans++; return;
        }
        else{
            id--; return;
        }
    }
    else
        id++;

    target_number(numbers, target + numbers[id]);
    target_number(numbers, target - numbers[id]);
}
 
int solution(vector<int> numbers, int target) {
    target_number(numbers, target);
    return ans;
}
