# CSV Files
CSV stands for comma separated value.  A CSV file consists of rows of data, where each row 
contains a few values separated by a comma. It is the most common import and export format
 for spreadsheets and databases.  
 
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
 that we want to open the file in.  The main mode that we will be working in is `'r'`, which stands for read mode. There is also a
  `'w'` mode that allows one to write. 

## Using Pandas
When we were looking at text files, we used the `read` method to store the contents of a 
file as a string.

```python
Moby_Dick = f.read()
```
If you don't have `pandas`, it is easy to install.

*in the shell:*
```shell
$ sudo easy-install pip
$pip install pandas
```

Since a CSV file is a list of rows of lists, it would be easier if we could read these files
in a format more fit for data.  One way to do this is with the `pandas` library.  This library is one of the most useful tools
for data analysis and makes reading a CSV file significantly easier.

```python
import pandas as pd

salaries = pd.read_csv('EmployeeSalaries.csv')
```

Using the `read_csv` method, we were able to store the file.  Now when we call `salaries`, we will 
be able to look at this file.

As we can see when we call `salaries`, however, some of the headers of the CSV file are very long.
This will make it inconvenient to type them in repeatedly.  For this reason, we will change these 
headers.

```python
salaries.rename(columns={'Employee Annual Salary': 'Salary', 'Position Title': 'Position'}, inplace=True)
```

Next, we can look at the individual salaries presented in this data set by calling `salaries['Salary']`.
We can try to find some statistics about this data `salaries['Salary'].max()`, but we run into some problems.
The value that is returned is clearly not the maximum salary.  This is because the data in the salary column
is currently written as strings with a '$' in front of them.  We will now remove the dollar sign and change the
type of the data into float.

```python
salaries['Salary'] = salaries['Salary'].map(lambda x: x.lstrip('$'))
salaries['Salary'] = salaries['Salary'].map(lambda x: float(x))
```
We can now look at some real statistics about these salaries.

```python
salaries['Salary'].max()
salaries['Salary'].min()
salaries['Salary'].mean()
salaries['Salary'].std()
```

This is useful information, but it does not tell us much about the specifics of the data.  We might want to
look closer at some of the groupings of the data, and organize the statistics we find around, say, the departments.

```python
by_dept = salaries.groupby('Department')
```

We now have the values in this data set organized together by department, but when we call `by_dept`, nothing
much seems to happen.  Similarly, if we try to look at the salaries by calling `by_dept['Salary']`, nothing much
seems to happen.  However, we can try the methods we used before.

```python
by_dept['Salary'].mean()
by_dept['Salary'].max()
by_dept['Salary'].min()
by_dept['Salary'].std()
```

We can also try some other methods.

```python
by_dept['Salary'].describe()
by_dept['Salary'].median()
```
We notice that sometimes, not all of the data is shown.  If we want to see all the data in the table, 
we can iterate over it, just as we would a list.
```python
for name, group in by_dept:
    print(name)
    print(group)
```

Iterating of the data in this way is important, because it allows us to access the data and store it in
other places, like dictionaries.

We will now create two more groups to look at.

```python
by_posn = salaries.groupby('Position')
by_posn2 = salaries.groupby(['Department', 'Position'])
```

The first grouping organizes by position, while the second one uses two heading to organize the data.  Let's
take a look at what these look like.

```python
for name, group in by_posn2:
	print(name)
	print(group)
```

Again, this gives us more than we need, so let's try to make this a little more readable.

```python
for name, group in by_posn2:
    print(name)
    print(group['Salary'].mean())
    print(group['Salary'].std())
```

We can now look at this data for everyone, and if we wanted to, we could store this data to a dictionary
to make it even easier to go through.
