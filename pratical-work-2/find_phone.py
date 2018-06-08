#!/usr/bin/python
import numpy as np
import cv2
import sys

def find_image(img_path, show_img = None):
	phone_cascade = cv2.CascadeClassifier('cascades/cascade.xml')
	img = cv2.imread(img_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	phones = phone_cascade.detectMultiScale(gray, 1.3, 5)
	
	if phones is not None and len(phones) > 0:
		x, y, w, h = phones[0]
		x_n = round(float(float(2*x+w) / 2.0) / float(img.shape[1]), 4)
		y_n = round(float(float(2*y+h) / 2.0) / float(img.shape[0]), 4)

		print(str(x_n) + ' ' + str(y_n))

		if show_img:
			for (x, y, w, h) in phones:
				cv2.rectangle(img,(x, y),(x+w, y+h), (255, 0, 0), 2)

			cv2.imshow('phone', img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

def main():
	file_path = str(sys.argv[1])
	show_img = '--showimg' in sys.argv[1:]
	find_image(file_path, show_img)
 
if __name__ == '__main__':
    main()