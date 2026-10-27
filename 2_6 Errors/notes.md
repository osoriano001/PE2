# Errors, failures, and other plagues

Sample code:
```python
import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)
```
The code block above can error out due to string inputs and if negative numbers are passed.

# Exceptions
Each time your code tries to do something wrong/foolish/irresponsible/crazy/unenforceable, Python does two things **(Raising Exceptions)**:

-   **it stops your program;**
-   **it creates a special kind of data, called an exception.**

Followed by:
-   the raised exception expects somebody or something to notice it and take care of it;
-   if nothing happens to take care of the raised exception, the program will be forcibly terminated, and you will see an error message sent to the console by Python;
-   otherwise, if the exception is taken care of and handled properly, the suspended program can be resumed and its execution can continue.
  
Sample Code:
```python
value = 1
value /= 0
```
Output
```cmd
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    value /= 0
ZeroDivisionError: division by zero
```

Sample Code:
```python
my_list = []
x = my_list[0]
```
Output
```cmd
Traceback (most recent call last):
File "lst.py", line 2, in <module>
x = list[0]
IndexError: list index out of range
```
How do you handle exceptions? The word try is the key to the solution.

The recipe for success is as follows:

-   first, you have to try to do something;
-   next, you have to check whether everything went well.
Sample Code:
```python
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")
```
Output
```cmd
Enter the first number: 1
Enter the second number: 0
This operation cannot be done.
THE END.
```
# Summary

Generally:
-   in the first step, Python tries to perform all instructions placed between the try: and except: statements;
-   if nothing is wrong with the execution and all instructions are performed successfully, the execution jumps to the point after the last line of the except: block, and the block's execution is considered complete;
-   if anything goes wrong inside the try: and except: block, the execution immediately jumps out of the block and into the first instruction located after the except: keyword; this means that some of the instructions from the block may be silently omitted.

```python
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")
```
Output
```cmd
Enter a number: 0
Oh dear, something went wrong...
THE END.
```
```python
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
```
Output
```cmd
Enter a number: 0.000000000000000000000000000
You must enter an integer value.
THE END.
```