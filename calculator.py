import os
 

import art_calculator
#functions in calculator 

def add(first, second):
    if first=="" or second=="":
        return 
    return first+second

def substract(first,second):
    return first-second

def multiply(first,second):
    return first*second

def division(first,second):
    return first/second

#functions dectionary
function_dictonary = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':division
}
def calculator():
    print(art_calculator.logo)    
    num1=float(input('Enter the first number : '))
    
    for symbol in function_dictonary:
        print(symbol)
    run =True
    
    while run:
            
        opration_symbol = input('Pick an operation symbol from the line above : ')
        
        num2=float(input('Enter the next number : '))
       
        for symbol in function_dictonary:
            if opration_symbol ==symbol:
                first_opration = function_dictonary[symbol]
                answer= first_opration(num1,num2)
     
        print(f"{num1} {opration_symbol} {num2} = {answer}\n\n")
        ask_user = input(f"Do You want to continue calculation with {answer} type 'y' if Yes otherwise 'n' for NO To start new calculation : " )
        if ask_user=='y' or ask_user=='Y':
            num1 = answer
        else :
            run =False
            #Clearing the Screen
            os.system('cls')
            calculator()

calculator()