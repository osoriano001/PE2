text = input("Enter your message: ")
shift = int(input("Enter shift value: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    else:
        code = (ord(char) + shift)
        if char.isupper():
            z_ord = ord('Z')
            a_ord = ord('A') - 1
        else:
            z_ord = ord('z')
            a_ord = ord('a') - 1
        if code > z_ord:
            code = (code % z_ord) + a_ord
        cipher += chr(code)
    # ((char + shift) % Z) + A
    # if code > ord('Z'):
        # code = ord('A')
    # cipher += chr(code)
print(cipher)