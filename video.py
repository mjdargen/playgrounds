import numpy as np
import cv2
from matplotlib import pyplot as plt
from IPython.display import clear_output
from google.colab.patches import cv2_imshow

class VideoEditor:
	def __init__(self):
		pass

	def process(self, f, in_path, out_path):
		stream = cv2.VideoCapture(in_path)
		fourcc = cv2.VideoWriter_fourcc(*'MP4V')
		out = cv2.VideoWriter(out_path, fourcc, 20.0, (640,480))
		count = 0
		while 1:
			ret, img = stream.read()
			count += 1
			print('Frame:', count)
			if ret:
				img = f(img)
				out.write(img)
				clear_output()
				plt.imshow(img)
				plt.pause(0.000000001)
			else:
				break




















