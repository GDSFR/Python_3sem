from _2 import dataframe
print(dataframe.head(3),dataframe.tail(4),dataframe.shape,'\n',dataframe.describe(),'\n',dataframe.iloc[1:6],'\n',dataframe[dataframe['Country.Region']=='Russia'])
