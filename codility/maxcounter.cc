#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<int> solution(int N, vector<int> &A) {
    int M = (int) A.size();
    vector<int> C;
    int i;
    for(i = 0; i < N; i++)
        C.push_back(0);
    int mx = 0;
    int acc = 0;
    for(i = 0; i < M; i++) {
        if(A[i] == N + 1) {
            acc = mx;
        }
        else {
            C[A[i]-1] = max(C[A[i]-1], acc);
            C[A[i]-1]++;
            mx = max(mx, C[A[i]-1]);
        }
    }
    for(i = 0; i < N; i++) {
        C[i] = max(C[i], acc);
    }
    return C;
}
