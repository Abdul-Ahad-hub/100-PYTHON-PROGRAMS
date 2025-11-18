import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

model = Sequential([
    Dense(8, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=5, batch_size=8)

print(model.evaluate(X, y))
