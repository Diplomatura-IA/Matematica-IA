import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Life Expectancy Data.csv")
print(data.shape)
print(data.head())

data2=data.query("Year == 2014")
data2=data2.query("GDP < 80000")
data2=data2.query("`percentage expenditure` != 0")
data2 = data2.loc[:,["Country","percentage expenditure","GDP"]]
print(data2.shape)
print(data2.head())


gasto = data2.loc[:,"percentage expenditure"]
pbi = data2.loc[:,"GDP"]
plt.scatter(pbi,gasto)
plt.show()
