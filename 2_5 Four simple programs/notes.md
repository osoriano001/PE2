# Ceasar cipher: encrypting a message
Rules: 
-   increment each letter. *A->B, B->C,...Z->A*
-   latin letters only (no whitespace or digits)
-   all letters are capital
```python
# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
```


# Caesar cipher: decrypting a message
Same as above, but decrement each letter

```python
# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
```

# The numbers processor
<code>int</code> or <code>float</code> are not inherently suitable with <code>input()</code>

```python
# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
```

# The IBAN validator
An IBAN-compliant account number consists of:
-   a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for - France, GB for Great Britain, DE for Germany, and so on)
-   two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
-   the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)

The standard says that validation requires the following steps (according to Wikipedia):
-   (step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
-   (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
-   (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
-   (step 4) Interpret the string as a decimal integer and compute the remainder of that number by modulo-dividing it by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.

```python
# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
```
Output
```cmd
Enter IBAN, please: GB72 HBZU 7006 7212 1253 00
IBAN entered is valid.
```

# Summary
-   a number of fuzzy string comparison algorithms has been created and implemented. These algorithms are able to find strings which aren't equal in the Python sense, but are similar. (hamming distance, levenshtein distance)
-   another way; acoustic similarity, which means a process leading to determine if two strings sound similar (like "raise" and "race") (soundex)
-    Due to limited native float and integer data precision, it's sometimes reasonable to store and process huge numeric values as strings. This is the technique Python uses when you force it to operate on an integer number consisting of a very large number of digits.

# LABs

## improving caesar cipher
### TODO: 
-   asks the user for one line of text to encrypt;
-   asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
-   prints out the encoded text.

Sample input
```cmd
abcxyzABCxyz 123
2
The die is cast
25
```
Outputs
```cmd
cdezabCDEzab 123
Sgd chd hr bzrs
```

## palindromes
### TODO: 
-   asks the user for some text;
-   checks whether the entered text is a palindrome, and prints the result.

Note:
-   assume that an empty string isn't a palindrome;
-   treat upper- and lower-case letters as equal;
-   spaces are not taken into account during the check – treat them as non-existent;
-   there are more than a few correct solutions – try to find more than one.

Sample input
```cmd
Ten animals I slam in a net
Eleven animals I slam in a net
```
Output
```cmd
It's a palindrome
It's not a palindrome
```

## anagrams
### TODO: 
-   asks the user for two separate texts;
-   checks whether, the entered texts are anagrams and prints the result.

Note:
-   assume that two empty strings are not anagrams;
-   treat upper- and lower-case letters as equal;
-   spaces are not taken into account during the check – treat them as non-existent

Sample input
```cmd
Listen
Silent
modern
norman
```
Output
```cmd
Anagrams
Not anagrams
```

## the digit of life
### TODO: 
-   asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
-   outputs the Digit of Life for the date.

Sample input
```cmd
19991229
20000101
```
Output
```cmd
6
4
```

## find a word!
### TODO: 
We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
Are the characters comprising the first string hidden inside the second string?
For example:
-   if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
-   if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)

Hints:
-   you should use the two-argument variants of the pos() functions inside your code;
-   don't worry about case sensitivity.

Sample input
```cmd
donor
Nabucodonosor
donut
Nabucodonosor
```
Output
```cmd
Yes
No
```
## sudoku
### TODO: 
-   reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
-   outputs Yes if the Sudoku is valid, and No otherwise.

Sample input
```cmd
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
```
Output
```cmd
Yes
No
```