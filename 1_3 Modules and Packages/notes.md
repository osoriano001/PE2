# First Module

## Step 2
```python
import module
```
<i>main.py</i>

## Step 3
```python
print("I like to be a module.")
```
<i>module.py</i>

## Step 4
```
> python3 .\main.py
I like to be a module.
```
cmd output

## Step 5
```python
print("I like to be a module.")
print(__name__)
```
<i>module.py</i>

```cmd
> python3 .\module.py
I like to be a module.
__main__

> python3 .\main.py  
I like to be a module.
module
```
cmd output

## Step 6
```python
if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")
```
<i>module.py</i>

```cmd
> python3 .\main.py
I like to be a module.

> python3 .\module.py
I prefer to be a module.
```
cmd output

## Step 7
```python
counter = 0
   
if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")
```
<i>module.py</i>

## Step 8
```python
import module
print(module.counter)
```
<i>main.py</i>

```cmd
> python3 .\module.py
I prefer to be a module.

> python3 .\main.py  
I like to be a module.
0
```
cmd output

## Step 9 
```python
#!/usr/bin/env python3 

""" module.py - an example of a Python module """
 
__counter = 0
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)
```
<i>module.py</i>

- <code>#!</code> in the first line is called the <i>shabang, shebang, hashbang, poundbang or even hashpling</i>. Instructs the OS how to execute the contents of the file (in other words, what program needs to be launched to interpret the text)
- <code>def</code> are functions that can be called via import of <i>module.py</i>
- <code>if __name__ == "__main__":</code> detects whether the module is being used as a standalone or module to run simple tests.

## Step 10

```python
from module import suml, prodl
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
```
```
> python3 .\module.py
I prefer to be a module, but I can do some tests for you.
True
True

> python3 .\main.py  
0
1
```
cmd output

## Step 11

```text
C:\
└── Users\
    └── ammiel.soriano\
        └── PE2\
            └── 1_3 Modules and Packages\
                ├── main.py
                ├── main2.py
                ├── notes.md
                ├── modules\
                |   └── module.py
                └── packages\
                    ├── extra\
                    |   ├── iota.py
                    |   ├── __init__.py
                    |   └── good\
                    |       ├── alpha.py
                    |       ├── beta.py
                    |       └── best\
                    |           ├── sigma.py
                    |           └── tau.py
                    └── ugly\
                        ├── omega.py
                        └── psi.py
```
```python
import sys
 
# Accessing environment $PATH through sys module
for p in sys.path:
  print(p)
```

## Step 12

```python
from sys import path

path.append('modules')

from modules import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
```
<i>main.py</i>

```
> python3 .\main.py                                              
0
1

\modules> python3 .\module.py
I prefer to be a module, but I can do some tests for you.
True
True
```
cmd output

# First Package

## Step 1

```python
#! /usr/bin/env python3

""" module: alpha """

def funA():
  return "Alpha"

if __name__ == "__main__":
  print("I prefer to be a module.")
```
<i>alpha.py</i>

## Step 2
- Repeat for other package <code>*.py</code> other than \_\_init__.py
- \_\_init__.py is key to packages

## Step 3
```text
C:\
└── Users\
    └── ammiel.soriano\
        └── PE2\
            └── 1_3 Modules and Packages\
                ├── main.py
                ├── main2.py
                ├── notes.md
                ├── modules\
                |   └── module.py
                └── packages\
                    ├── extra\
                    |   ├── iota.py
                    |   ├── __init__.py
                    |   └── good\
                    |       ├── alpha.py
                    |       ├── beta.py
                    |       └── best\
                    |           ├── sigma.py
                    |           └── tau.py
                    └── ugly\
                        ├── omega.py
                        └── psi.py
```

## Step 4 

- Python expects there to be a file with a very unique name inside the package's folder: \_\_init__.py.

- The contents of the file are executed when any of the package's modules is imported. If you don't want any special initializations, you can leave the file empty, but you can't omit it.

## Step 5

- \_\_init__.py can be added within subdirectories of the packages if unique handling of modules are necessary

## Step 6

- Downloadable .zip https://edube.org/uploads/media/default/0001/01/39a03067f85a9b39c0c94ca50b5d445b7df18a04.zip

## Step 7
```python
# from sys import path
# path.append('..∖∖packages')
 
import packages.extra.iota
print(packages.extra.iota.funI())
```
<i>main2.py</i>

Other variant is valid
```python
# from sys import path
# path.append('..∖∖packages')

from packages.extra.iota import funI
print(funI())
```
<i>main2.py</i>

## Step 8
```python
# from sys import path

# path.append('..∖∖packages')

import packages.extra.good.best.sigma
from packages.extra.good.best.tau import funT

print(packages.extra.good.best.sigma.funS())
print(funT())
```
<i>main2.py</i>

With aliasing

```python
# from sys import path

# path.append('..∖∖packages')


import packages.extra.good.best.sigma as sig
import packages.extra.good.alpha as alp

print(sig.funS())
print(alp.funA())
```
<i>main2.py</i>

## Step 9
<h2>Importing from .zip package</h2>

```python
from sys import path

path.append('..∖∖extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
```

# Section Summary

## Quiz

<h3>Question 1: <br>You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?</h3>

<h3>Answer:</h3>

```python
import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()
```

<h3>Question 2: <br>Some additional and necessary packages are stored inside the <i>D:\Python\Project\Modules</i> directory. Write a code ensuring that the directory is traversed by Python in order to find all requested modules.</h3>

<h3>Answer:</h3>

```python
import sys

# note the double backslashes!
sys.path.append("D:\\Python\\Project\\Modules")
```

<h3>Question 3: <br>The directory mentioned in the previous exercise contains a sub-tree of the following structure:</h3>

```text
abc
 |__ def
     |__ mymodule.py

Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.
```

<h3>Answer:</h3>

```python
import abc.def.mymodule
```