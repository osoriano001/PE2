user_in = input("Enter DoB digits:")

while len(user_in) > 1:
    dol = 0
    for digit in user_in:
        dol += int(digit)
    user_in = str(dol)
print(user_in)