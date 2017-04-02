#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

/*
([4,3,2,1,5, 6],[0, 0, 1, 1, 0, 0])
([4,3,2,1,5, 6],[0, 1, 0, 0, 0, 1])
([4,3,2,1,5, 6],[0, 1, 0, 0, 0, 0])
([4,3,2,1,5, 0],[0, 1, 0, 0, 0, 0])
([11,9,4,3,2,1,10], [1,1,1,1,1,1,0])
*/

int solution(vector<int> &A, vector<int> &B) {
    int i;
    int N = (int) A.size();
    vector<int> stk;
    for(i = 0; i < N; i++) {
        if(stk.size() > 0) {
            while(stk.size() > 0 && B[i] - B[stk.back()] == -1 && A[stk.back()] < A[i])
                stk.pop_back();
            if(stk.size() > 0) {
                if(B[i] - B[stk.back()] != -1)
                    stk.push_back(i);
            }
            else 
                stk.push_back(i);
        }
        else
            stk.push_back(i);
    }
    return stk.size();
}

int solution2(vector<int> &A, vector<int> &B) {
    int i;
    int N = (int) A.size();
    vector< pair<int, int> > stk;
    for(i = 0; i < N; i++) {
        if(stk.size() > 0) {
            if(B[i] == 1)
                stk.push_back(pair<int, int>(B[i], A[i]));
            else if(B[i] == 0) {
                pair<int, int> p = stk.back();
                if(p.first == 1 && A[i] < p.second) {
                }
                else if(p.first == 1 && A[i] > p.second) {
                    do {
                        stk.pop_back();
                        p = stk.back();
                    } while(stk.size() > 0 && p.first == 1 && A[i] > p.second);
                    if(p.first == 1 && A[i] < p.second)
                        ;
                    else
                        stk.push_back(pair<int, int>(B[i], A[i]));
                }
                else if(p.first == 0) 
                    stk.push_back(pair<int, int>(B[i], A[i]));
            }
        }
        else
            stk.push_back(pair<int, int>(B[i], A[i]));
    }
    return stk.size();
}

int solution_wrong(vector<int> &A, vector<int> &B) {
    int i;
    int N = (int) A.size();
    int die = 0;
    for(i = 0; i < N; i++) {
        if(B[i] == 1 && i + 1 < N && B[i + 1] == 0) {
            int j = i + 1;
            while(j < N && B[j] == 0)
                j++;
            int a = i + 1, b = j - 1;
            bool eaten = false;
            for(j = a; j <= b; j++) {
                if(A[j] < A[i])
                    die++;
                else if(A[j] > A[i]) {
                    eaten = true;
                    break;
                }
            }
            if(eaten)
                die++;
        }
    }
    return N - die;
}
