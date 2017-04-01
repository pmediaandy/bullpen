#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int i;
    int N = (int) A.size();
    vector<int> stk;
    for(i = 0; i < N; i++) {
        if(stk.size() >= 1) {
            if(stk.back() != A[i]) 
                stk.pop_back();
            else 
                stk.push_back(A[i]);
        }
        else 
            stk.push_back(A[i]);
    }
    if(stk.size() == 0)
        return -1;
    int l = stk.back();
    int cnt = 0;
    int idx = -1;
    for(i = 0; i < N; i++) {
        if(A[i] == l) {
            cnt++;
            idx = i;
        }
    }
    if(cnt > N / 2)
        return idx;
    return -1;
}
