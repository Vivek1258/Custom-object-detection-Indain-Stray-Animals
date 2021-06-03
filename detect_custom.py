
import cv2
import torch
import numpy as np

from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import non_max_suppression , scale_coords 

class CD_detecter():

	"""docstring for Cd_detecter"""
	def __init__(self, 
				model_weights_path = "./custom_models/last.pt",
				img_size = 640 ):

		super(CD_detecter, self).__init__()
		
		self.weights = model_weights_path 
		self.imgsz = img_size
		self.model = self.get_model()
		self.names = self.model.names # get class names
		self.stride = int(self.model.stride.max()) # model stride
 

	def get_model(self):

		model = attempt_load(self.weights)  # load FP32 model 

		return model 


	def process_img(self, img):

		# Padded resize
		img = letterbox(img, self.imgsz, stride= self.stride )[0]  

		# Convert
		img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
		img = np.ascontiguousarray(img)

		img = torch.from_numpy(img) 
		img =  img.float()  # uint8 to fp16/32
		img /= 255.0  # 0 - 255 to 0.0 - 1.0

		if img.ndimension() == 3:
		    img = img.unsqueeze(0)

		return img 


	def detect_cd(self, img0):

		model = self.get_model() 

		img = self.process_img(img0)

		# Inference
		pred = model(img)[0]  

		# Apply NMS
		pred = non_max_suppression(pred, 
								 conf_thres=0.25, # object confidence threshold
								 iou_thres=0.45,  # IOU threshold for NMS 
	                        	max_det=300 ) # maximum number of detections per image 

		results = dict()
 

		i = 0 ; 

		for det in pred :
			# Rescale boxes from img_size to im0 size
			det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round() 

			# print(np.shape(det))

			for *xyxy, conf, cls in reversed(det):

				results[i] = { "object" :  self.names[int(cls)] , 
								"confidance" : float(conf) , 
								"cocrdinates" : list(map(lambda x : float(x) , xyxy)) 
								}
				i = i + 1

		return results 


if __name__ == '__main__':
	
	img = cv2.imread('19.jpg')

	d = CD_detecter()
 
	print(d.detect_cd(img))
