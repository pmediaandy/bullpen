#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(string &S) {
    int i;
    int N = (int) S.size();
    vector<char> stk;
    for(i = 0; i < N; i++) {
        if(S[i] == '{' || S[i] == '[' || S[i] == '(')
            stk.push_back(S[i]);
        else if(S[i] == '}') {
            if(stk.size() > 0 && stk.back() == '{')
                stk.pop_back();
            else
                return 0;
        }
        else if(S[i] == ']') {
            if(stk.size() > 0 && stk.back() == '[')
                stk.pop_back();
            else
                return 0;
        }
        else if(S[i] == ')') {
            if(stk.size() > 0 && stk.back() == '(')
                stk.pop_back();
            else
                return 0;
        }
    }
    if(stk.size() == 0)
        return 1;
    return 0;
}
