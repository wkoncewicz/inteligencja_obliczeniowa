import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=292653)
x_test = test_set[:, :-1]
y_test = test_set[:, -1]
x_train = train_set[:, :-1]
y_train = train_set[:, -1]

for k in [3, 5, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    
    y_pred = knn.predict(x_test)
    
    accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"k-NN (k={k}) - Dokładność: {accuracy:.2f}%")
    cm = confusion_matrix(y_test, y_pred, labels=np.unique(y_train))

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_train))
    disp.plot(cmap="Blues", values_format="d")
    plt.title("Macierz błędów")
    plt.show()

model = GaussianNB()
model.fit(x_train, y_train)
predicted = model.predict(x_test)
accuracy = accuracy_score(y_test, predicted) * 100
print(f"Native Bayes - Dokładność: {accuracy:.2f}%")
cm = confusion_matrix(y_test, predicted, labels=np.unique(y_train))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_train))
disp.plot(cmap="Blues", values_format="d")
plt.title("Macierz błędów")
plt.show()


