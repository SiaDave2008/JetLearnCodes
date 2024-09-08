#Intro to Pandas:

# data structures
# data, rows, and colums
# a data frame - framworks/outline for data
# 2D, size-mutable, potentially heterogenous tabular data structured
# labeled axes (roaws and columns)
# outline/framwork for assesing and visulising data
# loading datasets from existing storage
# 

import pandas as pd

df = pd.DataFrame({"name":["sia", "ani", "mike"],
                    "age":[15, 45, 80],
                    "city":["dubai", "dehli", "new york"],
                    })
print(df)
print(df.shape)
print(df["name"])
print(df["age"].max())
print(df["age"].shape)
print(df.info())
print(df.dtypes)
print(df.describe())
data = pd.read_csv("/Users/sia/Downloads/titanic.csv")
print(data)
print(data.head())
print(data.tail())