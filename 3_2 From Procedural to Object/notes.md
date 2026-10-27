# Class and subclasses

Sample class:
```python
class Stack:
    # __init__ required in any class constructor statement
    # class functions require self parameter in all methods defined 
    def __init__(self):
        # __ double underscore makes attribute private and not visible outside of bound of class
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        # calling Stack object within subclass requires __init__ constructor to be called
        # any superclass method called requires self parameter
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
```


# LAB Counting stack
Your task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

-   introduce a property designed to count pop operations and name it in a way which guarantees it is hidden;
-   initialize it to zero inside the constructor;
-   provide a method which returns the value currently assigned to the counter (name it get_counter()).
-   
Code structure
```python
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
    #
    # Fill the constructor with appropriate actions.
    #

    def get_counter(self):
    #
    # Present the counter's current value to the world.
    #

    def pop(self):
    #
    # Do pop and update the counter.
    #
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
```

# LAB Queue aka FIFO
Let's try something new now. A queue is a data model characterized by the term FIFO: First In – First Out. Note: a regular queue (line) you know from shops or post offices works exactly in the same way – a customer who came first is served first too.

Your task is to implement the Queue class with two basic operations:

-   put(element), which puts an element at end of the queue;
-   get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
<br>
Follow the hints:

-   use a list as your storage (just like we did with the stack)
-   put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
-   define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.

Sample structure:
```python
class QueueError(???):  # Choose base class for the new exception.
    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        #
        # Write code here
        #

    def put(self, elem):
        #
        # Write code here
        #

    def get(self):
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
```

# LAB FIFO continued
Your task is to slightly extend the Queue class's capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Sample structure:
```python
class QueueError(???):
    pass


class Queue:
    #
    # Code from the previous lab.
    #


class SuperQueue(Queue):
    #
    # Write new code here.
    #


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
```

Hint:
```python
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError
```