#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    long long N = (long long) A.size();
    if(N == 0) 
        return 1;
    long long sum = ((1 + (N + 1)) * (N + 1)) / 2;
    int i;
    for(i = 0; i < N; i++)
        sum -= (long long) A[i];
    return sum;
}
