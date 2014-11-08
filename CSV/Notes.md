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

Find maximum and minimum salary
```python
salaries['Salary'].max()
salaries['Salary'].min()
```