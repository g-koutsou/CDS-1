CC=icc
CFLAGS=-O3 -axMIC-AVX512 -std=gnu99 -qopenmp
LDFLAGS=
LIBS=-lm -qopenmp
all:
	@echo make what?

.PHONY: A B C


A: lapl
B: laplt
C: laplv

lapl: lapl.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS)

laplt: laplt.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS)

laplv: laplv.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS)

clean:
	$(RM) lapl laplt laplv
