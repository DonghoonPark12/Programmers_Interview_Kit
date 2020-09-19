#include <string>
#include <vector>
#include<iostream>
#include<algorithm>
using namespace std;
int camera[10001]; 


int solution(vector<vector<int>> routes) {
    int answer = 0;
    int n = routes.size();
    // sort by increasing order of the starting point
    sort(routes.begin(), routes.end()); //앞의 숫자로 Sorting
    int k =0; 
    // get the first sorted pair 
    // set the limit of the first camera to be installed as 
    // the first pair's ending point 
    camera[k]= routes[0][1]; 
    
    for(int i=1; i<n; i++){
        if(camera[k]>routes[i][0] && camera[k]>routes[i][1]){
           camera[k]=routes[i][1];   
        }
        else if(routes[i][0]>camera[k]){
            k++; 
            // new limit 
            camera[k]=routes[i][1]; 
        }
    }
    answer=k+1; 
   
    return answer;
}
