#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <string.h>

using namespace std;

std::vector<std::string> split(std::string str,std::string sep) {
    char* cstr=const_cast<char*>(str.c_str());
    char* current;
    std::vector<std::string> arr;
    current=strtok(cstr,sep.c_str());
    while(current!=NULL){
        arr.push_back(current);
        current=strtok(NULL,sep.c_str());
    }
    return arr;
}

int solution(string &S) {
    int i;
    vector<string> cmds = split(S, " ");
    int N = (int) cmds.size();
    vector<int> stk;
    for(i = 0; i < N; i++) {
        if(cmds[i] == string("DUP")) {
            if(stk.size() == 0)
                return -1;
            else
                stk.push_back(stk.back());
        }
        else if(cmds[i] == string("POP")) {
            if(stk.size() == 0)
                return -1;
            else
                stk.pop_back();
        }
        else if(cmds[i] == string("+")) {
            if(stk.size() < 2)
                return -1;
            else {
                int a = stk.back(); stk.pop_back();
                int b = stk.back(); stk.pop_back();
                if(a + b > 1048575)
                    return -1;
                else
                    stk.push_back(a + b);
            }
        }
        else if(cmds[i] == string("-")) {
            if(stk.size() < 2)
                return -1;
            else {
                int a = stk.back(); stk.pop_back();
                int b = stk.back(); stk.pop_back();
                if(a - b < 0)
                    return -1;
                else
                    stk.push_back(a - b);
            }
        }
        else {
            int n = atoi(cmds[i].c_str());
            stk.push_back(n);
        }
    }
    if(stk.size() == 0)
        return -1;
    return stk.back();
}

