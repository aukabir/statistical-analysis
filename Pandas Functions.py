import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_excel("E:/1.1 MDSA/MDSA 502 Dr S.R/Assign_Data.xlsx");df 

# Show All Column Names
df.columns

# To check missing values
df.isnull().sum()

# Dropping duplicates
df.drop_duplicates(subset ="No.",)

# Drop any column
df.drop(columns='No')

# To show no of Rows in dataset
len(df)

# To check no of observation(not NULL) per Column/variable (by using direction 0)

df.count(0)

# To check no of observation(not NULL) per Row (by using direction 1)
df.count(1)

# Check difference 2 variable in a row 
df.query("Weight > IQ")

# creat a subset (0-10 Rows and 4-5 Columns)
df.iloc[:10, 3:5]

# Creating subset with specific rows and columns (Rows: 3,10,14,23; Columns: Age, Weight, IQ)
df.loc[[3, 10, 14, 23], ['Age', 'Weight', "IQ"]]

# To check data types
df.dtypes           #To check data types of all variables 
df.Age.dtypes       #To check data types of one variable

# To select variables of certain data types e.g; int64 or object
df.select_dtypes(include='int64')

# To exclude variables that do not have certain data types e.g; int64 or object
df.select_dtypes(exclude='int64')

# To create a new varibable 
random_col = np.random.randint(100, size=len(df));random_col

# inserts a column in the specified position e.g; third position
df.insert(3, 'random_col', random_col)
df.head()

# To creat a subset of n Rows from the main dataset
df.sample(n = 50)

# To creat a subset of 25% rows from the main dataset 
df.sample(frac = 0.25)

# To create a subset where values of any variable greater than a fixed value.
df['Age'].where(df['Age'] > 78)

# to create a subset based on category of categorical variables
Gender= ["M"]
male=df[df.Gender.isin(Gender)];male

# To find the unique values of Age column 
df.Age.unique()

# To find the no of unique values of Age column
df.Age.nunique()

# To find the no of unique values in whole dataset
df.nunique()

# Replace one unique value in a column (Replace 1 by 1.1)
df.replace(1.0, 1.1)

# Rename the Column/s
df.rename(columns = {"Age": "Age Group", "Wight": "Weighttttt"})

# Replace NAN values by zero value in a column
df['Age Group'].fillna(0, inplace=True)

# Replace NAN values by mean in a column
df['Age Group'].fillna(df['Age Group'].mean(), inplace = True)

# For Data Summarizing, group by one categorical variable 
df.groupby("Gender")['IQ'].sum()

# For Datasssssssssssssssss Summarizing, group by multiple categorical variable 
import numpy as np
df.groupby(['Gender', 'IQ'])['Age', 'Weight'].agg([np.mean, np.median])

# Cross tabulation of 2 variable
pd.crosstab(df['Gender'], df['Group'])

# Cross tabulation of 2 variable with Total 
pd.crosstab(df['Gender'], df['Group'], margins = True, margins_name="Total", normalize = True)

# Classify column data in 5 class
pd.qcut(df['IQ'], q = 5)
pd.qcut(df['IQ'], q = 5).value_counts()
# OR 
pd.cut(df['IQ'], bins = 5).value_counts()

# To get basic stat measures
df['IQ'].describe()

# To plot graph by column
df.plot('IQ')

# =============================================================================
# Visualization 
# =============================================================================
pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x = 'Gender' , data=df, plt.show()





