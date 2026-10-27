user_in = "".join(input("Enter string to check for palindrome:").lower().split())
if user_in == user_in[::-1] and user_in:
    print("It's a palindrome")
else:
    print("It's not a palindrome")