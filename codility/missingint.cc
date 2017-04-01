#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int N = (int) A.size();
    map<int, int> mm;
    int i;
    long long mx = -1;
    for(i = 0; i < N; i++) {
        map<int, int>::iterator it = mm.find(A[i]);
        if(it == mm.end()) {
            mm[A[i]] = 1;
        }
        else {
            mm[A[i]]++;
        }
        if(A[i] > 0)
            mx = max(mx, (long long)A[i]);
    }
    for(i = 1; i <= mx + 1; i++) {
        if(mm.find(i) == mm.end())
            return i;
    }
    return 1;
}

