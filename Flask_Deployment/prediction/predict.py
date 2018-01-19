from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
from keras.preprocessing import image
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import glob


img_width,img_height = 150,150
model = load_model('..//model//model.h5')

for i in glob.glob('..//uploads/*.*'):
	img = load_img(i ,False,target_size=(img_width,img_height))
	x = img_to_array(img)
	x = np.expand_dims(x, axis=0)
	preds = model.predict_classes(x)
	print("\n\nOutput: ",preds,"  ",i,"\n\n")
	# probs = model.predict_proba(x)
	# print(probs)
