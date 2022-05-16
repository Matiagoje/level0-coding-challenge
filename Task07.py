num = 32                #constant used for convertion

def fahrenheit_to_celcius(fahrenheit_input):
    celsius = (fahrenheit_input - num)* (5/9)
    celsius = int(celsius)
    print("celsius = ", celsius)

fahrenheit_to_celcius(86)

def celcius_to_fahrenheit(celsius_input):
    fahrenheit = (celsius_input * 1.8) + num
    fahrenheit = int(fahrenheit)
    print("fahrenheit = ", fahrenheit)

celcius_to_fahrenheit(32)