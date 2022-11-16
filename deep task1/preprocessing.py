import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("F:\matrail\deep task1\penguins.csv")
print(data.shape)
columns = []
for i in range(0, 5):
    if i == 0:
        columns.append("target")
    columns.append("X" + str(i + 1))
data.columns = columns
print(data.isnull().sum())


data["X4"].fillna("male", inplace=True)

print(data.isnull().sum())

def convertx4_to_numerical(x):
    if x == "male":
        return 1
    elif x == "female":
        return 2

data["X4"] = data["X4"].apply(convertx4_to_numerical)

def convert_class(x):
    if x == "Adelie":
        return 1
    elif x == "Chinstrap":
        return 3
    elif x == "Gentoo":
        return 2

data["target"]=data["target"].apply(convert_class)
c1=data[0:50]
c2=data[50:100]
c3=data[100:]
def get_class(class_no):
    if class_no == 1:
        return c1
    elif class_no == 2:
        return c2
    elif class_no == 3:
        return c3

def plot_class(class_1,class_2,f1,f2):
  c_1=get_class(class_1)
  c_2=get_class(class_2)
  plt.scatter(c_1[f1],c_1[f2])
  plt.scatter(c_2[f1],c_2[f2])
  plt.xlabel(f1)
  plt.ylabel(f2)
  plt.legend(["class 1", "class2"])
  plt.show()
