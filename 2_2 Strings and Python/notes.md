# Strings - brief
- Python strings are immutable sequences.

Example code
```python
# Example 1
word = 'by'         # basic 2 character string
print(len(word))

# Example 2
empty = ''          # strings can be empty
print(len(empty))

# Example 3
i_am = 'I\'m'       # '\' is an escape character and does not add to len()
print(len(i_am))
```

Output
```cmd
2
0
3
```

# Multiline strings
Example Code
```python
multiline = '''Line #1
Line #2'''

print(len(multiline))
```
Output
```cmd
15
```

- Multiline string require triple apostrophes (''')
- Between line 1 and 2 there is a newline character (\n; the escape character doesn't add to the count) that adds to the total string length
  
<table class="python-table" style="width:100%">
    <thead>
        <tr>
            <th>1</th>
            <th>2</th>
            <th>3</th>
            <th>4</th>
            <th>5</th>
            <th>6</th>
            <th>7</th>
            <th>8</th>
            <th>9</th>
            <th>10</th>
            <th>11</th>
            <th>12</th>
            <th>13</th>
            <th>14</th>
            <th>15</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>L</td>
            <td>i</td>
            <td>n</td>
            <td>e</td>
            <td> </td>
            <td>#</td>
            <td>1</td>
            <td>\n</td>
            <td>L</td>
            <td>i</td>
            <td>n</td>
            <td>e</td>
            <td> </td>
            <td>#</td>
            <td>2</td>
        </tr>
    </tbody>
</table>


# Operations and strings

- Concatenate: join strings ('+' operator)
- Replicate: self explanitory ('*' operator)

Example code
```python
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
```
Output
```cmd
ab
ba
aaaaa
bbbb
```

- <code>ord()</code> is used to translate a character to the ASCII/Unicode code point value

Example code
```python
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
```
Output
```cmd
97
32
```

- <code>chr()</code> is used get the corresponding character for a specified code point; *inverse ord()*

```python
# Demonstrating the chr() function.

print(chr(97))
print(chr(945))
```
Output
```cmd
a
α
```
- Note: <code>chr(ord(x)) == x</code> and <code>ord(chr(x)) == x</code> return True

# Strings and sequences

- Strings are sequences meaning they are not lists, but can be treated similarly in many cases by indexing or iterating

Example code
```python
# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
```
Output
```cmd
s i l l y   w a l k s 
```
Example code
```python
# Iterating through a string.
the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
```
Output
```cmd
s i l l y   w a l k s 
```

# Slices

Example code
```python
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

```
Output
```cmd
bd
efg
abd
e
e
adf
beg
```

# The in and not in operations

- <code>in</code> operator checks if its left argument (a string) can be found anywhere within the right argument (another string) and returns True or False
- <code>not in</code> is the opposite

Example code for <code>in</code>
```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
```
Output
```cmd
True
False
False
True
False
```

Example code for <code>not in</code>
```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

```
Output
```cmd
False
True
True
False
True
```

# Python strings are immutable

- lists can be modified with <code>del()</code>, <code>append()</code>, and <code>insert()</code>; whereas strings cannot

Example Code
```python
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
```
Output
```cmd
abcdefghijklmnopqrstuvwxyz
```

# Operations on strings: contd
- <code>min()</code> returns the minimum value of a list of sequence(string); ValueError if list/sequence is empty
- <code>max()</code> returns the maximum value of a list of sequence(string)
- <code>index()</code> searches the sequence from the beginning, in order to find the first element of the value specified in its argument.
- <code>list()</code> takes its argument (a string) and creates a new list containing all the string's characters, one per list element
- <code>count()</code> counts all occurrences of the element inside the sequence


Example Code for <code>min()</code>
```python
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))
```
Output

```cmd
A
[ ]
0
```

Example Code for <code>max()</code>
```python
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))
```
Output
```cmd
z
[y]
2
```

Example Code for <code>index()</code>
```python
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

```
Output
```cmd
2
7
1
```

Example Code for <code>list()</code>
```python
# Demonstrating the list() function:
print(list("abcabc"))
```
Output
```cmd
['a', 'b', 'c', 'a', 'b', 'c']
```

Example Code for <code>count()</code>
```python
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

```
Output
```cmd
2
0
```

# Summary
- Strings are immutable and **can be indexed, sliced, and iterated**
- Strings are subject to <code>in</code> or <code>not in</code> operators
- Single-line strings are denoted with apostrophes('a') or quotes("a")
- Multi-line strings are denoted with trigraphs:
```python
'''
docstring
docstring
'''
# or 
"""
docstring
docstring
"""
```
- <code>len()</code> returns length of a string; not including escape characters
```python
print(len("\n\n"))      # prints '2'
```
- concatenate with '+' operator
- iterate with '*' operator

```python
asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)       # prints '*+*+*+*+*'
```
- <code>chr()</code> and <code>ord()</code> are used to either create a character from a numberic codepoint or determine the codepoint of a specified character
```python
chr(ord(character)) == character
ord(chr(codepoint)) == codepoint
```
- <code>line()</code> - creates a list consisting of all the string's characters
- <code>max()</code> - finds the character with the maximum codepoint
- <code>min()</code> - finds the character with the minimum codepoint
- <code>index()</code> - finds the index of a given substring within a string

# Quiz

