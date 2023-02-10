def is_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
result = is_palindrome(string)
if result:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
