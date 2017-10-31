from random import *
def guessing_game():
    print('GUESSING NUMBER')
    print('A number between 1-100 was generated. Try your best to guess it! Start now!')
    a = randint(1,100)
    guess = int(input('input your guess:'))
    n = 0
    while guess != a:
        n += 1
        if n < 7:
            if guess > a:
                print('Sorry, but that\'s too big.')
            elif guess < a:
                print('Sorry, but that\'s too small.')
            guess = int(input('guess again: '))
        elif n >=7:
            print('Can I call you stupid? You\'ve run out of your chance! GAME OVER!')
            return
    if guess == a:
        print('CONGRATULATIONS!')
        return

guessing_game()