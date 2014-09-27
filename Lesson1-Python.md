# TechTeam Lesson 1

## Program Goals
My primary goal is to provide you guys with a basic understanding of the things that hold the internet together, and to provide you guys with a strong foundation in at least one programming language (Python, in this case). We're going to be focusing on gaining at least some level of mastery in the language, and then we'll be focusing on doing various data analysis tasks in the language. We'll also be focusing on interacting with various APIs, focusing primarily on Twitter and Facebook (LinkedIn if we have time).

### Skills
1. Programming
2. Web Development
3. Data Science 

### Technologies
1. Python
2. HTML/CSS/JavaScript
3. JSON/XML
4. Django

### APIs
1. Twitter
2. Facebook
3. LinkedIn

# Lesson Start
## What is Python?
Python is a dynamically-typed, interpreted language. It's easy to use, it's reasonably fast, and allows you to quickly create very powerful programs. It's used in everything from large-scale data science to running some of the biggest websites in the world. We're going to focus on doing awesome things with Python over the next couple of weeks, but first we have to focus on the basic.

## Our Setup
### Virtual Machine

## Hello World!
Open a text file named `hello.py`. Type into this file:
```python
print 'Hello World!'
```
We'll now execute this file by going into the directory where your file is being held and executing `python hello.py`.

## Variables
It's hard to work with data if you can't keep track of it. In programming languages, we keep track of various bits of data using **variables**. This allows us to easily keep track of and reuse bits of data. Let's try assigning 'Hello World!' to a variable, and making some magic happen with it.
```python
greeting = 'Hello WORLD!'
print greeting.upper()
print greeting.lower()
```

## Data Types
Though Python allows us to assign various bits of data to variables, we have to understand that there are many different kinds of data that can be held within these variables. Let's investigate a bit with some variables:
```python
var_1 = 'hello'
var_2 = 23
var_3 = 9.5
var_4 = True

print type(var_1)
print type(var_2)
print type(var_3)
print type(var_4)
```
What we're doing here is assigning 4 different pieces of data to 4 different variables. We're then calling the built-in function `type` on these variables, and printing out the result. As you can see, we have 4 different types that we're printing out. To quickly explain each one:
* **string**: Strings, generally contain textual data. Python provides a smorgasbord of functions to work with these.
* **int**: Integral numbers, support basic mathematical operations.
* **float**: Floating point numbers.
* **bool**: Boolean values. Limited to either `True` or `False`.

Despite these different types, Python allows you to stuff these into any variable, and silently detects and notes the data type. This allows you to do stuff like this:
```python
my_var = 2
my_var = my_var + 2
print my_var
print type(my_var)

my_var = True
print my_var
print type(my_var)
```
As you can see, Python allows us to stuff completely different data types into the same variable. This kind of type inference can have some pretty interesting outcomes. Let's see an example:
```python
num_1 = 3
print type(num_1)

num_2 = 3.14
print type(num_2)

num_3 = num_1 + num_2
print type(num_3)
```
Here we can see that Python automatically makes silent type conversions as necessary. There are situations, though, when not even these silent conversions will save a calculation. Let's check one out:
```python
val_1 = 3
val_2 = 'hello'
val_3 = val_1 + val_2
```
This calculation is going to die, and it dies loudly. Python can do type conversions, but only to a certain extent. At a certain level, it will just decide that the conversion is just not worth is, and will die. 
This type stuff seems like mumbo-jumbo right now, but it matters because other languages make this pretty explicit. For example, let's take a look at how this works in [C++](http://en.wikipedia.org/wiki/C%2B%2B)):
```c++
int num = 1;
string greeting = "hello";
```
As we can see, we have to explictly state the type of the variable before we actually use it. This means we can't write code like this without the compiler complaining very loudly:
```c++
int num_1 = 3;
float num_2 = 3.14;
float num_3 = num_1 + num_2;
```
Keep this type stuff in mind as we're going forward: it's all going to matter.

## Comments
Before we go any further, we need to remember that sometimes, it's worth explaining ourselves. I've had many, many situations where I've been presented with several thousand lines of raw code and spent weeks (sometimes months) making sense of it. As such, Python allows us leave comments in our code. You can make a single-line comment by adding `#` before some text:
```python
# this is a comment
num_1 = 3
print num_1
```
Note that the interpreter does nothing with this comment: it simply ignores it and moves on. Comments are simply for us to use to help ourselves and others better understand our code. We can also add in multi-line comments:
```python
"""
This is a multi
line comment
"""
greeting = "hello"
'''
This is also
a really long comment
'''
```
The proper amount of comments to include varies from place to place: I've worked in places that where comments are included in every other line and other places that regularly put out very complex programs with no comments. As a rule, add in as many comments as are necessary to make your code more readable, but not so many that your code becomes less readable. For example:
```python
# assigning first num
num_1 = 3
# printing first num
print type(num_1)

# assigning second num
num_2 = 3.14
# printing second num
print type(num_2)

# assigning third num
num_3 = num_1 + num_2
# printing third num
print type(num_3)
```
Super not-readable. Limit yourself.

