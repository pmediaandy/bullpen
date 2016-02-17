CC = g++
CFLAGS = -O3 -Wall -std=c++11

.PHONY: clean

sraid: soft-raid.o crc.o
	${CC} $? -o $@

%.o: %.cc
	${CC} $< ${CFLAGS} -c

clean:
	rm -f sraid
	rm -f *.o
