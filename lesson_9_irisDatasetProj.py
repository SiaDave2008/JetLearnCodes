import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv("/Users/sia/Downloads/iris.csv")
print(data)

data["species"] = data["species"].replace({"setosa":0, "versicolor":1, "virginica":2})
print(data)

plt.subplot(221)
plt.scatter(data["petal_length"], data["species"], s = 10, c = "g", marker = "o")

plt.subplot(222)
plt.scatter(data["petal_width"], data["species"], s = 10, c = "r", marker = "o")

plt.subplot(223)
plt.scatter(data["sepal_width"], data["species"], s = 10, c = "b", marker = "o")

plt.subplot(224)
plt.scatter(data["sepal_length"], data["species"], s = 10, c = "c", marker = "o")

plt.show()