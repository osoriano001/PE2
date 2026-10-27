# <code>capitalize()</code>
Creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

-   if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), it will be converted to upper-case;
-   all remaining letters from the string will be converted to lower-case.
-   **Note:** since strings are immutable the fucntion returns a string value and does not directly modifies the string argument; if you need to retain the output assign to variable

Example Code
```python
# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
```
Output
```cmd
Abcd
```

Example Code
```python
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
```
Output
```cmd
Alpha
Alpha
 alpha
123
Αβγδ
```

# <code>center()</code>
The one-parameter variant of the <code>center()</code> method makes a copy of the original string, trying to center it inside a field of a specified width.<br>
-   padding is default to spaces
```python
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
```
Output
```cmd
[  alpha   ]
```
```python
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
```
Output
```cmd
[Beta]
[Beta]
[ Beta ]
```

The two-parameter variant of <code>center()</code> makes use of the character from the second argument as padding, instead of a space.

```python
print('[' + 'gamma'.center(20, '*') + ']')
```
Output
```cmd
[*******gamma********]
```
# <code>endswith()</code>
Checks if the given string ends with the specified argument and returns <code>True</code> or <code>False</code>.
```python
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
```
Output
```cmd
yes
```

```python
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
```
Output
```cmd
True
False
False
True
```

# <code>find()</code>
Looks for a substring and returns the index of the first occurrence of this substring, but:
-   it's safer – it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
-   **works with strings only** – don't try to apply it to any other sequence.   

```python
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
```
Output
```cmd
1
-1
```
-   **Note:** don't use <code>find()</code> if you only want to check if a single character occurs within a string - the <code>in</code> operator will be significantly faster.
```python
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
```
Output
```cmd
2
2
0
-1
```
-   Two-parameter variant of the <code>find()</code> method can designate a starting point
```python
print('kappa'.find('a', 2))
```
Output
```cmd
4
```
-   <code>find()</code> can be looped to search for all occurrences within a string
```python
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
```
Output
```cmd
15
80
198
221
238
```

-   Three parameter variant of <code>find()</code> designates the range of indexes to search; [start_index, end_index]

```python
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
```
Output
```cmd
1
-1
```
# <code>isalnum()</code>
The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result
```python
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
```
Output
```cmd
True
True
True
False
False
False
```
```python
t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())
```
Output
```cmd
False
False
True
```
# <code>isalpha()</code>
Returns whether the sequence consists of alphabetical characters
```python
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())
```
Output
```cmd
True
False
```
# <code>isdigit()</code>
Returns whether sequence consists of numeric characters
```python
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())
```
Output
```cmd
True
False
```

# <code>islower()</code>
The <code>islower()</code> method is a fussy variant of <code>isalpha()</code> – it accepts lower-case letters only.
```python
# Example: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())
```
Output
```cmd
False
True
```

# <code>isspace()</code>
The <code>isspace()</code> method identifies whitespaces only – it disregards any other character (the result is False then).
```python
# Example: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
```
Output
```
True
True
False
```

# <code>isupper()</code>
The <code>isupper()</code> method is the upper-case version of <code>islower()</cdoe> – it concentrates on upper-case letters only.
```python
# Example: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
```
Output
```cmd
False
False
True
```

# <code>join()</code>
The <code>join()</code> method is rather complicated, so let us guide you through it step by step:

-   as its name suggests, the method performs a join – it expects one argument as a list; it must be assured that all the list's elements are strings – the method will raise a <code>TypeError</code> exception otherwise;
-   all the list's elements will be joined into one string but...
-   ...the string from which the method has been invoked is used as a - separator, put among the strings;
-   the newly created string is returned as a result.
```python
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
```
Output
```cmd
omicron,pi,rho
```

# <code>lower()</code>
Makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts
```python
# Demonstrating the lower() method:
print("SiGmA=60".lower())
```
Output
```cmd
sigma=60
```

