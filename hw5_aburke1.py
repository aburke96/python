# Homework 4  by Professor Sundararajan
# Implemented by <Alexandra Burke>

def dog():
    retValue = 'Bark'
    return retValue
    
def cat():
    retValue = 'Meow'
    return retValue
    
def lion():
    retValue = 'Roar'
    return retValue
    
def sheep(): 
    retValue = 'Baah'
    return retValue

def getUserInput():
    userInput = int(input("Select a number 1-5. 1-4 makes an animal sounds and 5 ends the program: "))
    

def main():
    
    userInput = getUserInput()
    while userInput !=5:
        if userInput == 1:
            return dog()
            userInput = int(input("Select a number 1-5. 1-4 makes an animal sounds and 5 ends the program: "))
        elif userInput == 2:
            return cat()
            userInput = int(input("Select a number 1-5. 1-4 makes an animal sounds and 5 ends the program: "))
        elif userInput == 3:
            return lion()
            userInput = int(input("Select a number 1-5. 1-4 makes an animal sounds and 5 ends the program: "))
        elif userInput == 4:
            return sheep()
            userInput = int(input("Select a number 1-5. 1-4 makes an animal sounds and 5 ends the program: "))
        else:
            return getUserInput()

main()
        
        
    
