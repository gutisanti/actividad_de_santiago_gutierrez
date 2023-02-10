def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("The temperature in Celsius is:", celsius)
