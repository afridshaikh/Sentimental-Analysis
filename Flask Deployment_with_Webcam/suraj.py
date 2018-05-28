from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import errno
app = Flask(__name__)
file_path = 'upload'
app.config['file_path'] = file_path

@app.route('/')
def upload():
	return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

	if request.method == 'POST':
		f = request.files['file']
		#f.save(secure_filename(f.filename))
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
	return 'file uploaded successfully'
		
if __name__ == '__main__':
        app.run(debug = True)
