import numpy as np
import argparse
import cv2 as cv
import subprocess
import time
import os
from yolo_utils import infer_image, show_image

def photo_labels(path):
  
  FLAGS={}
  FLAGS['labels']= './yolov3-coco/coco-labels'
  	# Download the YOLOv3 models if needed


	# Get the labels
  labels = open(FLAGS['labels']).read().strip().split('\n')
  colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')
  FLAGS['config']='./yolov3-coco/yolov3.cfg'
  FLAGS['weights']='./yolov3-coco/yolov3.weights'
	# Load the weights and configutation to form the pretrained YOLOv3 model
  net = cv.dnn.readNetFromDarknet(FLAGS['config'], FLAGS['weights'])

	# Get the output layer names of the model
  layer_names = net.getLayerNames()
  layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
  img = cv.imread(path)
  height, width = img.shape[:2]
  img, _, _, classids, idxs, text = infer_image(net, layer_names, height, width, img, colors, labels, FLAGS)

  #print(text)
  return text        
            
            
    