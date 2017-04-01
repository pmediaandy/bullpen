#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<int> solution(string &S, vector<int> &P, vector<int> &Q) {
    int N = (int) S.size();
    vector<int> a[4];
    int i;
    for(i = 0; i < N; i++) {
        if(S[i] == 'A') 
            a[0].push_back(i);
        else if(S[i] == 'C') 
            a[1].push_back(i);
        else if(S[i] == 'G') 
            a[2].push_back(i);
        else if(S[i] == 'T') 
            a[3].push_back(i);
    }
    vector<int> res;
    int M = (int) P.size();
    for(i = 0; i < M; i++) {
        int s, t;
        bool flag = false;
        for(s = 0; s < 4; s++) {
            for(t = 0; t < (int) a[s].size(); t++) {
                if(a[s][t] >= P[i] && a[s][t] <= Q[i]) {
                    res.push_back(s + 1);
                    flag = true;
                    break;
                }
            }
            if(flag)
                break;
        }
    }
    return res;
}
