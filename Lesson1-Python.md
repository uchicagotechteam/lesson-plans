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

### Which Python?


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

```
Other languages make this pretty explicit. For example, let's take a look at how this works in [C](http://en.wikipedia.org/wiki/C_(programming_language)):
```c++
int num = 1;
string greeting = "hello";
```
Each of them has their own purpose and behaves in a very different kind of way. Let's first get a handle on these different types of variables.

As we can see, we have a **string**, an **int**, a **float**, and a **bool**. Strings are the basic data type for all text. Ints are integer numbers, floats are numbers with floating-point decimals, and booleans are either `True` or `False`.

## PostScript: Which Python?
This is not super-important to us right now, but definitely worth mentioning, since you will run into this issue very, very soon. There is more than one implementation of Python, each one with very different backends. These implementations [Jython](http://en.wikipedia.org/wiki/Jython), [CPython](http://en.wikipedia.org/wiki/CPython), [PyPy](http://en.wikipedia.org/wiki/PyPy), and [IronPython](http://en.wikipedia.org/wiki/IronPython), each of which is worth exploring. 

But what really matters is the version number. From 2000 to 2008, the Python 2.0 branch was the de-facto Python standard, and pretty much everyone used it. But in 2008, Guido Van Rossum (Python's Benevolent Dictator For Life) released Python 3.0, which broke backwards-compatibility with Python 2.X. This made a lot of people very angry, and a decision was made to continue development on Python 2.6, effectively creating two incompatible versions of Python. Currently, there are two primary versions of Python: 2.7.8 and 3.4.1.  Python 3 is the future of the language, and major software companies are in the middle of migrating to Python 3. Having said that, I am choosing to teach you guys Python 2. Most companies currently continue to run Python 2, and a number of pretty critical packages (packages that we're going to use) are only available for Python 2. The differences between the two Pythons are not major enough to make a massive difference when picking up the other version, but are significant enough that it does effect the way you write certain parts of your code. We can discuss more offline, but this is the current state of the world.