import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History
from tensorflow.keras.callbacks import ModelCheckpoint

# Load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess data
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
original_test_labels = np.argmax(test_labels, axis=1) # Save original labels for confusion matrix
print("oryginał", original_test_labels)

# Define model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

checkpoint = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', save_best_only=True, verbose=1)
# Train model
history = History()
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2,
callbacks=[checkpoint, history])

# Evaluate on test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

# Predict on test images
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Confusion matrix
cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Plotting training and validation accuracy
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

# Plotting training and validation loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.tight_layout()
plt.show()

# Display 25 images from the test set with their predicted labels
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(predicted_labels[i])
plt.show()

#a) reshape dodaje kanał głębokości, żeby dane miały taki format jakiego oczekuje warstwa Conv2D; (60000, 28, 28) → (60000, 28, 28, 1)
#to_categorical - oryginalne etykiety to liczby 0–9, to_categorical zamienia je na one-hot encoding
#argmax - zwraca index największego elementu, czyli przywraca one-hot do normalnych danych

#b) Conv2D - (32, (3, 3)) dla (28, 28, 1) -> (28 - 3 + 1, 28 - 3 + 1, 32) -> (26, 26, 32)
#MaxPooling2D - (2, 2) dla (26, 26, 32) -> dzieli na 2x2 bloki -> (13, 13, 32)
#Flatten() -> spłaszcza do 1D -> (13, 13, 32) -> 13 * 13 * 32 -> 5408
#Dense(64, activation='relu') -> 64 neuronów wyjściowych -> 64 neurony z różnymi cechami określającymi cyfry
#Dense(10, activation='softmax') -> warstwa klasyfikacyjna, połączenie 64 neuronów cech cyfr w 10 neuronów za każdą liczbę od 0 do 9

#c) najczęściej mylona cyfra 5 - z 8, 6 i 3. najczęściej mylone z sobą cyfry to 7 z 2

#d) pod koniec dokładność walidacyjna przestaje rosnąć co może sugerować przeuczenie

#e) z dodaniem checkpoint do modelu 2 nie jest tak często mylona z 7 ale 3 z 5 jest częściej mylona