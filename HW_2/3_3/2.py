import pandas as pd
from sklearn import preprocessing
url = pd.read_csv('https://raw.githubusercontent.com/akmand/datasets/master/iris.csv')
print(url.head(5))
ZScaler = preprocessing.StandardScaler()
MinMaxScaler = preprocessing.MinMaxScaler()
url['sepal_length_cm'] = MinMaxScaler.fit_transform(url[['sepal_length_cm']])
print(url.head(5))
url['sepal_width_cm'] = ZScaler.fit_transform(url[['sepal_width_cm']])
print(url.head(5))
