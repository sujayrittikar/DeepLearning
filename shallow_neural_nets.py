import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Importing the Tensorflow library and the MNIST Fashion Dataset

import tensorflow as tf
fashion = tf.keras.datasets.fashion_mnist

# Getting the train and test datasets using .load_data() method
(x_train, Y_train), (x_test, Y_test) = fashion.load_data()

# Checking the shapes
print(f"x_train shape: {x_train.shape}")
print(f"Y_train shape: {Y_train.shape}")
print(f"x_test shape: {x_test.shape}")
print(f"Y_test shape: {x_test.shape}")

# Checking the shape of a single row in Training data, since the data is of images, since we have tensor data

print(x_train[0].shape)

# We observe the intensity matrix values between 0-255
import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()

# Scaling and Training data between 0 and 1
x_train = x_train/255.0
x_test = x_test/255.0

# Convert multi-dimensional array of intensities to a 1D array
x_train = x_train.reshape((60000, 784))
x_test = x_test.reshape((10000, 784))

# One-hot encoding the output data to make it easier for us to interpret the output generated by our training set as particular digits.

Y_train = tf.keras.utils.to_categorical(Y_train)
Y_test = tf.keras.utils.to_categorical(Y_test)

# Building our Shallow Neural Network Model with a sequential layers container to add layers to it.

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=(784, )))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
print(model.summary())

# Here, we've used only 1 hidden layer of dimension 128.

# Setting the optimizer and loss function for the model.
'''
		* Stochastic gradient descent as optimizer -> better performance than normal gradient descent
		* loss -> Categorical cross entropy as we are working on categorical data
'''
print("Building and fitting the model.........")
model.compile(optimizer='sgd', loss=tf.keras.losses.categorical_crossentropy, metrics=['acc'])

# Fitting the model on data
fitted = model.fit(x_train, Y_train, epochs=10, batch_size=10, validation_split=0.2)
print("Model built and fitted!")
print(model.predict(x_test))

# Evaluating the model on Test set
print("Evaluating the model...")
print(model.evaluate(x_test, Y_test, batch_size=10))

# Plotting our Model's Accuracy
print("Plotting the Model Accuracy...")
plt.plot(fitted.history['acc'])
plt.plot(fitted.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'])
plt.show()
# Plotting our Model's Loss
print("Plotting the Model Loss...")
plt.plot(fitted.history['loss'])
plt.plot(fitted.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'])
plt.show()

# While the current neural network model has a good accuracy, let's try the same with an additional hidden layer, forming DNN with 2 hidden layers.

# Let's try a NN model with another hidden layer
print("Building and fitting a model with another hidden layer...")
model_ = tf.keras.models.Sequential()
model_.add(tf.keras.layers.InputLayer(input_shape=(784, )))
model_.add(tf.keras.layers.Dense(128, activation='relu'))
model_.add(tf.keras.layers.Dense(64, activation='relu'))
model_.add(tf.keras.layers.Dense(10, activation='softmax'))
print(model_.summary())

model_.compile(optimizer='sgd', loss=tf.keras.losses.categorical_crossentropy, metrics=['acc'])

# Fitting the formed model
fitted_ = model_.fit(x_train, Y_train, epochs=10, batch_size=10, validation_split=0.2)
print("Model built and fitted to data")

# Predictions
print("Predictions: ")
print(model_.predict(x_test))

# Evaluate
print("Evaluating the model...")
print(model_.evaluate(x_test, Y_test, batch_size=10))

# Plotting the Accuracy and Loss
print("Plotting the accuracy...")
plt.plot(fitted_.history['acc'])
plt.plot(fitted_.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'])
plt.show()

print("Plotting the loss...")
plt.plot(fitted_.history['loss'])
plt.plot(fitted_.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'])
plt.show()

# Both the models have similar results but, adding more hidden layer slightly improves the performance in terms of smoothness of training, when we compare the model accuracy and loss for both models.

