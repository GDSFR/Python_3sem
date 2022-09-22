import pandas as pd
a=pd.Series([1,2,3,4,5,6])
b=pd.Series([1,2,3,4,5,6])
c=sum(((a-b)**2)**0.5)
print(c)