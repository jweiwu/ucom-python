import pandas
from matplotlib import pyplot as plt, rc

data1 = pandas.read_csv('.\\data\\data86.csv', skiprows=4,
                        index_col='Country Name')
usaData = data1[data1['Country Code'] == 'USA']
print usaData.shape
print usaData['2012'], usaData['2015']
print plt.style.available
font = {'family': 'Courier New'}
rc('font', **font)
plt.style.use('bmh')
usaData.plot(kind='bar', figsize=(12, 6),
             y=['1960', '1970', '1980', '1990', '2000'], fontsize=14)
plt.show()
