
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <vector>

using namespace std;

const int BLOCK_SIZE = 16;
typedef unsigned int byte;

class block {
public:
    byte buf[BLOCK_SIZE];

    void show() {
        for(int i = 0; i < BLOCK_SIZE; i++)
            printf("%02x", buf[i]);
        printf("\n");
    }

    bool operator==(const block& bk) const {
        for(int i = 0; i < BLOCK_SIZE; i++)
            if(buf[i] != bk.buf[i])
                return false;
        return true;
    }
};

block cal_parity_bk(vector<block> bks) {
    block pbk;
    int i, j;
    for(i = 0; i < BLOCK_SIZE; i++)
        pbk.buf[i] = bks[0].buf[i];
    for(i = 0; i < BLOCK_SIZE; i++) 
        for(j = 1; j < bks.size(); j++)
            pbk.buf[i] = pbk.buf[i] ^ bks[j].buf[i];
    return pbk;
}

void restore_block(vector<block> bks, const int idx, const block pbk) {
    block mbk = bks[idx];
    bks[idx] = pbk;
    block rbk = cal_parity_bk(bks);
    bks[idx] = rbk;
    printf("missing idx %d, recovered %s - ", idx, mbk == rbk ? "yes": "no");
    rbk.show();
}

void show_vec(const vector<int>& v) {
    int i;
    for(i = 0; i < v.size(); i++)
        printf("%d ", v[i]);        
    printf("\n");
}

int cal_parity(const vector<int>& v) {
    int i;
    int p = v[0];
    for(i = 1; i < v.size(); i++)
        p = p ^ v[i];
    return p;
}

void restore_vec(vector<int> v, const int idx, const int p) {
    printf("missing idx %d of %d, ", idx, v[idx]);
    int m = v[idx];
    v[idx] = p;
    int r = cal_parity(v);
    printf("recover %d, recovered %s\n", r, r == m ? "yes": "no");
    v[idx] = r;
}

const int VEC_LEN = 3;
const int LOOP = 9;

int main() {
    srand(time(NULL));
    vector<int> v;
    int i;
    for(i = 0; i < VEC_LEN; i++)
        v.push_back(rand() % 10000);
    show_vec(v);
    int p = cal_parity(v);
    for(i = 0; i < LOOP; i++)
        restore_vec(v, rand() % VEC_LEN, p); 

    vector<block> bks;
    block b;
    for(i = 0; i < VEC_LEN; i++) {
        int j;
        for(j = 0; j < BLOCK_SIZE; j++)
            b.buf[j] = rand() % 256;
        b.show();
        bks.push_back(b);
    }
    block pbk = cal_parity_bk(bks);
    for(i = 0; i < LOOP; i++)
        restore_block(bks, rand() % VEC_LEN, pbk);
}

