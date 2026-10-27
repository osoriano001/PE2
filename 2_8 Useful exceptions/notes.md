# Built-in Exceptions
General structure of exceptions consists of:
-   its name;
-   its location in the exception tree;
-   a short description;
-   a concise snippet of code showing the circumstances in which the exception may be raised.

## Built-in Exceptions (details reference [Python Docs](https://docs.python.org/3/builtins/exceptions.html))
```
BaseException
 ├── SystemExit  (Raised on sys.exit())
 ├── KeyboardInterrupt  (Raised on Ctrl+C)
 ├── GeneratorExit  (Raised when a generator or coroutine is closed)
 ├── BaseExceptionGroup  (Container for wrapping multiple unrelated exceptions)
 └── Exception  (The base class for all non-system-exiting exceptions)
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError  (Failed assert statement)
      ├── AttributeError  (Failed attribute reference or assignment)
      ├── BufferError
      ├── EOFError  (End-of-file condition with no input data)
      ├── ExceptionGroup  (Wraps multiple Exception instances)
      ├── ImportError
      │    └── ModuleNotFoundError  (Raised when a module cannot be located)
      ├── LookupError
      │    ├── IndexError  (Sequence index out of range)
      │    └── KeyError  (Dictionary key not found)
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError  (Local variable referenced before assignment)
      ├── OSError  (System-related errors like I/O failures)
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── IsADirectoryError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── ReferenceError  (Accessing a garbage-collected weak reference proxy)
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError  (Maximum recursion depth exceeded)
      ├── StopIteration / StopAsyncIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── TypeError  (Operation applied to an inappropriate type)
      ├── ValueError  (Correct type, but invalid value)
      │    └── UnicodeError
      └── Warning  (Base class for non-fatal warning alerts)
           ├── DeprecationWarning
           ├── RuntimeWarning
           └── UserWarning
```

# LAB - Reading integers safely

Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

-   accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
-   if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
-   if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
-   if the input value is valid, return it as a result.

Sample basis:
```python
def read_int(prompt, min, max):
    #
    # Write your code here.
    #


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    
```

Example run:
```cmd
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
```