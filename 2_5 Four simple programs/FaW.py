user_in0 = input("Enter word to search:").lower()
user_in1 = input("Enter string to search through:").lower()

found = True
for char0 in user_in0:
    if char0 not in user_in1:
        found = False

if found:
    print("Yes")
else:
    print("No")