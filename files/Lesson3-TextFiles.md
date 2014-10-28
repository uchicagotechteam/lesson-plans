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

### Making Directories

## Files in Python
### Preparation
To start, let's go ahead and create ourselves a directory to work in:
```bash
cd
cd Documents
mkdir techteam
cd techteam
mkdir text
cd text
```
Cool, so we're now in our directory of interest. Now, let's got ahead and download the files we'll be working with. To do this, we're going to use the `wget` utility to download two URLs:
```bash
wget https://raw.githubusercontent.com/uchicagotechteam/lesson-plans/master/files/mobydick.txt
wget https://raw.githubusercontent.com/uchicagotechteam/lesson-plans/master/files/access_log
```
If we now use `ls` to check the contents of our directory, we should see two new files: `mobydick.txt` and `access_log`. We can check out the contents of these files by just looking at the first couple of lines:
```bash
head mobydick.txt
head access_log
```
We can see that one is, as expected, the great novel Moby Dick and a bunch of text we don't quite understand. We'll do some cool things with these files, but let's get started with something fairly straightforward.

### Opening Files
Generally, when working with a file in Python, you first have to open it and load it into memory. We can do this using the built-in `open` method:
```python
mobydick = open('mobydick')
type(mobydick)
dir(mobydick)
```
As we can see from the output of our `dir` method, there's quite a lot we can do with out file. For now, we're going to go ahead and close and reopen it.
```python
mobydick.close()
```
It's generally good practice to close your files once you're done with them. We want to make sure that we don't do anything stupid with our file while we're working with it, so we're going to go ahead and open it in read-only mode:
```python
mobydick = open('mobydick', 'r')
```
You can open files in several different modes, depending on what you want to do with them:
* `r` = read-only: cannot modify file, can only read in
* `w` = write-only: overwrites all contents in file
* `rw` = read-write: can read and write to file
* `a` = append: appends onto file, useful if don't want to overwrite past contents
Cool, so we've got an open file, so let's go ahead and do something with it.

## File Methods
Let's first go ahead and run find a way to store all the lines within our file:
```python
lines = mobydick.readline()
```
The `readlines` method simply breaks the file up into lines and returns a list of lines. Let's take a look to make sure this is the case.
```python
len(lines)
lines[1]
```
Awesome. We've now got a super-straightforward list of lines. Let's go ahead and run through these.
```python
for line in lines:
    print len(lines)
```
Cool, let's go ahead and write a quick script that finds the length of the longest line in the file:
```python
def find_longest_line(file_obj):
    lines = file_obj.readlines()
    long_len = 0
    for line in lines:
    	if len(line) > long_len:
	   long_len = len(line)
    return long_len

def main():
    mobydick = open('mobydick.txt', 'r')
    longest_line = find_longest_line(mobydick)
    print 'The longest line in this text is ' + str(longest_line)
    mobydick.close()

if __name__ == '__main__':
   main()
```
All of this should more or less make sense. Just a quick note about the last bit:
```python
if __name__ == '__main__':
   main()
```
Before, we've been putting our entry methods onto the top level of our script. Previously, our script would look like this:
```python
def find_longest_line(file_obj):
    lines = file_obj.readlines()
    long_len = 0
    for line in lines:
    	if len(line) > long_len:
	   long_len = len(line)
    return long_len


mobydick = open('mobydick.txt', 'r')
longest_line = find_longest_line(mobydick)
print 'The longest line in this text is ' + str(longest_line)
mobydick.close()
```

## String Methods
Very cool, so we've just found the longest line. We can now
## Regular Expressions
## 