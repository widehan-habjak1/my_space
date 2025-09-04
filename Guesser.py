import random
import time

def NumberGuesser(com):
    print('\n--Number Guesser--')
    m = 0
    guess = None
    while True:
        guess = int(input('Guess the number: '))
        if guess < 1 or guess > 20:
            print('Input out of range! Exiting the program.')
            break
        elif guess > com:
            print('nope, lower')
            m += 1
            continue
        elif guess < com:
            print('nope, upper')
            m += 1
            continue
        else:
            print('You finally guessed!')
            print('You attempted {} time(s) to guess the number!!'.format(m))
            break

guessnum = random.randint(1, 20)
print('Computer gives you a number: {}'.format(guessnum - random.randint(1, 7)))
print('It seems like a gift... but be careful, it may a trap!')
time.sleep(2)

NumberGuesser(guessnum)
