'''
Write a Python function that generates the first n Fibonacci numbers. The function should return the numbers as a list.
'''

def fibonacci(n):
    a,b = 0,1
    while a < n:
        print(a, end = ' ')
        a,b = b, a + b

value = int(input("Please enter a number "))
output = fibonacci(value)
print(f'The fibonacci of {value} is {output}')
