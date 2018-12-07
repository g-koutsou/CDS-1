CC=icc
CFLAGS=-O3 -axMIC-AVX512 -std=gnu99 -qopenmp
LDFLAGS=
LIBS=-lm

all:
	@echo make what?

.PHONY: A B

A: mm-orig
B: mm-blck


mm-orig: mm.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS)

mm-blck: mm.c
	$(CC) $(CFLAGS) -DBLCK $< -o $@ $(LDFLAGS) $(LIBS)

clean:
	$(RM) mm-blck mm-orig
