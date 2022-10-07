import random
import numpy as np
import statistics
from matplotlib import pyplot as plt
lst=np.random.rand(15)
x=range(0,15,1)
print('Среднее',statistics.mean(lst))
print('Медианное',statistics.median(lst))
print(lst)
plt.scatter(x,lst,c='b')
plt.grid(c='black')
plt.show()