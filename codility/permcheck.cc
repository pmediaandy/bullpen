#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int i;
    int N = (int) A.size();
    map<int, int> mm;
    int mx = 1;
    for(i = 0; i < N; i++) {
        mx = max(mx, A[i]);
        map<int, int>::iterator it = mm.find(A[i]);
        if(it == mm.end()) 
            mm[A[i]] = 1;
        else {
            mm[A[i]]++;
            return 0;
        }
    }
    if(N == mx)
        return 1;
    return 0;
}

