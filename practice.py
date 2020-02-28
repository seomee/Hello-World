

num = 1


def mult(num) :
	for i in range (1, 10) :
		print( num, "  * ", i , " = ", num * i)



def fib(n) :
	"""Print a Fibonacci series up to n.
	"""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()




print ("============ fib ============")
fib(2000)

from collections import deque

queue = deque(["eric", "john", "michel"])
queue.append("terry")
queue.append("graham")

queue.popleft()
queue.popleft()

for ele in queue :
	print(ele, end=" ")
