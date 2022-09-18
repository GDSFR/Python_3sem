import pandas as pd
import matplotlib.pyplot as plt
data_files =['Microsoft.csv','Google.csv','Apple.csv']
for file in data_files:
        df = pd.read_csv(file)
        x = list(range(1, len(df['Close']) + 1))
        y = df['Close']
        plt.grid()
        plt.plot(x,y,label=file.title())
plt.legend()
plt.show()