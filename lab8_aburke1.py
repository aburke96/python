# Lab 8
# Alexandra Burke

# reads stuff of two files in separate lists
# user should enter boys name, girls name, or both, and app will display
# messages indicating whether the name were among most popular
# GirlNames.txt -- contains list of 200 most popular names given to girls
# BoysNames.txt -- contains list of 200 most popular names given to boys 
# all born in US from 2000 through 2009

def main():
    
    girlNames = []
    boyNames = []
    
    list1 = open('GirlNames.txt', 'r')

    for eachLine in list1:
        eachLine = eachLine.strip('\n')
        girlNames.append(eachLine)
    list1.close()
    print(girlNames)
    
    list2 = open('BoyNames.txt', 'r')
    
    for eachLine in list2:
        eachLine = eachLine.strip('\n')
        boyNames.append(eachLine)
    list2.close()
    print(boyNames)
    
    userInput = (input('Enter a name: ')
    
    if userInput in girlNames:
        print('This is one of the popular girl names.')
    
    if userInput in boyNames:
        print('This is one of the popular boy names.')
    else:
        print('This name is uncommon.')
    
main()