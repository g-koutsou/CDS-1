CC=icc
CFLAGS=-O3 -axMIC-AVX512 -xKNL -std=gnu99
LDFLAGS=
LIBS=-lm

ifneq ($(VL),)
CFLAGS += -DVL=$(VL)
endif

all:
	@echo make what?

.PHONY: A B

A: space-time-aos
B: space-time-soa

space-time-aos: space-time-aos.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS) -qopenmp

space-time-soa: space-time-soa.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS) $(LIBS) -qopenmp

clean:
	$(RM) space-time-aos space-time-soa
