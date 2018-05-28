import os #to use operating system dependent functionality
from flask import Flask, request, redirect, url_for ,render_template,flash 
from werkzeug.utils import secure_filename #werkzeug is Web server gateway interface (WSGI) which help us connect to web servers and perform various tasks.
# UPLOAD_FOLDER = 'E:\\suraj\\programs\\PythonProjects\\C & D\\flask\\img' #
UPLOAD_FOLDER = os.getcwd() + "\\img\\"
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg',]) #extensions to be allowed

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS # filename splitted in [0,1] 0=filename 1=extension

@app.route('/')
def first():
	import delFiles as del_fil
	del_fil.del_files_uploads()
	del_fil.del_files_img()
	return render_template('index.html') # first page popped up when server is hitted with request.

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # this catches the local drive path on which the server is running and uploads the images in the said directory
			print ("file uploaded successfully")
			return render_template('predict.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
	import crop as cr
	cr.cropUploadImage()
	import predict as pre
	result = pre.predict_sentimets()
	import delFiles as del_fil
	# print("before del")
	# del_fil.del_files_uploads()
	# del_fil.del_files_img()
	print("before del")
	if(result == '[0]'):
		return 'Our system has analysed it as Happy <br><a href="http://localhost:5000">Test More Sentiments</a>'
	elif(result=='[1]'):
		return 'Our system has analysed it as Neutral <br> <a href="http://localhost:5000">Test More Sentiments</a>'
	elif(result=='[2]'):
		return 'Our system has analysed it as Sad <br> <a href="http://localhost:5000">Test More Sentiments</a>'
	return result
	
@app.route('/webcam',methods=['GET','POST'])
def webcam():
	import webCam as wc
	result_1 = wc.imageCapture()
	if result_1 !=0:
		return render_template('predict.html')
	else:
		return render_template('index.html')
	
if __name__ == '__main__':
	app.run(debug = True)
	