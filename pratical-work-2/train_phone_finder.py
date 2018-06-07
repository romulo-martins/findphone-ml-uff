#!/usr/bin/python
import numpy as np
import cv2
import sys
import os

# Desenha um retangulo onde o phone foi encontrado
def show_finded_phone(path, img_name, x, y):
	# Carrega a imagem
	img = cv2.imread(path + '/' + img_name)

	# Exibe no console as dimensoes da imagem
	img_shape = img.shape
	print(img.shape)

	# Muda das coordenadas normalizadas para a posicao dos pixels na imagem
	x = int(float(x) * img_shape[1])
	y = int(float(y) * img_shape[0])
	factor = 30

	# Desenha um retangulo ao redor do telefone
	cv2.rectangle(img, (x - factor, y - factor), (x + factor, y + factor), (0, 0, 255), 2)

	if not os.path.exists('test'):
		os.makedirs('test')

	# Escreve na imagem
	cv2.imwrite('test/' + img_name, img)

# Le as coordenadas normalizadas a partir do labels.txt
# OBS: ainda esta em fase de desenvolvimento
def read_labels(path):
	with open(path + '/labels.txt') as f:
		read_data = f.readlines()
		for line in read_data:
			temp = line.split()
			print(temp[0], temp[1], temp[2])
			show_finded_phone(path, temp[0], temp[1], temp[2])
	f.closed


# ----- main -----
path = str(sys.argv[1])
read_labels(path)
# show_finded_phone(path, '/1.jpg', 0.8714, 0.1718)
