import pandas as pd

url = 'https://raw.githubusercontent.com/RamiKrispin/coronavirus-csv/master/coronavirus_dataset.csv'
dataframe = pd.read_csv(url)
print(dataframe.head(5))
