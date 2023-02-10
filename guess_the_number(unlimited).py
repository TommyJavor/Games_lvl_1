#guess the number 
def total_foolproof(num):
  if num.isdigit() == False: #проверка на число
      return False
  if 1 <= int(num) <= right:    
    return True
  else:
  	return False	

def the_game():
	import random 

	counter = 1

	num = random.randint(1, right)

	n = input('enter the number: ')
	print()
	while total_foolproof(n) == False:
		print('nope, another one')
		print()
		n = input('enter the number: ')
		print()

	n = int(n)

	while n != num:
		if n < num:
			print('мало, надо больше')
			counter += 1
		elif n > num:
			print('не, чет перебрали, меньше')
			counter += 1
		n = int(input('enter another one: '))
		print()

	if n == num:
		print('bingo!')
		print('количество попыток:', counter)
		print()


while True:
	print('wanna play? (yes/no)')
	ans = input()

	if ans == 'yes':
		print('nice:)')
		right = int(input('enter the right border: '))
		the_game()
	elif ans == 'no':
		print('ok:(')
		break
	else:
		print('fuck you, too!')
		break


