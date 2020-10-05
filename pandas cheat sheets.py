# pandas cheat sheet

#[Data Wrangling with pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

'''
https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
'''

#____________________________________________________________________________________________
# Code Snippets

# Creating DataFrames from dictionary
import pandas as pd


df1 = pd.DataFrame(
    {"a":[4 ,5, 6],
     "b":[7, 8, 9],
     "c":[10, 11, 12]},
     index = [1, 2, 3])

# Creating DataFrames from list
df2 = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
     index=[1, 2, 3],
     columns=['a', 'b', 'c'])

import pandas as pd

list1 = ['tom', 'reacher', 25]
list2 = ['krish', 'pete', 30]
test = zip(list1, list2)
print(*test)

# List
lst = [['tom', 'reacher', 25], ['krish', 'pete', 30], 
       ['nick', 'wilson', 26], ['juli', 'williams', 22]] 
    
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'], dtype = float) 
display(df)


#Dictionary
dictionary = {
    "First_Name" :
    [
     "tom", "nick"
    ],
    "Second_Name" :
    [
     "pete", "williams"
    ],
    "Age" :
    [
     30,
     20
    ]
}

df_2 = pd.DataFrame(dictionary) 
display(df_2) 

# multi index dataframe
df3 = pd.DataFrame(
    {"a":[4 ,5, 6],
     "b":[7, 8, 9],
     "c":[10, 11, 12]},
     index = pd.MultiIndex.from_tuples(
             [('d',1),('d',2),('e',2)],
              names=['n','v']))

# Reshaping Data
df4 = pd.melt(df1, var_name='var', value_name='val')
df4.pivot(columns='var', values='val')
df5 = pd.concat([df1, df2], axis=1)

zip 
# Sorting, drop, rename
df1.sort_index(ascending=False)
df1.sort_values('a', ascending=False)
df1.drop(columns=['b', 'c'])
df1.rename(columns = {'a':'c1', 'b':'c2', 'c':'c3'})

# Subset Rows
df = pd.concat([df1, df2])
df.a >= 5  # return bool series
df[df.a >= 5]  # extract rows that meet logical criteria
df.drop_duplicates()  # remove duplicate rows
df.head(2)  # select first 2 rows
df.tail(2)  # select last 2 rows
df.sample(frac=0.5)  # randomly select fraction of rows
df.sample(n=3)  # randomly select n rows
df.iloc[2:4] # select rows by position
df.nlargest(3, 'b')  # select and order top 3 entries of column b
df.nsmallest(3, 'c') # select and order bottom 3 entries of column c

# Subset Columns
df.a
df['a']
df[['a', 'b']]
df.filter(regex='^b$') # slect columns whose name matches regex
df.loc[:, 'b':'c'] # select all columns between b and c
df.iloc[:, [1,2]]  # select columns in positions 1, 2 (first is 0)
df.loc[df['a'] > 5, 'b':'c']

# Summarize Data
df['a'].value_counts()
len(df)
df['a'].nunique()
df.describe()  # basic descriptive statistics for each column
df.sum()
df.count()
df.median()
df.quantile([0.25, 0.75, 0.90])
df.apply(sum)
df.min()
df.max()
df.mean()
df.var()
df.std()

# Handling Missing Data
foo = df4.pivot(columns='var', values='val')
foo.dropna()
foo.fillna(1)

# Make New Columns
df.assign(d=lambda df: df.a*df.b)  # Compute and append new columns
df['d'] = df.a*df.b  # Add single column

# Group Data


# Windows


# Plotting


# Combine Data Sets