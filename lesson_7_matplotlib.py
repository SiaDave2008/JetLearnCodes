#Plot the bar graphs of total number of men and women in the titanic, 
# average fare of men and women, pie chart for the number of people of 
# different classes present. Titanic dataset should be interpreted to 
# complete this task.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/sia/Downloads/titanic.csv")

#Plot the bar graphs of total number of men and women in the titanic
'''
gender = data["Sex"].value_counts()
gender.plot(kind = "bar", color = ["r", "b"])
'''

#Average fare of men and women
'''
avg = data.groupby("Sex")["Fare"].mean()
avg.plot(kind = "bar", color = ["orange", "green"])

plt.xlabel("Gender")
plt.ylabel("Num of People")
plt.show()
'''


#Pie chart for the number of people of different classes present

classType = data["Pclass"].value_counts()
lab = ["C1", "C2", "C3 "]
col = ["c", "m", "r"]
classType.plot(kind = "pie", colors = col, labels = lab)
plt.title("Classes")
plt.show()