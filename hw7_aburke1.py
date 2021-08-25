# Lab 7 
# Alexandra Burke

# add a thing to do item to text file & print list
# while loop so user can add 1 or more or print list
# if user selects 1 open file in append mode
# ask user to enter a "things to do" and append item to end of file and close
# if user selects 2 open txt and read, use for loop to print the items in list the close
# put file-open code in one function and print list in another
# main() manage while loop and menu sections and call functions
# close file after adding an item and printing list

def main():
    
    outfile = open('todoList.txt', 'w+')

def addItem():
 
    outfile = open(mode = 'a')
    todoList = str(input("Thing to do: "))
    outfile.write(line)
    outfile.close()
    
def printList():
    
    outfile = open(mode = 'r')
    todo_list = outfile.readlines()
    for item in todo_list:
        print(item, end = '')
    outfile.close()
    
def openFile(mode):
    
    try:
        outfile = open("./todoList.txt", mode)
    except IOError:
        print("Exiting.")
        exit(1)
    return outfile

def closeFile(outfile):
    outfile.close()
    
def invalid():
    print("Error. Enter something valid.")
    print()

main()
    