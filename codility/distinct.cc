#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

void bin_ins_sort(vector<int>& a, int v) {
    int l = 0;
    int r = int(a.size()) - 1;
    while(l <= r) {
        int m = (l + r) / 2;
        if(a[m] > v)
            r = m - 1;
        else if(a[m] < v)
            l = m + 1;
        else {
            l = m;
            break;
        }
    }
    if(l >= int(a.size()))
        a.push_back(v);
    else
        a.insert(a.begin() + l, v);
}

int solution(vector<int> &A) {
    int i;
    int N = (int) A.size();
    if(N == 0)
        return 0;
    map<int, int> mm;
    sort(A.begin(), A.end());
    int cnt = 1;
    for(i = 1; i < N; i++) {
        if(A[i] != A[i-1])
            cnt++;
    }
    return cnt;
}

int solution2(vector<int> &A) {
    int i;
    int N = (int) A.size();
    map<int, int> mm;
    for(i = 0; i < N; i++) {
        if(mm.find(A[i]) == mm.end()) 
            mm[A[i]] = 1;
        else
            mm[A[i]]++;
    }
    return mm.size();
}
