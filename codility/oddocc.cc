#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    map<int, int> mm;
    unsigned int i;
    for(i = 0; i < A.size(); i++) {
        map<int, int>::iterator it = mm.find(A[i]);
        if(it == mm.end()) {
            mm[A[i]] = 1;
        }
        else {
            mm[A[i]]++;
        }
    }
    map<int, int>::iterator it;
    for(it = mm.begin(); it != mm.end(); it++) {
        if(it->second % 2 == 1)
            return it->first;
    }
    return 0;
}
