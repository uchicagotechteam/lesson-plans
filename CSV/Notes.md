# Using Pandas
```python
import pandas as pd

salaries = pd.read_csv('EmployeeSalaries.csv')
```
Major problem: some headers are super-long

```python
salaries.rename(columns={'Employee Annual Salary': 'Salary', 'Position Title': 'Position'}, inplace=True)
```
Take '$' off salary column
```python
salaries['Salary'] = salaries['Salary'].map(lambda x: x.lstrip('$'))
```

Turn salary column into column of floats

```python
salaries['Salary'] = salaries['Salary'].map(lambda x: float(x))
```

Find maximum and minimum salary
```python
salaries['Salary'].max()
salaries['Salary'].min()
```

Grouping by Departments and Finding Values
```python
by_dept = salaries.groupby('Department')
by_posn = salaries.groupby(‘Position’)
by_posn2 = salaries.groupby(['Department', 'Position'])
by_dept[‘Salary’].describe()
by_dept[‘Salary’].mean()
by_dept[‘Salary’].max()
by_dept[‘Salary’].min()
by_dept[‘Salary’].std()
by_dept[‘Salary’].median
for name, group in by_posn2:
	print(name)
	print(group[‘Salary’].mean())
	print(group[‘Salary’].std())
```


