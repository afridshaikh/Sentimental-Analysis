import glob
from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.4,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')


save_path = "C:\\Users\\ABHIJEET\\Desktop\\Sentimental Analysis\\test\\train\\happy\\"

j = 0

for i in glob.glob('C:\\Users\\ABHIJEET\\Desktop\\Sentimental Analysis\\data\\train\\happy\\*.jpg'):
    img = load_img(i)  
    x = img_to_array(img)  
    x = x.reshape((1,) + x.shape)  
    j = 0
    for batch in datagen.flow(x,save_to_dir=save_path, save_prefix='happy', save_format='jpg'):
        j += 1
        if j > 40:
            break 
