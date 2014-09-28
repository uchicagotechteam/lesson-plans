# Introduction, Part 2
## Lesson Overview
Today, we'll be learning about the two basic building blocks of Python program organization: functions and classes. Once we have a basic hold on the two of these, we'll go ahead and start working on a basic project that utilizes all that we've learned thus far. But before we head into functions, we're going to cover the tow most important data structures in Python.

## Functions
Often times, we have a piece of code that we want to reuse multiple times. Let's say you want your program to easily be able to greet the user. The basic code for this would go like this:
```python
name = 'Olivia'
print 'Hello, ' + name + '!'
```
But this code is let's say you want to do this for a couple of different people:
```python
# greeting Olivia
name = 'Olivia'
print 'Hello, ' + name + '!'

# greeting Erin
name = 'Erin'
print 'Hello, ' + name + '!'
```
It seems that we can clean this up. And indeed we can: by defining a function that takes the users name and greeting them:
```python
def greet(name):
    print 'Hello, ' + name + '!'

greet('Olivia')
greet('Erin')
```
Let's explain what we're doing here a bit. First, we use the `def` keyword to tell the Python interpreter that we're about to create a function. The word after `def` is the function name, `greet`. After this, we put in parentheses the function **arguments**, which are the things that Python expects for us to input. This means that Python is expecting us to input a value for `name` each time we call the function `greet`. Then we add a colon (`:`), which is the standard way to denote a code block that is associated with a given piece of code. Also note that all of the lines of code within the function are begun with a single tab. These tabs tell Python that these pieces of code are associated with this specific function. We then call this function, passing in the **arguments** 'Olivia' and 'Erin'. Unfortunately we can't just pass in any values: there are a number of ways to screw this up. Let's see a couple of these examples:
```python
name = 'Jakub'
greet(name)

greet(68) # this will fail
greet(True) # this will also fail

greet(str(68)) # this will work, since first converting argument to string
greet(str(True)) # this will also work
```
As you can see, the function can take another variable as an input instead of a raw value. We can also see that the function will fail on an integer input, and any other input that is not a string, returning the error `TypeError: cannot concatenate 'str' and 'int' objects`. We can fix this by converting the input into a string before calling the function. From this, we can see a pretty easy way to fix our original function:
```python
def greeting(name):
    input = str(name)
    print 'Hello, ' + input + '!'
```
This allows us to (at least partially) ensure that we're eliminating type errors when calling our function. There's also another way to screw up our function call though:
```python
greet()
>>> TypeError: greeting() takes exactly 1 argument (0 given)
greet('Erin', 'Olivia')
>>> TypeError: greeting() takes exactly 1 argument (2 given)
```
From this error, we can see that `greeting` will not behave properly unless we provide it with the exact number of arguments that it expects. We've defined `greeting` to work with only one argument, so that's the way it's going to work. There is a way to hack this to allow a function to take variable numbers of arguments, but that's slightly more advanced Python than we're ready to cover right now. Let's go ahead and make some more functions:
```python
def generic_greet():
    print 'Hello, world!'

generic_greet()

def add(num1, num2):
    print str(num1 + num2)

add(1, 4)
```
As we can see, we can define functions that take no arguments, and we can also define functions that take multiple arguments. We can also define functions that transform data and give us back results. Let's go back to the `add` function we just defined:
```python
def add(num1, num2):
    return num1 + num2

number = add(2, 8)
print number
```
The `return` keyword does just what it says: it causes the function to return a piece of data that we can then go ahead and use. This is allows us to easily do some work on some data, and then quickly return it for further use. Note that a `return` statement will exit your function, so you really can't do something like this:
```python
def add_double(num1, num2):
    return num1 + num2
    num1 = num1 * 2

add_double(4, 3)
```
In this context, the function will exit before the last statement is called, meaning that nothing really happens after the `return` statement is called.

We an also embed loops and other code blocks into our functions. Let's take a look at how we can embed loops into our functions by writing a function to check if a number is prime:
```python
def is_divisible(num, divisor):
    return num % divisor == 0

def is_prime(num):
    for i in range(2, num):
    	if is_divisible(num, i):
	   return False
    return True
```
This is pretty good. This loops through all of the numbers from 2 to one less than the input number and checks if this number can cleanly divide the input number. If none of these division checks work, then the program continues to return True. Note the layering of the code blocks: we can clearly see which code executes exactly where. Also note that `is_divisible` is a helper function that is used by `is_prime` to determine whether or not a function is divisible. We can make this a bit better: this doesn't check whether the number is less than 2, in which case it cannot be a prime number. Let's go ahead and fix that:
```python
def is_prime(num):
    if num < 2:
       return False

    for i in range(2, num):
    	if is_divisible(num, i):
	   return False
    return True
```

## Lists
Lists are a super-fundamental part of Python programming, and are **super** awesome. We saw a list last lesson:
```python
print range(10)
print type(range(10))
```
As expected from the name, lists are lists of elements. They can contain pretty much whatever we want:
```python
seasons = ['spring', 'summer', 'autumn', 'winter']
crimson_tide_championships = [1925, 1926, 1930, 1934, 1941, 1961, 1964, 1965, 1973, 1978, 1979, 1992, 2009, 2011, 2012]
random_stuff = [192, 'hello', False]
```
We can also construct lists easily from scratch, adding one element at a time:
```python
techteamers = []
techteamers.append('Alita')
techteamers.append('Audriana')
techteamers.append('Carmin')
techteamers.append('Darius')
techteamers.append('Emma')
techteamers.append('Erin')
techteamers.append('Kevin')
techteamers.append('Olivia')
techteamers.append('Yujia')

print techteamers
```
Calling the `append` function on the `techteamers` list adds each of these elements to the end of the list. We can now examine our list by checking out each of the elements in the list:
```python
print techteamers[0]
print techteamers[1]

print len(techteamers)
print techteamers[len(techteamers)] # fails
print techteamers[len(techteamers) - 1]
```
We can use this bracket syntax to access individual elements of our list. Note that there's something a bit strange going on here: the numbering of the elements in the list begins from 0 and ends at 1 less than the list length. Keep this in mind, since most programming languages do the same kind of zero-based indexing, and the sooner this becomes habit, the sooner you can avoid silly mistakes.

Let's go ahead and try doing a bit of magic with lists. Let's write a function that find the minimum element in a list:
```python
'''
assuming that the list is at 
least 1 element long
'''
def minimum(nums):
    minimum = nums[0]
    for i in range(len(nums)):
    	if nums[i] < minumum:
	   minimum = nums[i]
    return minimum

numbers = [1, 3, 9, -4, 58, -19, 3, 85]
print minimum(numbers)
```
This works by initializing the minimum value to the beginning of the list, and then goes through the list checking if each element is lower than the next. This is 

## Dictionaries