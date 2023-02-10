# -*- coding: utf-8 -*-
def the_game():
    import random
    answers = ["100проц", "абсолютно да", "будь уверен", "определенно", "точно так", "вообще хз, но вероятно", "скорее да", "вероятность высока", "шансы есть", "звезды благосклонны", "а вот хз", "не ебу", "понятия не имею", "программа закрыта на перерыв", "давай потом", "хуйня идея", "не ешь, подумой", "она тебя сожрет", "нет.", "нахуй надо"]

    print('чо?')
    question = input()
    answer = random.choice(answers)
    print(answer)

while True:
    print('wanna play? (yes/no)')
    ans = input()
    print()
    if ans == 'yes':
        print('here you go')
        the_game()
        print()
    elif ans == 'no':
        print('ok:(')
        break
    else:
        print('fuck you, too')
        break


