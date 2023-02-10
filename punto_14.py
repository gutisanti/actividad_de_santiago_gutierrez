def mean(numbers):
    return sum(numbers) / len(numbers)

numbers = [int(x) for x in input("Enter a list of numbers, separated by space: ").split()]
result = mean(numbers)
print("The mean of", numbers, "is", result)
