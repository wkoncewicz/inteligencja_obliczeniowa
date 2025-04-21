import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

# Step 1: Build DataFrame from image filenames
filenames = os.listdir('./dogs-cats-mini')
categories = ['dog' if name.startswith('dog') else 'cat' for name in filenames]

df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})

# Step 2: Split into train and validation
train_df, validate_df = train_test_split(df, test_size=0.2, random_state=42)
validate_df = validate_df.reset_index(drop=True)

# Step 3: Create ImageDataGenerator for validation (no shuffle!)
IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32

val_datagen = ImageDataGenerator(rescale=1./255)

val_generator = val_datagen.flow_from_dataframe(
    validate_df,
    './dogs-cats-mini',
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False  # Important for matching predictions with true labels
)

# Step 4: Load your model
model = load_model('model.h5')

# Step 5: Predict
preds = model.predict(val_generator)
pred_labels = np.argmax(preds, axis=1)
true_labels = val_generator.classes
class_names = list(val_generator.class_indices.keys())

# Step 6: Confusion Matrix
cm = confusion_matrix(true_labels, pred_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# Step 7: Classification Report
print(classification_report(true_labels, pred_labels, target_names=class_names))
