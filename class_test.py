

class MyClass:
	"""A simple example calss """

	i = 12345

	def __init__(self, real, image):
		print("called 2")
		self.r = real
		self.i = image





	def f(self, num):
		self.i = num
		print("i :", self.i)

	def pf(self):
		print("i :", self.i)
		

cls = MyClass(1, 2)


cls.f(10)
cls.pf()

xf = cls.f(8)
xpf = cls.pf

#xf(11)
xpf()

cls.f(10)
xpf()




