#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int solution(vector<int>& A, int K) {
    int n = A.size();
    int best = 0;
    int count = 1;
    for (int i = 0; i < n - K - 1; i++) {
        if (A[i] == A[i + 1])
            count = count + 1;
        else
            count = 1;
        best = max(best, count);
        printf("best=%d\n", best);
    }
    if(best == n - K)
        return best;
    int result = best + K;

    return result;
}

int main() {
   vector<int> A;
   int i;
   int a[] = {1, 1, 3, 3, 3, 4, 5, 5, 5, 5};
   for(i = 0; i < sizeof(a) / sizeof(int); i++)
       A.push_back(a[i]); 
   cout << solution(A, 2) << endl;
   A.clear();
   int a2[] = {1, 1, 3, 4, 4, 5};
   for(i = 0; i < sizeof(a2) / sizeof(int); i++)
       A.push_back(a2[i]); 
   cout << solution(A, 2) << endl;
   A.clear();
   int a3[] = {3, 3, 3};
   for(i = 0; i < sizeof(a3) / sizeof(int); i++)
       A.push_back(a3[i]); 
   cout << solution(A, 2) << endl;
   return 0;
}
