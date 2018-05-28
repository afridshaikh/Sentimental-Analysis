import glob, os, os.path


mydir_uploads =  os.getcwd() +  '\\uploads'
def del_files_uploads():
	filelist = glob.glob(os.path.join(mydir_uploads, "*.*"))
	for f in filelist:
		os.remove(f)
	print("uploads folder is cleared")

	

mydir_img =   os.getcwd() +'\\img'
def del_files_img():
	filelist = glob.glob(os.path.join(mydir_img, "*.*"))
	for f in filelist:
		os.remove(f)
	print("img folder is cleared")
	

