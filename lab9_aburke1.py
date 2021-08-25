# ALexandra Burke
# Lab 9 - Professor Sundararajan

#  create phone book dictionary for key value pairs
#  key method-->print all names  
#  value method-->print all phone numbers 
#  add jake to book with number and remove jill
#  print each element using items method and for loop
#  write code to get user input for name 
#  write exception code “ERROR: The given name, <name>, does not exist in the phonebook”
#  for listOp() create list of 5 numbers given by user
#  for loop, after added to list then print 
#  print total sum of all elements, print average of elements average = sum/lengthOfElements
#  reverse list and print, print largest and smallest values, sort and print again

def main():
    phoneBook()
    listOperations()

def phoneBook():
    phBook = {'John': '938477566', 'Jack': '938377264', 'Jill': '947662781'}
    print("The names in the phone book are ", phBook.keys())

    phBook['Jake'] = '938273443'
    phBook.pop('Jill')

    for k, v in phBook.items():
        print("The phone number of", k, "is", v)

    userInput = input("Name of the user you want to look up: ")

    if userInput not in phBook.keys():
        print("ERROR: The given name,", userInput, ", does not exist in the phonebook")
    else:
        print(phBook[userInput])

def listOperations():
    nums = []

    for i in range(5):
        num = int(input("Enter a number: "))
        nums.append(num)
        print(nums)

    print("Total sum of elements: ", sum(nums))
    print("Average of elements: ", sum(nums) / len(nums))
    print("Elements reversed: ", nums[::-1])
    print("Largest element: ", max(nums))
    print("Smallest element: ", min(nums))
    nums.sort()
    print("Sorted elements: ", nums)

main()