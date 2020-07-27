
# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os.path

if not os.path.isfile('my_model.h5'):
  mnist = keras.datasets.mnist

  (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

  class_names = ['0', '1', '2', '3', '4', '5', '6', '7 ', '8', '9']

  train_images = train_images / 255.0

  test_images = test_images / 255.0

  model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
  ])

  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  model.fit(train_images, train_labels, epochs=5)
  model.save('my_model.h5')
else:
  model = keras.models.load_model('my_model.h5')

def predict (image):
  img = np.array(image, dtype=float)
  img = img[:, :, 0]
  img = ((img / 255.0) -1) * -1

  plt.figure()
  plt.imshow(img)
  plt.colorbar()
  plt.grid(False)
  plt.show()

  predictions_single = model.predict(img.reshape(1,28,28))
  print(predictions_single)
  return np.argmax(predictions_single[0])
