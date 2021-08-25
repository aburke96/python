# Lab 5  by Professor Sundararajan
# Implemented by <Alexandra Burke>

def calc_average(test1, test2, test3, test4, test5):
    
    average = (test1 + test2 + test3 + test4 + test5) / 5
    return average

def determine_grade(grade):
    
    #if to establish letter grades for each test score
    if (grade >= 90) and (grade <= 100):
        return 'A'
    elif (grade >= 80) and (grade <= 89):
        return 'B'
    elif (grade >= 70) and (grade <= 79):
        return 'C'
    elif (grade >= 60) and (grade <= 69):
        return 'D'
    else:
        return 'F'

def main():
    
    #ask user to input 5 test scores to find the total/5 = average 
    test1 = int(input('Enter the test score 1: '))
    test2 = int(input('Enter the test score 2: '))
    test3 = int(input('Enter the test score 3: '))
    test4 = int(input('Enter the test score 4: '))
    test5 = int(input('Enter the test score 5: '))
    retValue = calc_average(test1, test2, test3, test4, test5)
    print("Your average test score is ", retValue)
    grade = determine_grade(retValue)
    print("The grade is ", grade)
    
main()
