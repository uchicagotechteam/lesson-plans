# Working with Text Files
Today we're going to be talking about working with files in Python. Files are the bread and butter of data science: you'll be working with them all the time, in various formats, so its best to go ahead and learn the basics. 

## Opening files
Generally, when working with a file in Python, you first have to open it and load it into memory. We can do this using the built-in `open` method:

```python
Jakubs_Favorite_Book = open('mobydick.txt', 'r')
f = open('mobydick.txt')
```
The open method takes two arguments.  The first argument is the name of the file to be opened, and the second argument is the mode
 that we want to open the file in.  The two main modes that we will be working in are `'r'` and `'w'`, which stand for read mode 
and write mode, repsectively. There is also an `'r+'` mode that allows one to both read and write. 

## File Methods
There are a number of methods to use on files that are important to know.  The first method we will go over is the read method.

```python
Moby_Dick = f.read()
```
The read method gives the text of the file as a string.  There is an optional argument that one can give to the read function
called 'size' that limits how large of a file can be read.  This argument can be important if you are working with very large files.
The number given is the number of bytes that are read.

Another way to read a file is by going line by line.  

```python
A_Line_From_Moby_Dick = f.readline
Moby_Dick_Lines = f.readlines()
```
The first method, `readline`, will give us one line from the text file.  The second method, `readlines`, will give us a
list of every line from the file as a string.  Because this is a list, we can use any of the list operations that we already know
on this list.  For instance:

```python
f.readlines()[47]
for line in f.readlines()
	if "cetology" in line:
		print line
```


## String Methods
Now that we know how to get strings of text from a file, it is time for us to learn more about string methods.  Notice above how
we used the `for`  `in` construction on a string.  That is because we can often treat strings as lists of characters.  For instance

```python
"Call me Jakub"[8]
"Olivia Myszkowski"[7:]
"I very much enjoyed reading this book."[2:27]
```

The first example will return the eighth character in the given string, remembering that counting starts at 0.  
The second example will return the the seventh character in the string and those after it.
The third example will return those characters that occur between the given indices.  

We have already seen some other operations we can do with strings, like 

```python
"Call " + "Me"
"Maybe" * 7
```

but we haven't seen many methods for strings yet.

The first methods we will go over will be about cases.

```python
sentence = "heLlO eRiN.  iT iS gOoD To SeE yOu."
sentence.capitalize()
sentence.lower()
sentence.upper()
```

The `capitalize` method gave us the same string, but with the first letter capitalized, the `lower` method gave us
the same string but with every letter lowercase, and the `upper` method gave us the same string but with every letter uppercase.

Another method that we can use on strings is the `strip` method.  We can use `strip` to remove certain letters from
the beginning or end of a given string.

```python
author = "Herman Melville"
author.lstrip('her')
author.lstrip('Her')
author.rstrip('el')
author.strip('Herl')
```

Another method to use on strings is split.  The split method will give us a list of the words in a string that are separated by
some specified delimiter string. 

```python
a_string = "material consisting of threads of cotton, hemp, or other material twisted together to form a thin length."
a_string.split()
``` 

The last two string methods we will go over are `replace` and `count`, though there are many 
more methods that are possible to use on strings.  `replace` takes two arguments and replaces all 
occurrences of the first string given with that of the second string given.

```python
whale = "I just saw a whale.  Have you ever seen a whale?  I really like whales.  Do you like whales?"
whale.replace('whale', 'quagga')
```

`count` returns the number of times a given substring occurs in a string.
```python
f.read().count(whale)
```

## Regular Expressions


## Creating a Dictionary

We will now use some code that Jakub made for us last year to create a dictionary that contains every
word in Moby Dick.  This task is a little bit daunting, but it almost entirely uses concepts
that we have covered

```python
import string

def read_file():
    f = open("mobydick.txt", 'r')
    # declaring new dictionary
    word_list = {}
    for line in f.readlines():
        for word in line.split():
            print word
            lower_word = word.lower()
            # declaring new list
            processed_word = []
            for letter in lower_word:
                if letter in string.ascii_lowercase:
                    print letter
                    processed_word.append(letter)
            print processed_word
            processed_word = ''.join(processed_word)
            print processed_word
            # have we seen this word already?
            if processed_word in word_list:
                word_list[processed_word] += 1
            else:
                word_list[processed_word] = 1
    return word_list

def main():
    word_list = read_file()
    print word_list

if __name__ == "__main__":
    main()
```