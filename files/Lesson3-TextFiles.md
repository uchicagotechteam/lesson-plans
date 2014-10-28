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

The second, abbreviated directory address is equally interesting. This path begins with a `~`, which is an alias for my home folder. The shell is not configured to launch from the root directory, since the root contains many mission-critical folders, which could destroy your OS if removed. As such, most of your work is going to be done in your working directory, which is generally located at `/home/yourcomputername`. 

### Listing Files
Whenever you're in a directory, the first thing you usually want to do is figure out what is located in it. You do this by typing the command
```bash
ls
```
This command simply lists all files within the directory. We can also provide absolute and relative addresses to the command as parameters:
```bash
ls /home
ls ~/School
```

### Moving Around The Filesystem
In order to figure out the filesystem, we need to move around it as well as figure out where we are. We do this via the `cd` command (which simply changes the directory in which you are currently working:
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