#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int i;
    int N = (int) A.size();
    if(N <= 2)
        return 0;
    sort(A.begin(), A.end());
    for(i = 2; i < N; i++) {
        if((long long)A[i - 2] + A[i - 1] > A[i]) 
            return 1;
    }
    return 0;
}
