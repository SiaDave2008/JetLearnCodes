import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("/Users/sia/Downloads/Data.csv")

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

#Calculating the mean value for the missing vals
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
#creating the inputs for the missing vals
imputer.fit(x[:,1:3])
#inputing the missing vals with the new calculated mean val
x[:,1:3] = imputer.transform(x[:,1:3])

ct = ColumnTransformer(transformers = [("encoder", OneHotEncoder(), [0])], remainder = "passthrough")
x = np.array(ct.fit_transform(x))

print(data)
print(x)
print(y)
print(data)

'''
#HW:
-----------------------
 Supervised Learning:
# labeled datasets to train algorithms to predict outcomes 
# and recognize patterns with input-output pairs provided. 
-----------------------
 Unsupervised Learning:
# unlabeled data to train algorithms to predict outcomes 
# and find hidden patterns or structures
-----------------------
 Classification:
# non-numerical data
# catogorical or class-based interpretation
-----------------------
 Regression:
# numerical data
# relationship between independent variables
# and dependent variable
'''