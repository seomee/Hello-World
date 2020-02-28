#Fibonacci numbers module

def fib(n) :
	a, b = 0, 1
	while a < n :
		print(a, end=' ')
		a, b = b, a+b
	print()

def fib2(n) :
	result = []
	a, b = 0, 1
	while a < n :
		result.append(a)
		a, b = b, a+b
	return result

if __name__ == "__main__" :
	print("fibo module loaded as script")
	import sys
	fib(int(sys.argv[1]))

else :
	print("fibo module loaded as module")
