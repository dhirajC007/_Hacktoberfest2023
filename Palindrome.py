def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if the string is equal to its reverse

# Input: Enter a string to check for palindrome
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
