''' 
Write a Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin.
The program should ask the user to enter a temperature and the unit (C, F, K), then convert the 
temperature to the other two units and display the results.

Concepts Covered: Variables, Data Types, Basic Operations
'''


def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

def celsius_to_kelvin(C):
    return C + 273.15

def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9

def fahrenheit_to_kelvin(F):
    return (F - 32) * 5/9 + 273.15

def kelvin_to_celsius(K):
    return K - 273.15

def kelvin_to_fahrenheit(K):
    return (K - 273.15) * 9/5 + 32

    
temp = float(input("Please enter a temperature : "))
unit = input("Please enter a unit either in C or F or K : ").upper()

if unit == 'C':
    fahrenheit = celsius_to_fahrenheit(temp)
    kelvin = celsius_to_kelvin(temp)
    print(f'The converted temperature is {fahrenheit} F and {kelvin} K')
    
if unit == 'F':
    celsius = fahrenheit_to_celsius(temp)
    kelvin = fahrenheit_to_kelvin(temp)
    print(f'The converted temperature is {fahrenheit} F and {kelvin} K')
    
if unit == 'K':
    celsius = kelvin_to_celsius(temp)
    fahrenheit = kelvin_to_fahrenheit(temp)
    print(f'The converted temperature is {fahrenheit} F and {kelvin} K')
    
