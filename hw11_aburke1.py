# Alexandra Burke
# Homework 11 

class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name 
        self.__address = address
        self.__phone = phone_num
        
    def set_name(self, name):
        self.__name = name 
        
    def set_address(self, address):
        self.__address = address 
        
    def set_phone_num(self, phone_num):
        self.__phone = phone_num 
        
    def get_name(self):
        return self.__phone 
    
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone
    
class Customer(Person):
    def __int__(self, name, address, phone_num, customer_num, mail_list):
        self.__customer = customer_num
        self.__mail = mail_list
        Person.__init__(self, name, address, phone_num)
        
    def set_customer_number(self, mail_list):
        self.__mail = mail_list
            
    def get_mail_status(self):
        return self.__mail
    
    def __str__(self):
        if self.__mail == True: 
            choice = 'yes'
        else:
            choice = 'no'
        return 'Name: ' + self.__Person__name + \
                '\nAddress: ' + self.__Person__address + \
                '\nPhone number: ' + self.__Person__phone_ + \
                '\nCustomer number: ' + str(self.__customer_num) + \
                '\nMail list: ' + choice 

def main():
    
    alex = Customer('Alexandra Burke', 'South Park Meadows', '6199902988', '222', True)
    print(alex)
        
main()    
                