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
print('Hello World!')
```
We'll now execute this file by going into the directory where your file is being held and executing `python hello.py`.

## Variables
It's hard to work with data if you can't keep track of it. In programming languages, we keep track of various bits of data using **variables**. This allows us to easily keep track of and reuse bits of data. Let's try assigning 'Hello World!' to a variable, and making some magic happen with it.
```python
greeting = 'Hello WORLD!'
print(greeting.upper())
print(greeting.lower())
```

## Data Types
Though Python allows us to assign various bits of data to variables, we have to understand that there are many different kinds of variables. Each of them has theire own purpose and behaves in a very different kind of way. Let's first get a handle on these different types of variables.
```python
var_1 = 'hello'
var_2 = 23
var_3 = 9.5
var_4 = True

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
```
As we can see, we have a **string**, an **int**, a **float**, and a **bool**. Strings are the basic data type for all text. Ints are integer numbers, floats are numbers with floating-point decimals, and booleans are either `True` or `False`.