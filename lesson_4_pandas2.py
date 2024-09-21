import pandas as pd

data = pd.read_csv("/Users/sia/Downloads/titanic.csv")

#Conditional to get colums 
a = data.loc[data['Age'] > 18, "Name"]
print(a)

#Index to get columns, i - index
b = data.iloc[9:25, 2:5]
print(b)

c = data.iloc[5, 2]
print(c)

data.iloc[4, 2] = "Sia"
print(data["Name"])

data.to_csv("changed_data.csv")
data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * 2
print(data.head())

d_rename = data.rename(columns = {
    "Pclass" : "Passenger_Class", 
    "Siblings/Spouses Aboard" : "Siblings Aboard"
})

print(d_rename.info())

print("The avg age is: ", data["Age"].mean())
print("The avg age/fare is: ", data[["Age", "Fare", "Test"]].mean())

print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"],
}))

print(data.agg({
    "Test": ["min", "max"],
    "Test2": ["max", "median"],
}))

print(data[["Sex", "Age"]].groupby("Sex").mean())
print(data.groupby("Sex")["Age"].mean())

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

print(data["Pclass"].value_counts())
print(data.groupby("Pclass")["Pclass"].count())

data.sort_values(by = "Age")
print(data[["Name", "Age"]].head())

data.sort_values(by = ["Pclass", "Age"], ascending = False)
print(data[["Age"]].head())

print(data.info())

data["Name lowercase"] = data["Name"].str.lower()
print(data["Name lowercase"].head())

print(data["Name"].str.split(","))

data["Surname"] = data["Name"].str.split(",").str.get(1)
print(data["Surname"])

data["gender_code"] = data["Sex"].replace({
    "male":"M",
    "female":"F"
})

print(data[["gender_code", "Sex"]])

#HW: 
# Find the mean fare of passengers wrt sex and pclass like (Male 1st Class Passenger). 
# Do this for all possible combinations - Total 6 combinations.

print("The Mean Age Fare of Passenger with Regards to Sex and Pclass: \n")

maleFirstClass = data[(data["Pclass"] == 1) & (data["Sex"] == "male")]
print("Male First Class: ", maleFirstClass["Fare"].mean())
print(maleFirstClass)

femaleFirstClass = data[(data["Pclass"] == 1) & (data["Sex"] == "female")]
print("Female First Class: ", femaleFirstClass["Fare"].mean())
print(femaleFirstClass)

maleSecondClass = data[(data["Pclass"] == 2) & (data["Sex"] == "male")]
print("Male Second Class: ", maleSecondClass["Fare"].mean())
print(maleSecondClass)

femaleSecondClass = data[(data["Pclass"] == 2) & (data["Sex"] == "female")]
print("Female Second Class: ", femaleSecondClass["Fare"].mean())
print(femaleSecondClass)

maleThirdClass = data[(data["Pclass"] == 3) & (data["Sex"] == "male")]
print("Male Third Class: ", maleThirdClass["Fare"].mean())
print(maleThirdClass)

femaleThirdClass = data[(data["Pclass"] == 3) & (data["Sex"] == "female")]
print("Female Third Class: ", femaleThirdClass["Fare"].mean())
print(femaleThirdClass)

# Find the median / mean age of passengers who died wrt sex.

print("The Mean / Median Age of Passenger with Regards to Sex and Survived: \n")

female = data[(data["Survived"] == 0) & (data["Sex"] == "female")]
print("Females Median: ", female["Fare"].median())
print("Females Mean: ", female["Fare"].mean())
print(female)

male = data[(data["Survived"] == 0) & (data["Sex"] == "male")]
print("Males Median: ", male["Fare"].median())
print("Males Mean: ", male["Fare"].mean())
print(male)