## Number Operations
We have the basics of variables, types, and comments down. Let's go ahead and do some calculations with these
```python
num_1 = 1 + 2
num_2 = num_1 - 5
num_3 = 8 * num_2
num_4 = num_3 / 4

print num_1
print num_2
print num_3
print num_4
```
Basic number operations: nothing revolutionary or that you haven't seen since grade school. If we're working on making modifications to a single variable, we have a syntax that allows us to take a bit of a shortcut:
```python
var = 1

var += 10
print var

var -= 5
print var

var *= 5
print var

var /= 10
print var
```
This syntax allows us to cleanly do transformations on one variable without having to define both operatands. Let's take our math work up a notch to exponentiation and modulo division:
```python
num_1 = 10 % 2 # modulo division
num_2 = 2 ** 5 # exponentiation

print num_1
print num_2
```
As you can see, modulo (`%`) is simply remainder division, and exponentiation (`**`) is exactly what you'd expect.

## Control Flow
A lot of the time, you don't want all of your code to execute all of the time. Let's say we're trying to inform a person what we think of their height. Using this, we can do the following:
```python
# height given in feet
height = 10

if height > 5:
   print "You're tall!"
```
Okay, so what's happening here? We're setting a variable, and then creating a block of code that checks if a certain condition is met (i.e. `height > 5`), and executes a print statement if it is met (i.e. `print "You're tall!"`). Things to note here are the colon (`:`) at the end of the condition check. This lets Python know that we're entering into a block of code that should be executed only when the condition line is true. Also note that we have put a **tab** before `print "You're tall!"`. Python separates code into blocks using whitespace, specifically tabs. The number of tabs located before a block of code determines what block this code is associated with. This is confusing now, but we'll give more examples to explain later.

Let's say we want to let our person know that they are short if they're not over 5 feet tall. Let's add an `else` statement to make this happen:
```python
# height given in feet
height = 10

if height > 5:
   print "You're tall!"
elif height == 5:
   print "You're pretty average!"
else:
   print "You're short!"
```
Let's say we want to let people who are 5 foot whatever know that they're not actually tall. Let's add on another intermediary statement that executes if the first `if` condition is not true, but if `height` is five feet:
```python
# height given in feet
height = 10

if height > 5:
   print "You're tall!"
elif height == 5:
   print "You're pretty average!"
else:
   print "You're short!"
```
As we can see, we use the `elif` keyword, we can add in another condition that checks and executes before the `else`.

## Loops
Let's say we want to do something very simple, like print out "Hello!" 10 times (we're very enthusiastic greeters). Let's try to make this happen:
```python
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
print "Hello!"
```
But this is really no good. Let's fix this by writing a loop:
```python
for i in range(10):
    print "Hello!"
```
What happens here is for each number in a range of 0 to 9, the code executes the `print` statment. To better understand this, let's examine `range` for a second:
```python
print range(10)
```
We can see here that `range(10)` generates a list of 10 numbers, numbered from 0 to 9. Our `for` loop iterates over this list and perfroms the action we want once for every element within the list. To get a better grasp on this, let's try a slightly bit more involved loop:
```python
for i in range(10):
    print i
```
Here we can see each of the elements in the range that are printed out. This isn't the only way to loop in Python: we can also try the `while` loop, which executes a piece of code as long as certain condition is true:
```python
i = 0
while i < 10:
      print i
      i += 1
```
This has the exact same effect as the previous `for` loop, but works in a completely different way. While the for loop traversed over an **iterator** and executed once for each element in the iterator, the while loop executes the code block associated with it for as long as the loop condition is true. The above loop works just fine, but can be broken pretty easily:
```python
i = 0
while i < 10:
      print i
```
This is a pretty terrible idea. Since your `i` value is not being changed, `i` will always be less than 10, meaning that this loop will execute forever. There are some problems that you do want to execute 'forever' (or for some long period of time), but this is not one of them.

## PostScript: Which Python?
This is not super-important to us right now, but definitely worth mentioning, since you will run into this issue very, very soon. There is more than one implementation of Python, each one with very different backends. These implementations [Jython](http://en.wikipedia.org/wiki/Jython), [CPython](http://en.wikipedia.org/wiki/CPython), [PyPy](http://en.wikipedia.org/wiki/PyPy), and [IronPython](http://en.wikipedia.org/wiki/IronPython), each of which is worth exploring. 

But what really matters is the version number. From 2000 to 2008, the Python 2.0 branch was the de-facto Python standard, and pretty much everyone used it. But in 2008, Guido Van Rossum (Python's Benevolent Dictator For Life) released Python 3.0, which broke backwards-compatibility with Python 2.X. This made a lot of people very angry, and a decision was made to continue development on Python 2.6, effectively creating two incompatible versions of Python. Currently, there are two primary versions of Python: 2.7.8 and 3.4.1.  Python 3 is the future of the language, and major software companies are in the middle of migrating to Python 3. Having said that, I am choosing to teach you guys Python 2. Most companies currently continue to run Python 2, and a number of pretty critical packages (packages that we're going to use) are only available for Python 2. The differences between the two Pythons are not major enough to make a massive difference when picking up the other version, but are significant enough that it does effect the way you write certain parts of your code. We can discuss more offline, but this is the current state of the world.