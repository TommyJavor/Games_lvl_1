def play():
	import random
	list_of_options = ['камень', 'ножницы', 'бумага'] #список, из которого будет выбор
	counter_move = 0
	counter_a = 0
	a = input('your move: ')
	move = random.choice(list_of_options)  # компуктер выбрасывает камень/ножницы/бумагу

	while True:
		if move == a:
			print('ничья')
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'камень' and a == 'ножницы':
			print(move, 'win')
			counter_move += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'камень' and a == 'бумага':
			print(a, 'win')
			counter_a += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'ножницы' and a == 'камень':
			print(a, 'win')
			counter_a += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'ножницы' and a == 'бумага':
			print(move, 'win')
			counter_move += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'бумага' and a == 'камень':
			print(move, 'win')
			counter_move += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif move == 'бумага' and a == 'ножницы':
			print(a, 'win')
			counter_a += 1
			print('игрок:', counter_a, 'мегамозг:', counter_move)
			print()
		elif a == 'стоп':
			print('пока:)')
			break
		a = input('next move: ')
		move = random.choice(list_of_options)


while True:
	print('wanna play? (yes/no)')
	ans = input()
	if ans == 'yes':
		print('cool:)')
		play()
	elif ans == 'no':
		print('ok:(')
		break
	else:
		print('fuck you, too')
		break
		

