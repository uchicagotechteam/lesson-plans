# Working with Text Files
Today we're going to be talking about working with files in Python. Files are the bread and butter of data science: you'll be working with them all the time, in various formats, so its best to go ahead and learn the basics. 

## The Command Line
Before we start, let's go ahead and remind ourselves how to navigate the command line.
### Directories
Whenever we are working in a command line environment, we are in a given directory. Directories are analogous to "folders" in Windows. We can check what directory we are in using the command
```bash
pwd
```
This will output the current directory in absolute format. We generally have directories printed out in two different formats: absolute and relative
```
/home/jtuchol/School/techteam/lesson-plans/files
~/School/techteam/lesson-plans/files
```
The absolute address always begins with a forward slash `/`. This is the 'root' directory, which is the top point of the filesystem. We can see from the first address that the path to my current directory goes through a series of directories:
```
home -> jtuchol -> School -> techteam -> lesson-plans -> files
```
This is the path to get to my current location from the root of the filesystem.

The second, abbreviated directory address is equally interesting. This path begins with a `~`, which is an abbreviation for my home folder. The shell is configured to launch not in out 
```bash
cd
cd ..
cd 
```
## Opening files
Generally, when working with a file in Python, you first have to open it and load it into memory. We can do this using the built-in `open` method:
```python
text = open('mobydick')
```
## File Methods

## String Methods

## Regular Expressions
## 