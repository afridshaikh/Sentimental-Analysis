import cv2
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import glob, os, os.path
def cropUploadImage():
	j=1
	img_width,img_height = 150,150
	for i in glob.glob('img\*.*'):
		image = cv2.imread(i)
		for (x,y,w,h) in face_detector.detectMultiScale(image):
			new_img = image[y:y+h,x:x+w]
			cv2.imwrite("uploads\img"+str(j)+".jpg", new_img)
			j+=1
			print("Image Cropped")
	#if i>=1:
		#return(1)
	#else:
		#return(0)
		
