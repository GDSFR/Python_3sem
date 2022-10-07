import numpy as np
import matplotlib.pyplot as plt
def Evc(v1,v2):
    return np.linalg.norm(v1-v2)
def Cheb(v1,v2):
    return np.linalg.norm(v1-v2,ord=np.inf)
def Hem(v1,v2):
    return np.linalg.norm(v1-v2,ord=1)
def Set(a):
    arr=np.array([[],[]])
    for i in range(a):
        x=np.random.rand(1)
        y=np.random.rand(1)
        z=np.random.rand(1)
        ax.scatter(x,y,z)
        arr=np.append(arr,[x,y,z])
    arr = np.resize(arr, [a,3])
    print(arr)
    return arr
def Dist(arr,a):
    for i in range(a):
        print('\n',i+1,':','Evc------------------Cheb-------------------Hem---------------',)
        for j in range(a):
            print('       ',Evc(arr[i],arr[j]),'   ',Cheb(arr[i],arr[j]),'   ',Hem(arr[i],arr[j]))
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
a=4
arr=Set(a)
Dist(arr,a)
plt.show()
