import time

def MyCalc(op, n): # the argument n i make it as list parameter.
    if op == '+':
        ans = 0
        for i in n:
            ans += i
    elif op == '-':
        ans = 0
        for i in n:
            ans -= i
    elif op == '*':
        ans = 1
        for i in n:
            ans *= i
    elif op == '/':
        ans = n[0]
        for i in n:
            ans = ans / i
            if ZeroDivisionError:
                return 'you cannot divide by zero. Try again.'
        return ans

print('Welcome to my calculator!')
print('This calculator was made with function in Python.')
time.sleep(2)

while True:
    op = input('which operation you need in this calculator? (+, -, *, /) ')
    n = list(map(int, input('Put the numbers! (divide it with space) ').split()))

    res = MyCalc(op, n)
    print("The answer: {}".format(res))
    ask = input('Wanna calculate more? (y/n) ')
    if ask == 'y':
        continue
    else:
        print('There you go, thanks for use our program.')
        quit()
