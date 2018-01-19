import glob
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

img_width, img_height = 150, 150
model = load_model('models/model_10_epochs_2Classes.h5')

for i in glob.glob('predict/test.jpg'):
	print(i)
	img = load_img(i, False, target_size=(img_width, img_height))
	x = img_to_array(img)
	x = np.expand_dims(x, axis=0)
	preds = model.predict_classes(x)
	print(preds)
	# probs = model.predict_proba(x)
	# print(probs)
	print('\n\n\n')