# Alexandra Burke
# Professor Sundararajan 

# write a program that reads a files contents to find:
# the number of lines in a file
# the number of words in the file
# use split() command to split words in each line into list 
# strip all the punctuation letters at the end of the words using strip() 
# create a list of unique words in the file and print list
# print number of unique words 
import random

def main():
    
    outfile = __import__('stEds.txt')

try:
    f = open('stEd.txt', 'r')
    line_count = 0
    character_count = 0
    word_count = 0
    
    for i in f:
        line_count += 1
        word_count = word_count + len(i.split())
        
        for j in i.split():
            character_count = character_count + len(j)

    print('Number of characters:', character_count)
    print('Number of lines:', line_count)
    print('Number of words:', word_count)
    
    outfile.close()

main()