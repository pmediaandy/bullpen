
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <vector>

#include "block.h"

using namespace std;

block cal_parity(const vector<block>& bks) {
    block pbk;
    size_t i, j;
    pbk = bks[0];
    for(i = 0; i < BLOCK_SIZE; i++) 
        for(j = 1; j < bks.size(); j++)
            pbk.buf[i] = pbk.buf[i] ^ bks[j].buf[i];
    return pbk;
}

void restore_block(vector<block>& bks, const int idx, const block pbk) {
    block mbk = bks[idx];
    bks[idx] = pbk;
    block rbk = cal_parity(bks);
    bks[idx] = rbk;
    printf("missing idx %d, recovered %s - ", idx, mbk == rbk ? "yes": "no");
    rbk.show();
}

const int VEC_LEN = 3;
const int LOOP = 9;

int main() {
    srand(time(NULL));
    vector<block> bks;
    block b;
    for(size_t i = 0; i < VEC_LEN; i++) {
        for(size_t j = 0; j < BLOCK_SIZE; j++)
            b.buf[j] = rand() % 256;
        b.cal_crc();
        b.show();
        bks.push_back(b);
    }
    block pbk = cal_parity(bks);
    for(size_t i = 0; i < LOOP; i++)
        restore_block(bks, rand() % VEC_LEN, pbk);
}

