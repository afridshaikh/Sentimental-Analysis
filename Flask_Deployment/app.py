import os
from flask import Flask, request, redirect, url_for,render_template,flash
from werkzeug.utils import secure_filename
UPLOAD_FOLDER =  os.getcwd() + '\\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def first():
	return render_template('index.html')

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
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#return 'file uploaded successfully'
			return render_template('predict.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
	import predict as pre
	result = pre.predict_sentimets()
	if(result == '[[1]]'):
		return 'Our system has analysed it as Happy'
	elif(result=='[[0]]'):
		return 'Our system has analysed it as Sad'
	return result

if __name__ == '__main__':
	app.run(debug = True)
	