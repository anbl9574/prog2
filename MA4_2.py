#!/usr/bin/env python3

from person import Person
import time
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter
from time import perf_counter as pc
from time import sleep as pause


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
	
	fib47=Person(47)
	fib47numba=fib_numba(47)
	print(fib47)
	print(fib47numba)
	vector=[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
	timelist=[]
	timeFibC=[]
	timelist2=[]

	for i in vector:	
		t2_start = perf_counter()
		fib=Person(i)
		t2_stop = perf_counter()
		timeFibC.append(t2_stop-t2_start)
		print(timeFibC)
	
		
#	vector=[4,5]
	vector=[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
	for i in vector:


            t1_start = perf_counter() 
            fibresult=fib_numba(i)
            t1_stop = perf_counter()
            timelist.append(t1_stop-t1_start)

	for i in vector:


            t1_start = perf_counter() 
            fibresult=fib_py(i)
            t1_stop = perf_counter()
            timelist2.append(t1_stop-t1_start)
	
	print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)
	print(timelist)#!/usr/bin/env python3
	plt.plot(vector,timelist)
	plt.show()
	plt.savefig('plotesting..png')
	print(timeFibC)
	plt.plot(vector,timeFibC)
	plt.savefig('testingfib.png')
	
	plt.plot(vector,timelist2)
	plt.show()
	plt.savefig('testingpyb.png')


