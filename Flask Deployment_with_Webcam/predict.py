from keras.models import load_model # Tensorflow is the neural network library for the easing the process for making the neural network. Keras is the layer above tensorflow 
from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
from keras.preprocessing import image
import numpy as np
import h5py
from keras.preprocessing import image
#from keras.applications.vgg16 import preprocess_input
import glob 


img_width,img_height = 150,150
model = load_model('model/model_20_epochs_adadelta.h5')# loading the model.

def predict_sentimets():
	for i in glob.glob('uploads/*.*'):
		img = load_img(i ,False,target_size=(img_width,img_height))
		x = img_to_array(img)
		x = np.expand_dims(x, axis=0)
		preds = model.predict_classes(x)
		res = np.array_str(preds)
		return res
	
                #print("\n\nOutput: ",preds,"  ",i,"\n\n")
                #probs = model.predict_proba(x)
                #print(probs)
