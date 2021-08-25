# Lab 6 
# Implemented by <Alexandra Burke>

def main():
    
    number = int(input('Enter an integer: '))
    fact = factorial(number)
    
    print('The factorial of ', number, 'is ', fact)

def factorial(n):
    if n == 0: 
        return 1
    if n < 0:
        print("Error. Select a positive value.")
    else:
        return n * factorial(n - 1)
   
main()