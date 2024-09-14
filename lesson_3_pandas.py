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

print(data.shape)
print(data.info())
print(data.describe())
print(data.dtypes)

name_age = data[["Name", "Age"]]
print(name_age.tail())
print(name_age.shape)

age = data[data["Age"] > 35]
print(age)
print(age.shape)

class2and3 = data[data["Pclass"].isin([2, 3])]
print(class2and3[["Name", "Pclass"]])

class2or3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class2or3[["Name", "Pclass"]].head())

maleFirstClass = data[(data["Pclass"] == 1) & (data["Sex"] == "male")]
print("The mean age of male first class passenger is: ", maleFirstClass["Fare"].mean())
print(maleFirstClass)

femaleSecondClass = data[(data["Pclass"] == 2) & (data["Sex"] == "female")]
print("The mean age for the female 2nd class is: ", femaleSecondClass["Fare"].mean())
print(femaleSecondClass)