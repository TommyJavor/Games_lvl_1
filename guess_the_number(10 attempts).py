#guess the number (just 10 attempts)
import random, time
def total_foolproof(num):
  if num.isdigit() == False: #проверка на число
      return False
  if 1 <= int(num) <= 100:    #не проходит тест с большим числом 
    return True
  else:
  	return False			#новая строчка, проверить

def the_game():
	n = input('enter the number: ')
	
	while total_foolproof(n) == False:
		print('пошел ты нахер, козёл')														#добавить переменную для правой границы 
		n = input('enter correct number (in range 1 to 100): ')
		print()
	n = int(n)

	num = random.randint(1, 100)
	
	for i in range(9, 0, -1):
		if num > n:
			print('nope, more')
			print('you have', i, 'attempts left')
			n = input('enter another one: ')
			while total_foolproof(n) == False:											
				print('пошел ты нахер, козёл')
				n = input('enter correct number (in range 1 to 100): ')
			n = int(n)
			print()
		elif num < n:
			print('nope, less')
			print('you have', i, 'attempts left')
			n = input('enter another one: ')
			while total_foolproof(n) == False:
				print('пошел ты нахер, козёл')
				n = input('enter correct number (in range 1 to 100): ')
			n = int(n)
			print()
		elif num == n:
			print('krasavchik')
			break

	if num != n:
		print('next time, pal')

while True:									#основная программа 
	print('wanna play?')
	print('(yes/no)')
	ans = input().lower()						
  
	if ans == 'no':
		print('think again')
		for i in range(10, -1, -1):
			print(i)
			time.sleep(1)
	elif ans == 'yes':
		print('good choice')
		print(the_game())
	elif ans == 'stop it':
		print('as you wish:(')
		break
	else:
		print('what did you say about my mom?!')
		print()
    
    
    