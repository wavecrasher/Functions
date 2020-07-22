# FUNCTIONS - a block instructions to do an action. They're used to organize code. 

# 2 things required to do: 
# 1) define the function
# 2) call the function 

#define a function
#def greeting():
 # print("Hello!")

#call function
#greeting() 

#function with a parameter, a parameter is a value to plug into a function, for the function to use in creating a output
#def greeting(name):
 # print("Hello, " + name)

#guestname = input("What is your name: ")

#greeting(guestname)

def addNumbers(num1, num2):
  print(num1 + num2)

def subNumbers(num1, num2):
  print(num1 - num2)

#Ask user to enter two numbers. Plug these two  numbers into the addNumbers function 

num1 = int(input("enter number 1: "))
num2 = int(input("enter number2: "))
operator = input("add or subtract: ")



if operator.lower == "add": 
  addNumbers(num1, num2)
elif operator.lower() == "subtract": 
  subNumbers(num1, num2)
else:
  print("that's not an operator")