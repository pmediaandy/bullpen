#pragma once

#include <string.h>
#include <array>

#include "crc.h"

const int BLOCK_SIZE = 512;

typedef unsigned char byte;

template<typename T, size_t SZ>
class block_t {
public:
    std::array<T, SZ> buf;
    int crc32;

    block_t() {
        crc32 = 0;
    }

    int cal_crc() {
        crc32 = crc(buf.data(), SZ); 
        return crc32;
    }

    void show() {
        printf("%08x\n", crc32);
    }

    bool operator==(const block_t<T, SZ>& bk) const {
        for(size_t i = 0; i < SZ; i++)
            if(buf[i] != bk.buf[i])
                return false;
        return true;
    }

    block_t<T, SZ>& operator=(const block_t<T, SZ>& bk) {
        buf = bk.buf;
        crc32 = bk.crc32;
        return *this;
    }
};

typedef block_t<byte, BLOCK_SIZE> block;

