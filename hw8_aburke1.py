# Homework 8
# Alexandra Burke

# create list of 20 random numbers between 1-100
# ask user to enter num and gives values 1-100 for 'n'
# call largerThan_n function and pass two values 
# print and return list and then return and print 
# print max and min values

import random

def largerThan_n(list, n):
    
    result_list = []
    
    for i in list:
        if i>n:
            result_list.append(i)
    return result_list

def main():
    
    list = []

    for i in range(20):
         list.append(random.randint(1,100))
         
    print('Enter a number between 1-100: ')
    n = int(input())

    while n<=1 or n>=100:
        print('Invalid number try again: ')
        n = int(input())

    the_list = largerThan_n(list, n)
    print("The List is: ")
    print(the_list)

    print('Reverse of the List is: ')
    the_list.reverse()
    print(the_list)

    print('Sorted List is: ')
    the_list.sort()
    print(the_list)

    print('Max value in the list is: ')
    print(max(the_list))
    print('Min value in the list is: ')
    print(min(the_list))


main()