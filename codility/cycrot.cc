#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<int> solution(vector<int> &A, int K) {
    int N = (int) A.size();
    if(N == 0)
        return A;
    int k = K % N;
    if(k == 0)
        return A;
    int i;
    for(i = 0; i < N - k; i++) {
        int v = A[0];
        A.erase(A.begin());
        A.push_back(v);
    }
    return A;
}

