def generate_even_numbers():
    return [x for x in range(2, 101, 2)]

even_numbers = generate_even_numbers()
print("The list of even numbers:", even_numbers)
