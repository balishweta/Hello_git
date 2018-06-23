# #Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd
data = {'Name':['Shweta'],'Age':['36'],'Mail-id':['bali82.shweta@gmail.com'],'Phone-Number':['67676976969'] }
df = pd.DataFrame(data)
df.loc[1]=['Priyanka','32','priyanka.grover@gmail.com','35645382483']
print(df)

# 2.Download the dataset from this link ,Click Here
# Import the data and print the following :
# a.) First 5 rows of Dataframe
# b.) First 10 rows of the Dataframe
# c.) find basic statistics on the particular dataset.
# d.) Find the last 5 rows of the dataframe
# e.) Extract the 2nd column and find basic statistics on it.


import pandas as pd

df = pd.read_csv('dataset_pandas.csv', sep='\s*,\s*',
                           header=0, encoding='utf-8-sig', engine='python')
print(' First 5 rows of Dataframe')
print(df.head(5))

print('First 10 rows of the Dataframe')
print(df.head(10))

# print(' find basic statistics on the particular dataset')
# For numeric columns, describe() returns basic statistics: the value count, mean, standard deviation, minimum, maximum, and 25th, 50th, and 75th quantiles for the data in a column.
print(df['MinTemp'].describe())
# print(type(df))
# print(df.shape)
# print(df.dtypes)

# print(df.columns.tolist())

# Extract the 2nd column and find basic statistics on it.
print(df)
print(df.columns.tolist())

print(df['Location'].describe())


print('Find the last 5 rows of the dataframe')
print(df.tail(5))
