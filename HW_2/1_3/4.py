import numpy as np
a=np.ones((5,5))
a[1:4:,1:4:] = 0
print(a)