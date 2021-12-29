print("\033c", end="")

value = input("Please enter your name:\n") #for asking the name 
 
print(f'Hello! {value}')  #it show the user name for the user

print ("this script can work addition , subtraction, multiplication and division use it please") #this is like intoduction
print("ok lets start")  #the program is start 
value1 = input("write your first number:\n")  #this one ask the first number
value2 = input("write your second number:\n")  #and this one ask the second number

v1 = int(value1) #this is show the first number
v2 = int(value2) #this is show the scond number

choice = input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for Multiplication.\nEnter 4 for division.\n")   #this is for chooseing
choice = int(choice)  #then you choose it 

if choice == 1:
    print(f'You entered {v1} and {v2} and their addition is {v1 + v2}' )  #when you choose the first one the script will be add your two numbers
elif choice == 2:
    print(f'You entered {v1} and {v2} and their subtraction is {v1 - v2 }' ) #when you choose the second one the script will be  subtract your two numbers
elif choice == 3:
    print(f'You entered {v1} and {v2} and their multiplication is {v1 * v2}' ) #when you choose the third one the script will be multiple your two numbers
elif choice ==4:
    print(f'You entered {v1} and {v2} and their division is {v1/v2}') #when we choose the fourth one the script will be divided your two numbers
else:
    print("wrong choice, terminating the program..........")  #when you enter another number like 5, 6, 7, 8, 9, ....  the script will bes quite the work 

print("thanks for using our script")   #this is for thanking the user of the script
print("from the unknown group")
print("c_h4ck3r") #the script owner


# so yezarew temro yehan yemsel nber guysoch