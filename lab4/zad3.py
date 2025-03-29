import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
df = pd.read_csv("diabetes 1.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=292653)
train_data = train_set[:, :-1]
train_labels = train_set[:, -1]
test_data = test_set[:, :-1]
test_labels = test_set[:, -1]

train_labels = list(map(lambda x: 1 if x == 'tested_positive' else 0, train_labels))
test_labels = list(map(lambda x: 1 if x == 'tested_positive' else 0, test_labels))

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

mlp = MLPClassifier(hidden_layer_sizes=(3,), activation="relu", max_iter=500)
mlp.fit(train_data, train_labels)

print("jeden")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

cm = confusion_matrix(test_labels, predictions_test, labels=np.unique(train_labels))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(train_labels))
disp.plot(cmap="Blues", values_format="d")
plt.title("Macierz błędów")
plt.show()

mlp = MLPClassifier(hidden_layer_sizes=(6,), activation="relu", max_iter=500)
mlp.fit(train_data, train_labels)

print("dwa")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

cm = confusion_matrix(test_labels, predictions_test, labels=np.unique(train_labels))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(train_labels))
disp.plot(cmap="Blues", values_format="d")
plt.title("Macierz błędów")
plt.show()

mlp = MLPClassifier(hidden_layer_sizes=(3,3,), activation="relu", max_iter=500)
mlp.fit(train_data, train_labels)

print("trzy")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

cm = confusion_matrix(test_labels, predictions_test, labels=np.unique(train_labels))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(train_labels))
disp.plot(cmap="Blues", values_format="d")
plt.title("Macierz błędów")
plt.show()

mlp = MLPClassifier(hidden_layer_sizes=(3,), activation="tanh", max_iter=500)
mlp.fit(train_data, train_labels)

print("cztery")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))

cm = confusion_matrix(test_labels, predictions_test, labels=np.unique(train_labels))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(train_labels))
disp.plot(cmap="Blues", values_format="d")
plt.title("Macierz błędów")
plt.show()

#Więcej jest błędów fn, fn jest gorsze, gdyż pacjenta może ominąć leczenie którego potrzebuje