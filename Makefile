
CC = g++
CFLAGS = -c -Wall

all: sraid

clean: 
	rm -rf o.* *.o

sraid: soft-raid.cc
	g++ -o o.sraid $<


