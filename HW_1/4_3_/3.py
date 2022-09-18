import matplotlib.pyplot as plt
import math as m
import numpy as np
from numpy import trapz
x=np.arange(0.0,10,0.1)
y=np.abs(np.cos(x*m.e**(np.cos(x)+np.log(x+1))))
plt.grid()
plt.plot(x,y,c="r")
plt.fill_between(x,y)
area=trapz(y)
print(area)
plt.show()