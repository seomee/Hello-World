

while True :
	try :
		x = int(input("Input Number : "))
		break
	except ValueError :
		print("It's not a number\n")
	except (RuntimeError, TypeError, NameError) :
		pass


class B(Exception) :
	print("Called B")
	pass

class C(B) :
	print("Called C")
	pass

class D(C) :
	print("Called D")
	pass


for cls in [B, C, D] :
	try :
		raise cls()
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")

import sys

try : 
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err :
	print("OS Error {0}".format(err))
except ValueError :
	print("Cound not convert data to an integer.")
except :
	print("Unexpected error :", sys.exc_info()[0])
	raise


