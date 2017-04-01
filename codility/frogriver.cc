#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(int X, vector<int> &A) {
    int i;
    int N = (int) A.size();
    int *nx = new int[X];
    int cnt = X;
    for(i = 0; i < X; i++)
        nx[i] = 0;
    int t = -1;
    for(i = 0; i < N; i++) {
        if(nx[A[i]-1] == 0) {
            nx[A[i]-1] = 1;
            cnt--;
        }
        if(cnt == 0) {
            t = i;
            break;
        }
    }
    delete [] nx;
    return t;
}

