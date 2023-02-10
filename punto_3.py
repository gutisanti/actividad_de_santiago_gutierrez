import random

def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

count = int(input("How many random numbers would you like to generate? "))
lower_bound = int(input("What is the lower bound for the range of numbers? "))
upper_bound = int(input("What is the upper bound for the range of numbers? "))

random_numbers = generate_random_numbers(count, lower_bound, upper_bound)
print("Random numbers:", random_numbers)