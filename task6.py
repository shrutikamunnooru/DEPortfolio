
'''
Write a Python function to check if a given number is prime. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself.

'''
def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
            
num = int(input("Please enter a number to check if it's prime"))
if prime(num):
    print(f'The {num} is prime')
else:
    print(f'The {num} is not prime')