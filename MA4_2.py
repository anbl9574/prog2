#!/usr/bin/env python3

from person import Person
import time
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter



def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def  fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())



if __name__ == '__main__':
	main()
	timelist=[]
	vector=[31,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
	for i in vector:
		t1_start = perf_counter() 
		fibresult=fib_py(i)
		t1_stop = perf_counter()
		timelist.append(t1_stop-t1_start)

	print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)
	print(timelist)