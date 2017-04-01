#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int N = (int) A.size();
    int i;
    int s = 0;
    vector<int> sum;
    for(i = 0; i < N; i++) {
        s += A[i];
        sum.push_back(s);
    }
    int acc = 0;
    for(i = 0; i < N; i++) {
        if(A[i] == 0) {
            acc += sum[N-1] - sum[i];
            if(acc > 1000000000)
                return -1;
        }
    }
    return acc;
}

