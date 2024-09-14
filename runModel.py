# -*- coding: utf-8 -*-
"""runModel

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LHFmgDLetcGuBfcR3ReYIsclEZYpeMyw
"""

# Train the model
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=10  # You can adjust the number of epochs based on performance
)

# Evaluate the model on the validation set
loss, accuracy = model.evaluate(validation_data)
print(f"Validation Accuracy: {accuracy:.2f}")

# Visualize training graph and details
import matplotlib.pyplot as plt
import os

# Create a directory to save the models if it doesn't exist
os.makedirs('saved_models', exist_ok=True)

# Save the model as an H5 file
h5_path = os.path.join('saved_models', 'sentiment_model.h5')
model.save(h5_path)
print(f"Model saved as H5 file: {h5_path}")


# Save the model in Keras format
keras_path = os.path.join('saved_models', 'sentiment_model_keras.keras') # Added .keras extension
model.save(keras_path)
print(f"Model saved in Keras format: {keras_path}")

# Plot training & validation accuracy values
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.tight_layout()
plt.savefig('training_graphs.png')
plt.show()

print("Training graphs saved as 'training_graphs.png'")