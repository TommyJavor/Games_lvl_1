import random 

word_list = ['кошка', 'собака', 'кролик', 'корова', 'курица', 'карась', 'свинья', 'овца', 'баран', 'лось']  # дополнить список

def get_word():
	step = random.choice(word_list).upper()
	return step

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
	guessed_letters = []
	guessed = False
	tries = 6
	word_complition = list(len(word) * '_')
	print('поиграем!')
	print('попыток осталось =', tries)
	print(display_hangman(tries))			# распечатать состояние человечка
	print(*word_complition)	# распечатать _ по количеству букв
	
	while tries != 0:
		user_guess = input('введите букву: ').upper()			# проверка на букву
		while user_guess.isalpha() == False or len(user_guess) > 1:
			print('что-то не так')
			user_guess = input('введите одну букву: ').upper()

		if user_guess.rstrip() in guessed_letters:		# getting rid of doubles
			print('эта буква уже была')
			continue

		if user_guess.rstrip() in word:
			guessed_letters.append(user_guess)
			for i in range(len(word)):
				if word[i] == user_guess:		# замена _ буквами (не смог проверить)
					word_complition[i] = user_guess
					print('попыток осталось =', tries)
					print(display_hangman(tries))
					print(*word_complition)
		else:
			guessed_letters.append(user_guess)
			tries -= 1
			print('попыток осталось =', tries)
			print(display_hangman(tries))		# reduccing the amount of tries
			print(*word_complition)

		if word == ''.join(word_complition):			# cheсk if you've guessed
			print('you win!')
			return word

	if word != ''.join(word_complition):
		print('next time')						# if you didn't guess
		print('the word was: ')
		return word


print(play(get_word()))
