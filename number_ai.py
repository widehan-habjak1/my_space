import time
import random

com = random.randint(1, 20)
askCom = None
m = 0


print('**Guess number between 1 ~ 20**')
while askCom != com:
    askCom = int(input('Guess the number: '))
    if askCom < 1 or askCom > 20:
        print('Input out of range! Exiting the program.')
        break
    elif askCom > com:
        print('nope, lower')
        m += 1
        continue
    elif askCom < com:
        print('nope, upper')
        m += 1
        continue
    else:
        print('You finally guessed!')
        break
print('You had attempted {} time(s) for this.'.format(m + 1))