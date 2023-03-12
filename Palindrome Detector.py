def is_palindrome(s):
    # Remove all spaces and punctuation
    s = ''.join(c for c in s if c.isalnum())
    # Convert to lowercase
    s = s.lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
