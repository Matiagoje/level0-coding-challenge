def fahrenheit_to_celsius(fahrenheit_input):
    celsius = (fahrenheit_input - 32)* (5/9)
    celsius = int(celsius)
    print("celsius = ", celsius)

fahrenheit_to_celsius(86)

def celsius_to_fahrenheit(celsius_input):
    fahrenheit = (celsius_input * 1.8) + 32
    fahrenheit = int(fahrenheit)
    print("fahrenheit = ", fahrenheit)

celsius_to_fahrenheit(35)