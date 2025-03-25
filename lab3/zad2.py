import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=292653)

x_train = train_set[:, :-1]
y_train = train_set[:, -1]
x_test = test_set[:, :-1]
y_test = test_set[:, -1]

clf = tree.DecisionTreeClassifier()
clf.fit(x_train, y_train)
# tree.plot_tree(clf)
# plt.show()
predicted = clf.predict(x_test)
len = len(predicted)
good_predictions = 0
for i in range (len):
    if predicted[i] == test_set[i][4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/len*100, "%")

# cm = confusion_matrix(y_test, predicted, labels=np.unique(y_train))

# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_train))
# disp.plot(cmap="Blues", values_format="d")
# plt.title("Macierz błędów")
# plt.show()