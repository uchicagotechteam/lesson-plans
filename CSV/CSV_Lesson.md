# CSV Files
CSV stands for comma separated value.  A CSV file consists of rows of data, where each row
 contains a few values separated by a comma.  
 
 ```CSV
 Tucholski,Jakub,Moby Dick
 Simpson,Erin,War and Peace
 Myszkowski,Olivia,One Hundred Years of Solitude
 ```
Each row in the CSV file will have the same number of values, and as we can see, each
position in each row should fit into the same category.  Today we will look at how to manipulate
the data in these files to make the information they contain more digestible.  That may not seem
useful in the example above, but CSV files can be much, much larger.


## Opening files
Recall how we opened files using the built-in `open` method:

```python
Jakubs_Favorite_Book = open('mobydick.txt', 'r')
f = open('mobydick.txt')
```
The open method takes two arguments.  The first argument is the name of the file to be opened, and the second argument is the mode
 that we want to open the file in.  The two main modes that we will be working in are `'r'` and `'w'`, which stand for read mode 
and write mode, repsectively. There is also an `'r+'` mode that allows one to both read and write. 

## CSV File Methods
When we were looking at text files, we used the `read` method to store the contents of a 
file as a string.

```python
Moby_Dick = f.read()
```

Since a CSV file is a list of rows of lists, it would be easier if we could read these files
as lists rather than strings.  One way to do this is with the `csv` module.

```python
import csv

f = open('file.csv')

csv_f = csv.reader(f)

f.close()
```

Using the `reader` method, we were able to store the file.  But what does the file we have stored
look like?

```python
for row in csv_f:
	print row
	
for row in csv_f:
	print row[2]
```

As we can see, each row is returned as a list, and we can go through these lists to find
the data that we want.

We can also access files to write to them with the `csv` module.

```python
import csv

f = open('file.csv', 'wb')

csv_f = csv.writer(f)
csv_f.writerow(['Smith','John','The Foot Book'])

f.close
```