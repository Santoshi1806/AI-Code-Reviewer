import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os

# Streamlit UI Title
st.title("🐶🐍🐱 Animal Image Classifier")
st.write("Upload an image, and the model will classify it as a Cat, Dog, or Snake.")

# Set Image Parameters
img_height, img_width = 128, 128
batch_size = 16

data_dir = "C:\\Users\\saksh\\OneDrive\\Desktop\\Animals"  # Adjust path

datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)
val_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Load Pretrained MobileNetV2 Model
base_model = keras.applications.MobileNetV2(input_shape=(img_height, img_width, 3), include_top=False, weights='imagenet')
base_model.trainable = True
for layer in base_model.layers[:-20]:  # Freeze first 20 layers
    layer.trainable = False

# Define Model
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(3, activation='softmax')  # 3 classes (cat, dog, snake)
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train Model
epochs = 10
model.fit(
    train_data,
    validation_data=val_data,
    epochs=epochs
)

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")

    # Preprocess Image
    img = load_img(uploaded_file, target_size=(img_height, img_width))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for batch
    img_array = img_array / 255.0  # Normalize

    # Predict
    predictions = model.predict(img_array)
    class_labels = list(train_data.class_indices.keys())
    predicted_class = class_labels[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Show Prediction
    st.write(f"### 🏆 Prediction: {predicted_class.capitalize()} ({confidence:.2f}%)")
