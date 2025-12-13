import time

class MyCalc:
    def __init__(self):
        pass
    
    def calculate(self, op, n):         # Perform the calculation based on operation and numbers
        try:
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
                for i in n[1:]:
                    if i == 0:
                        return 'you cannot divide by zero. Try again.'
                    ans = ans / i
            else:
                return 'Invalid operation'
            return ans
        except Exception as e:
            return f'Error: {str(e)}'
    
    def run(self): # run the calculator
        print('Welcome to my calculator!')
        print('This calculator was made with class in Python.')
        time.sleep(2)
        
        while True:
            op = input('Enter the operations you need (+, -, *, /) ')
            n = list(map(int, input('Put the numbers to calculate! (divide w/ space) ').split()))
            
            res = self.calculate(op, n)
            print("The result: {}".format(res))
            ask = input('Wanna calculate more? (y/n) ')
            if ask == 'y':
                continue
            else:
                print('There you go, thanks for using our program.')
                quit()

if __name__ == '__main__':
    calc = MyCalc()
    calc.run()