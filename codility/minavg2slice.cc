#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    int i;
    int N = (int) A.size();
    int s = 0;
    vector<int> sum;
    for(i = 0; i < N; i++) {
        s += A[i];
        sum.push_back(s);
    }
    int idx = -1;
    float mn = 2147483647;
    for(i = 0; i < N - 1; i++) {
        int j;
        for(j = i + 1; j < N; j++) {
            float avg;
            if(i == 0) 
                avg = float(sum[j]) / (j - i + 1);
            else 
                avg = float(sum[j] - sum[i - 1]) / (j - i + 1);
            if(avg < mn) {
                mn = avg;
                idx = i;
            }
            if(j - i + 1 >= 3)
                break;
        }
    }
    return idx;
}
