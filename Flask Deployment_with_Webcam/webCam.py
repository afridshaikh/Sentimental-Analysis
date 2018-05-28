import cv2
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def imageCapture():
	camera = cv2.VideoCapture(0)
	read_data = camera.read()
	camera.release()
	image = read_data[1]
	#cv2.imshow("asd", image)
	#cv2.waitKey(0)

	i = 1
	for (x,y,w,h) in face_detector.detectMultiScale(image):
		new_img = image[y:y+h,x:x+w]
		cv2.imwrite("uploads/img"+str(i)+".jpg", new_img)
		i += 1
	if i>=1:
		return(1)
	else:
		return(0)

