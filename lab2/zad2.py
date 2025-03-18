from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')
print(X.head())
pca_iris = PCA(n_components=2).fit(iris.data)
print(pca_iris)
print(pca_iris.explained_variance_ratio_)
print(pca_iris.components_)
df = pca_iris.transform(iris.data)

x_setosa, y_setosa = zip(*df[0:49])
x_versicolor, y_versicolor = zip(*df[50:99])
x_virginica, y_virginica = zip(*df[-50:-1])
plt.scatter(x_setosa, y_setosa, label='Setosa', color='blue', marker='o')
plt.scatter(x_versicolor, y_versicolor, label='Versicolor', color='cyan', marker='o')
plt.scatter(x_virginica, y_virginica, label='Virginica', color='orange', marker='o')
plt.title('PCA of IRIS dataset')

plt.grid(True)
plt.legend()
plt.show()