#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

bool check_words(string a, string b){
    int sz = a.length(); 
    int cnt =0; 
    for(int i=0; i<sz; i++){
        if(a[i]==b[i]) cnt++; 
    }
    if(cnt==sz-1) return true; 
    else return false; 
}; 

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int n = words.size(); 
    queue<pair<int, int>>q; // index of word, level 
    bool visited[51]; 
    for(int i=0; i<51; i++) visited[i]=false; 
    //1. check if the word is contained in words
    bool hastarget=false; 
    for(int i=0; i<n; i++){
        if(words[i]==target) hastarget=true; 
    }
    if(hastarget==false) return 0; 
    
    int idx =0; 
    int level = 1; 
    while(1){
        for(int i=0; i<n ; i++){
            if(check_words(begin, words[i])==true && visited[i]==false){
                if(words[i]==target) return level; 
                q.push(make_pair(i, level)); //words의 인덱스와 Level 저장. 
                visited[i]=true; 
            }
        }
        answer = level; 
        //level++; 
        begin=words[q.front().first]; //인덱스를 가진 words가 begin이며(hot)
        level = q.front().second+1;  //level을 1 더해준다.
        q.pop(); 
    }
    
    return answer;
}
