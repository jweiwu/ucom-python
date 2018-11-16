import pandas
from matplotlib import pyplot as plt, rc

data1 = pandas.read_csv('.\\data\\data86.csv', skiprows=4,
                        index_col='Country Name')
print data1.shape
print data1.head()
print data1.columns
mean1960 = data1['1960'].mean()
print mean1960
data1['combined'] = data1['1960'] + data1['1961']
print data1.columns
# pip install openpyxl
data1.to_excel(".\\data\\lab86.xlsx",
               sheet_name="population_from_worldbank")
