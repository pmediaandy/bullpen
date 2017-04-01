#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(int A, int B, int K) {
    int ma = A % K;
    int mb = B % K;
    if(ma == 0 && mb == 0) {
        return (B - A) / K + 1;
    }
    else if(ma == 0 && mb != 0) {
        return ((B - mb) - A) / K + 1;
    }
    else if(ma != 0 && mb == 0) {
        return (B - (A + (K - ma))) / K + 1;
    }
    else {
        return ((B - mb) - (A + (K - ma))) / K + 1;
    }
}

