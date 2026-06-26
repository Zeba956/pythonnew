print("Hello AI")


#epochs 
#backpropagration



#25-06-2026
#Neural Learning
#Xor problem


import numpy as np

def sigmoid(x): return 1 / (1+np.exp(-x))
def sigmoid_d(x): return x * (1-x)

X = np.array ([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
W1 = np.random.randn(2,4) * 0.5
W2 = np.random.randn(4,1) * 0.5

lr = 0.5
losses = []

for epoch in range(10000):
    h = sigmoid(X @ W1)
    o = sigmoid(h @ W2)

    loss = np.mean((y-o)**2)
    losses.append(loss)

    d_o = (o-y) * sigmoid_d(o)
    d_h = (d_o @ W2.T) * sigmoid_d(h)


    W2 -= lr * h.T @ d_o
    W1 -= lr * X.T @ d_h

import matplotlib.pyplot as plt
plt.plot(losses); plt.title('Loss Decreasing During Training')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.show()


print('Final predictions (should be close to [0,1,1,0]):')
print(np.round(o,2))






import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt



# Keras ANN for Handwritten Digit Classification (MNIST)

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Build ANN model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=10,
    validation_split=0.2,
    verbose=1
)

# Evaluate model
test_loss, test_acc = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Test Accuracy: {test_acc*100:.2f}%")

# Plot training history
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(history.history['accuracy'], label='Train')
axes[0].plot(history.history['val_accuracy'], label='Validation')
axes[0].set_title('Accuracy')
axes[0].legend()

axes[1].plot(history.history['loss'], label='Train')
axes[1].plot(history.history['val_loss'], label='Validation')
axes[1].set_title('Loss')
axes[1].legend()

plt.tight_layout()
plt.show()

# Predictions on test images
predictions = model.predict(X_test[:15])
pred_classes = np.argmax(predictions, axis=1)

plt.figure(figsize=(15, 3))

for i in range(15):
    plt.subplot(3, 5, i + 1)
    plt.imshow(X_test[i], cmap='gray')

    correct = pred_classes[i] == y_test[i]

    plt.title(
        str(pred_classes[i]),
        color='green' if correct else 'red',
        fontsize=8
    )
    plt.axis('off')

plt.suptitle("Green = Correct, Red = Wrong")
plt.show()