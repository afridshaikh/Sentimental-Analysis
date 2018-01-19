import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K



image_width = 150
image_height = 150


nb_train_img = 250
nb_validation_img = 50
batch_size = 25
epochs = 10

train_data_path = 'data/train/'
validation_data_path = 'data/validation/'

if K.image_data_format() == 'channels_first':
	input_shape = (3, image_width, image_height)
else:
	input_shape = (image_width, image_height, 3)

train_data_gen = ImageDataGenerator(
		rescale=1./255,
		rotation_range=40,
		shear_range=0.2,
		zoom_range=0.2,
		horizontal_flip=True)

validation_data_gen = ImageDataGenerator(
		rescale=1./255)


train_data_generator = train_data_gen.flow_from_directory(
		train_data_path,
		target_size= (image_width, image_height),
		batch_size = batch_size,
		class_mode='categorical')

validation_data_generator = validation_data_gen.flow_from_directory(
		validation_data_path,
		target_size= (image_width, image_height),
		batch_size = batch_size,
		class_mode='categorical')

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('softmax'))


model.compile(
		loss='categorical_crossentropy',
		optimizer='adam',
		metrics=['accuracy']
	)


model.fit_generator(
		train_data_generator,
		validation_data = validation_data_generator,
		epochs = epochs,
		steps_per_epoch = nb_train_img // batch_size,
		validation_steps = nb_validation_img // batch_size
	)



model.save('models/CheckAccuracy_model_10_epochs_2Classes.h5')
model.save_weights('weights.h5')