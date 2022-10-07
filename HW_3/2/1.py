from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
iris = sns.load_dataset('iris')
print(iris)
X_train,X_test,y_train,y_test=train_test_split(iris.iloc[:, :-1],iris.iloc[:,-1],test_size =0.15)
X_train.shape,X_test.shape,y_train.shape,y_test.shape
X_train.head()
y_train.head()
def kn(a):
    plt.figure(figsize=(20, 7))
    model = KNeighborsClassifier(n_neighbors=a)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    plt.subplot(121)
    sns.scatterplot(data=iris, x='petal_width', y='petal_length', hue='species', s=50)
    plt.xlabel('Длина лепестка, см')
    plt.ylabel('Ширина лепестка, см')
    plt.legend()
    plt.grid()

    for i in range(len(y_test)):
        if np.array(y_test)[i]!=y_pred[i]:
            plt.scatter(X_test.iloc[i,3],X_test.iloc[i,2],color='red',s=150)
    print(f'accuracy:{accuracy_score(y_test,y_pred):.3}')
    plt.show()
kn(1)
kn(5)
kn(10)
