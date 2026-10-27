user_in0 = input("Enter first string:").lower()
user_in1 = input("Enter second string:").lower()

for char0 in user_in0:
    user_in1 = user_in1.replace(char0, "", 1)

if not len(user_in1):
    print("Anagrams")
else:
    print("Not anagrams")