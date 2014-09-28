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
Let's explain what we're doing here a bit. First we 
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
techteamers.append('Erin')
techteamers.append('Kevin')
techteamers.append('Olivia')
techteamers.append('Yujia')

print techteamers
```
Calling the `append` function 

## Dictionaries

## Functions