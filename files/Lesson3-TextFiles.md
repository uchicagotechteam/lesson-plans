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

The first address is the absolute address of the directory. This address explicitly describes the path to the directory of interest from the filesystem root. The second address is the relative address. This describes the path to the directory of interest from the current directory.

Note that when describing the relative address, there are two important shortcuts. The first is `..`, which refers to the directory directly above the current directory, i.e. the current directory's 'parent directory'. We will see ways to use this when moving around the directory shortly. The second is `.`, which refers to the current directory. While seldom used when traversing the directory tree, this is more often used when running commands that you want to act upon the current directory.

### Listing Files
Whenever you're in a directory, the first thing you usually want to do is figure out what is located in it. You do this by typing the command
```bash
ls
```
This command simply lists all files within the directory. We can also provide absolute and relative addresses to the command as parameters:
```bash
ls /home
ls ~/School
ls ../classes/statistics
```

### Moving Around The Filesystem
In order to figure out the filesystem, we need to move around it as well as figure out where we are. We do this via the `cd` command (which simply changes the directory in which you are currently working. In order to change your directory, we have to give `cd` a paramter of the form a directory path, either absolute or relative:
```bash
cd School
cd ../Projects
cd 
```
Running `cd` without a parameter automatically returns you to your home directory, i.e. the directory described by `~`. This can be very useful when you just want to get back to your home directory without having to type in long directory paths.

## Opening files
Generally, when working with a file in Python, you first have to open it and load it into memory. We can do this using the built-in `open` method:
```python
text = open('mobydick')
```
## File Methods

## String Methods

## Regular Expressions
## 