#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int N = (int) A.size();
    vector<int> sum;
    int i;
    int s = 0;
    for(i = 0; i < N; i++) {
        s += A[i];
        sum.push_back(s);
    }
    int mn = 20000;
    for(i = 1; i < N; i++) {
        int d = abs(sum[i-1] - (sum[N-1] - sum[i-1]));
        mn = min(d, mn);
    }
    return mn;
}
