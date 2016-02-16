CC = g++
CFLAGS = -O3 -Wall

.PHONY: clean

sraid: soft-raid.o
	${CC} $< -o $@

%.o: %.cc
	${CC} $< ${CFLAGS} -c

clean:
	rm -f sraid
	rm -f *.o
