
from flask import Flask , request , jsonify
import numpy as np 
import cv2
 
from detect_custom import CD_detecter

app = Flask(__name__)


@app.route('/primg' , methods=['POST'])
def mask_image():

	# set the detector
	D = CD_detecter(model_weights_path = "./custom_models/last.pt" , img_size = 640)



	# process image data 
	
	file = request.files['image'].read() ## byte file

	npimg = np.fromstring(file, np.uint8)
	img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)


	#detect objects 
	objects = D.detect_cd(img)


	return jsonify(objects)
 

if __name__ == '__main__':
	app.run(debug = True)