# Lab 4  by Professor Sundararajan
# Implemented by <Alexandra Burke>

def sumOfNumbers():
    userInput = float(input("Enter a number --> "))
    sumNum = 0
    
    while userInput >= 0 :
        sumNum = userInput + sumNum
        userInput = float(input("Enter a number --> "))
    
    print("The sum of all the numbers that you entered is --> ", sumNum)
    
    
def caloriesBurned():
    caloriesPerMinute = 4.2
    
    for numMinutes in range (10, 31, 5):
        numCalories = numMinutes * caloriesPerMinute
        
        print('you burned ',numCalories, 'in ', numMinutes)    
    
def main():
    sumOfNumbers()
    caloriesBurned()
        
main()