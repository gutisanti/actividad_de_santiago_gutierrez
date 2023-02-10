import numpy as np

def generate_array(size):
    return np.arange(size)

size = int(input("Enter the size of the array: "))
numbers = generate_array(size)
print("The generated array:", numbers)
