import matplotlib.pyplot as plt
import math as m
import numpy as np
x=np.arange(0,11,1)
y=np.sqrt(1+m.e**np.sqrt(x)+np.cos(x**2)/abs(1-np.sin(x)**3))
plt.grid()
plt.plot(x,y,c="g")
c=x[0:len(x)//2:1]
plt.grid()
y=np.sqrt(1+m.e**np.sqrt(c)+np.cos(c**2)/abs(1-np.sin(c)**3))
plt.scatter(c,y,c='r')
plt.show()