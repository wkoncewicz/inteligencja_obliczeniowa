import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))
# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3,
random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3,
# random_state=42)
# Define the model
model = Sequential([
Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
Dense(64, activation='relu'),
# Dense(3, activation='softmax')
Dense(y_encoded.shape[1], activation='softmax')
])
# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='RMSprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)
# history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=4)
# history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=16)
# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")
# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.tight_layout()
plt.show()
# Save the model
model.save('iris_model.h5')
# Plot and save the model architecture
# plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

#a) StandardScaler służy do normalizacji cech poprzez przekształcenie danych tak, aby miały zerową średnią i jednostkowe odchylenie standardowe.
#Normalizacja danych poprawia efektywność i stabilność trenowania modeli uczenia maszynowego.
#Pomaga unikać problemów z różnicami w skali wartości między cechami.

#b) One-hot encoding zamienia każdą kategorię na wektor, w którym tylko jedna wartość to 1, a reszta to 0.
# Setosa -> 0 -> [1, 0, 0]
# Versicolor -> 1 -> [0, 1, 0]
# Vigrinica -> 2 -> [0, 0, 1]
# Sieci neuronowe działają lepiej na kodowaniu one-hot niż na surowych etykietach numerycznych.
# Zapobiega to nadaniu liczbowym etykietom fałszywego porządku (np. że Virginica (2) jest „większa” niż Setosa (0)).

#c) X_train.shape[1] - liczba cech, czyli 4 - 4 neurony wejściowe
#y_encoded.shape[1] - liczba klas, czyli 3 - 3 neurony wyjściowe

#d) LeakyReLU jest lepszym modelem od klasycznego ReLU

#e) użycie SGD jako optymalizator daje znacząco gorsze wyniki
# użycie RMSprop jako optymalizator i sparse_categorical_crossentropy jako funkcję straty daje większą stratę i dobrą dokładność

#f) przy batch_size = 4 wykres jest bardziej zmienny i straty są większe i rosnące wraz z epokami
# przy batch_size = 16 wykres jest bardziej stabilny a straty są mniejsze niż przy batch_size = 4

#g) najlepsza wydajność jest osiągnięta między 40 a 100 epoką, gdzie dokładność na danych walidacyjnych jest stale najwyższa, z wyjątkami gdzie są małe dołki
# model nie jest ani przeuczony ani niedouczony


