import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

EPOCHS = 15
BATCH_SIZE = 100
NUMBER_OF_CLASSES = 10

def buildModel():
	model = Sequential()
	model.add(Dense(512, input_shape=(784,)))
	model.add(Activation('relu'))
	model.add(Dropout(0.2))

	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.2))

	model.add(Dense(10))
	model.add(Activation('softmax'))
	return model

def main():
	(X_train, y_train), (X_test, y_test) = mnist.load_data()
	print("X train shape\t\t\t:\t", X_train.shape)
	print("y train shape\t\t\t:\t", y_train.shape)
	print("X test shape\t\t\t:\t", X_test.shape)
	print("y test shape\t\t\t:\t", y_test.shape)

	# Viewing 9 random Images
	for i in range(9):
		plt.subplot(3, 3, i + 1)
		plt.tight_layout()
		imageNumber = random.randint(0, 60000)
		plt.imshow(X_train[imageNumber], cmap='gray', interpolation='none')
		plt.title("Digit: {}".format(y_train[imageNumber]))
		plt.xticks([])
		plt.yticks([])
	plt.show()

	X_train = X_train.reshape(60000, 784)
	X_test = X_test.reshape(10000, 784)
	X_train = X_train.astype('float32')
	X_test = X_test.astype('float32')
	X_train /= 255
	X_test /= 255

	print("Shape before one-hot encoding\t:\t", y_train.shape)
	Y_train = np_utils.to_categorical(y_train, NUMBER_OF_CLASSES)
	Y_test = np_utils.to_categorical(y_test, NUMBER_OF_CLASSES)
	print("Shape after one-hot encoding\t:\t", Y_train.shape)

	model = buildModel()
	model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
	model = model.fit(X_train, Y_train,
		batch_size=BATCH_SIZE, epochs=EPOCHS,
		verbose=1,
		validation_data=(X_test, Y_test))

	plt.subplot(2, 1, 1)
	plt.plot(model.history['acc'])
	plt.plot(model.history['val_acc'])
	plt.title('Model Accuracy')
	plt.ylabel('Accuracy')
	plt.xlabel('Epoch')
	plt.legend(['Train', 'Test'], loc='lower right')

	plt.subplot(2, 1, 2)
	plt.plot(model.history['loss'])
	plt.plot(model.history['val_loss'])
	plt.title('Model Loss')
	plt.ylabel('Loss')
	plt.xlabel('Epoch')
	plt.legend(['Train', 'Test'], loc='upper right')

	plt.tight_layout()
	plt.savefig('../Images/ModelPerformance.png')
	plt.show()

if __name__ == '__main__':
	main()