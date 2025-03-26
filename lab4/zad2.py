import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()

datasets = train_test_split(iris.data, iris.target, train_size=0.7, random_state=292653)

train_data, test_data, train_labels, test_labels = datasets
# print(train_labels) #0 - setosa, 1 - versicolor, 2 - virginica

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

mlp = MLPClassifier(hidden_layer_sizes=(2,), activation="relu", max_iter=3000)
mlp.fit(train_data, train_labels)

print("jeden")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

mlp = MLPClassifier(hidden_layer_sizes=(3,), activation="relu", max_iter=3000)
mlp.fit(train_data, train_labels)

print("dwa")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

mlp = MLPClassifier(hidden_layer_sizes=(3,3,), activation="relu", max_iter=3000)
mlp.fit(train_data, train_labels)

print("trzy")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))





