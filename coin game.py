def play():
	import random 

	num = random.randint(0, 1)
	if num == 1:
		print('орёл')
	else:
		print('решка')

print('hi, your answer is: ')
play()
print()
ans = input("flip a coin again? ")

while True:
	if ans == 'yes':
		play()
		print()
		ans = input("flip a coin again? ")
	elif ans == 'no':
		print('ok:(')
		break
	else:
		print('see you soon')
		break
