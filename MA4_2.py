#!/usr/bin/env python3

from person import Person
from random import random
def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == '__main__':
	main()



