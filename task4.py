'''
Create a Python program that functions as a basic calculator. It should support addition, subtraction, multiplication, 
and division. The user provides two numbers and an operator,and the program performs the corresponding operation.
'''



def calculator(num1,num2, operation):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1/num2
        
num1 = int(input("Please enter first number : "))
num2 = int(input("Please enter second number : "))
operation = input("Please enter the operation you would like to perform : ")
output = calculator(num1, num2, operation)

print(f'The result of {num1} {operation} {num2} is {output}')
    
    

    
