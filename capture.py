import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
	number = random. randint(0,100) 
	#initializing cv2
	videoCaptureObject = cv2.VideoCapture(0)
	result = True 
	while(result):
		#read the frames while the camera is on
		ret, frame = videoCaptureObject.read() 
		#cv2.imwrite() method is used to save an image to any storage device
		img_name = "img"+str(number)+".png"
		cv2.imwrite(img_name, frame) 
		start_time = time.time
		result = False
	return img_name
	print("snapshot taken")
	# releases the camera
	videoCaptureObject. release()
	#closes all the window that might be opened while this process
	cv2.destroyAllWindows()

def upload_file (img_name):
	access_token = "sl.BCwRWD_l9t8yTwzovAzwoZg73O7BUsa9yxHVatql8YMmrOeLbPRlmZ_ZS_lnBN7eo0xEliAYlFRexZcY62jDgahU2nj8OxwoveHqE25U_7IP2vtZDC_AgQ67xTHfVFApqLpx1SY"
	file =img_name 
	file_from= file
	file_to="/testFolder/"+(img_name) 
	dbx = dropbox.Dropbox (access_token)
	
	with open (file_from, 'rb') as f: 
		dbx.files_upload (f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
		print("file uploaded")

def main(): 
	while(True):
		if ((time.time() - start_time) >= 5): 
			name = take_snapshot() 
			upload_file (name) 
main()