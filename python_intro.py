
#Author : seomee
#2019.9.27

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


def hi(name) :
	print('How are you? ' + name)



girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls :
	hi(name)
	print('Next girl')



for i in range(1,6):
	print(i)
	



