# Homework 4  by Professor Sundararajan
# Implemented by <Alexandra Burke>

def budgetAnalysis():
    
    budget = int(input("Enter the budget amount of expenses for the month: "))
    x = input("Do you have any expenses for the month?")
    
    total = 0
    
    while x == 'yes':
        expenses = int(input("Enter the expense amount: "))
        x = input("Are there more expenses?")
        total += expenses
    
    print("The total amount spent: ", total)
    
    under = budget - total
    over = total - budget
    
    if total<budget:
        print("You are underbudget by ", under, "dollars.")
    else:
        print("You are overbudget ", over, "dollars.")

def celciusToFahrenheit():
    
    c = int(input("What is the beginning Celsius temperature? --> "))
    d = int(input("What is the ending Celsius temperature? --> "))
    print ("Celsius       Farenheit")

    
    for temp in range (c, d):
        f = 9 /5 * temp + 32
        print (temp, f)
        c += 1
    
def main():
    budgetAnalysis()
    celciusToFahrenheit()
    
main()