import random
import time
ask = input('Are you want to join this math quiz? >> ')

while ask == 'yes':
    print("Welcome! This math quiz consists of 10 questions,")
    print("and you must complete all 10 questions to escape from here.")
    time.sleep(3)

    for i in range(11):
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)

        quiz = int(input('{} + {} = ? >> '.format(a, b)))
        c = a + b

        if quiz == c:
            print('Good job! You got it right.')
            time.sleep(1)
        else:
            print('Wrong answer! The correct answer is {}.'.format(c))
            time.sleep(1)
    print("Yes... This was the math quiz.")

print("Alright, goodbye.")
quit()