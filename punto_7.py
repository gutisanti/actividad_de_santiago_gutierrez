numbers = [1, 2, 3, 4, 5]

def find_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = find_min_max(numbers)
print("The smallest number in the list is:", minimum)
print("The largest number in the list is:", maximum)
