def fahrenheit_to_celsius(fahrenheit_input):
    celsius = (fahrenheit_input - 32)* (5/9)
    celsius = int(celsius)
    return celsius

fahrenheit_to_celsius(86)

def celsius_to_fahrenheit(celsius_input):
    fahrenheit = (celsius_input * 1.8) + 32
    fahrenheit = int(fahrenheit)
    return fahrenheit

print("Celsius = ", fahrenheit_to_celsius(86))
print("Fahrenheit = ", celsius_to_fahrenheit(35))
