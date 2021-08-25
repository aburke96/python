#Lab 7
#Alexandra Burke

import random

def main():

    outfile = open('random_file.txt', 'w')

    try:
        for i in range(20):
            line = str(random.randint(1,100))
            outfile.write(line)
            print(line)
    #error handling 
    except ValueError:
        print('ERROR: Give only valid numbers')
        
        outfile.close()
        
        outfile = open('random_file.txt', 'r')
        print(outfile.read())
        outfile.close()
        
    outfile = open('random_file.txt', 'r')
    x = outfile.readlines()
    
    total = 0
    count = i
    
    for count in range(20): 
        
        rand = random.randrange(1,100)
        total = total + rand 
        average = total / 20
        count = count + 1
        
    print('the total of the numbers is: ', total)
    print('the average is: ', average)
    print('the number of random numbers read from file: ', count)
    
    outfile.close()

main()