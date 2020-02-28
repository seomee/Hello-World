

class Dog :

	kind = 'canine'
	#tricks = []

	def __init__(self, name) :
		self.name = name
		self.tricks = []

	def add_trick(self, trick):
		self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('paly dead')

print("d :", d.tricks)
print("e :", e.tricks)

#e.add_trick = 1
#print(e.add_trick)
e.add_trick('산책')
print(e.tricks)