# <code>lstrip()</code>
Returns a newly created string formed from the original one by removing all leading whitespaces
```python
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
```
Output
```cmd
[tau ]
```
The one-parameter version of the lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:
```python
print("www.cisco.com".lstrip("w."))
```
Output
```cmd
cisco.com
```
```python
print("pythoninstitute.org".lstrip(".org"))
```
Output
```cmd
pythoninstitute.org
```

# <code>replace()</code>
The two-parameter <code>replace()</code> method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
```python
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
```
Output
```cmd
www.pythoninstitute.org
Thare are it!
Apple
```
The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
```python
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
```
Output
```cmd
Thare is it!
Thare are it!
```

# <code>rfind()</code>
The one-, two-, and three-parameter versions of the <code>rfind()</code> method do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).
```python
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
```
Output
```cmd
8
-1
4
```

# <code>rstrip()</code>
Two variants of the <code>rstrip()</code> method do nearly the same as lstrips, but affect the opposite side of the string.
```python
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
```
Output
```cmd
[ upsilon]
cis
```


# <code>split()</code>
The <code>split()</code> method does what it says – it splits the string and builds a list of all detected substrings.
-   The method assumes that the substrings are delimited by whitespaces – the spaces don't take part in the operation, and aren't copied into the resulting list.
```python
# Demonstrating the split() method:
print("phi       chi\npsi".split())
```
Output
```cmd
['phi', 'chi', 'psi']
```


# <code>startswith()</code>
Checks if a given string starts with the specified substring.
```python
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()
```
Output
```cmd
False
True
```

# <code>strip()</code>
Makes a new string lacking all the leading and trailing whitespaces.
```python
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
```
Output
```cmd
[aleph]
```

# <code>swapcase()</code>
Makes a new string by swapping the cases of all letters within the source string: lower-case characters become upper-case, and vice versa
```python
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()
```
Output
```cmd
i KNOW THAT i KNOW NOTHING.
```

# <code>title()</code>
Changes every word's first letter to upper-case, turning all other ones to lower-case.
```python
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()
```
Output
```cmd
I Know That I Know Nothing. Part 1.
```

# <code>upper()</code>
Makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
```python
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
```
Output
```cmd
I KNOW THAT I KNOW NOTHING. PART 2.
```

# Summary
## *Methods below follow <code>{string}.{method}(**arg)</code>
1. Some of the methods offered by strings are:

-   <code>capitalize()</code> – changes all string letters to capitals;
-   <code>center()</code> – centers the string inside the field of a known length;
-   <code>count()</code> – counts the occurrences of a given character;
-   <code>join()</code> – joins all items of a tuple/list into one string;
-   <code>lower()</code> – converts all the string's letters into lower-case letters;
-   <code>lstrip()</code> – removes the white characters from the beginning of the string;
-   <code>replace()</code> – replaces a given substring with another;
-   <code>rfind()</code> – finds a substring starting from the end of the string;
-   <code>rstrip()</code> – removes the trailing white spaces from the end of the string;
-   <code>split()</code> – splits the string into a substring using a given delimiter;
-   <code>strip()</code> – removes the leading and trailing white spaces;
-   <code>swapcase()</code> – swaps the letters' cases (lower to upper and vice versa)
-   <code>title()</code> – makes the first letter in each word upper-case;
-   <code>upper()</code> – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

-   <code>endswith()</code> – does the string end with a given substring?
-   <code>isalnum()</code> – does the string consist only of letters and digits?
-   <code>isalpha()</code> – does the string consist only of letters?
-   <code>islower()</code> – does the string consists only of lower-case letters?
-   <code>isspace()</code> – does the string consists only of white spaces?
-   <code>isupper()</code> – does the string consists only of upper-case letters?
-   <code>startswith()</code> – does the string begin with a given substring?

# LAB Your own split
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

-   it should accept exactly one argument – a string;
-   it should return a list of words created from the string, divided in the places where the string contains whitespaces;
-   if the string is empty, the function should return an empty list;
-   its name should be mysplit()
  
Expected output
```cmd
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]
```
*Lab.py*
```python
def mysplit(arg: str) -> list:
    if not len(arg.strip()):
        return []
    return arg.split()

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
```
