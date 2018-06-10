#!/usr/bin/python
import numpy as np
import cv2
import os
import sys

# Configuraoes de variaveis
FACTOR = 25
NEG_PATH = 'neg/'
NUM_POS = 100
NUM_NEG = 150
NUM_STAGES = 15

# Opcional: Desenha um retangulo onde o phone foi encontrado, foi utilizado apenas observar se a conversao de coordenadas estava correto
def show_finded_phone(path, img_name, x, y):
	img = cv2.imread(path + img_name)

	# Desenha um retangulo ao redor do telefone
	cv2.rectangle(img, (x - FACTOR, y - FACTOR), (x + FACTOR, y + FACTOR), (0, 0, 255), 2)

	if not os.path.exists('test'):
		os.makedirs('test')

	# Escreve na imagem
	cv2.imwrite('test/' + img_name, img)


def convert_coords(path, img_name, x_n, y_n):
	img = cv2.imread(path + img_name)
	img_shape = img.shape

	# Muda das coordenadas normalizadas para a posicao dos pixels na imagem
	x = int(float(x_n) * img_shape[1])
	y = int(float(y_n) * img_shape[0])

	return x, y

def convert_labels_to_train(path):
	with open(path + 'labels.txt') as f:
		read_data = f.readlines()
	f.closed

	with open(path + 'info.txt', 'w') as f:
		for line in read_data:
			temp = line.split()
			print(path, temp[0], temp[1], temp[2])
			x, y = convert_coords(path, temp[0], temp[1], temp[2])
			# show_finded_phone(path, temp[0], x, y)
			f.write("{0} 1 {1} {2} {3} {4}\n".format(temp[0], x, y, FACTOR, FACTOR))
	f.closed

# Cria o arquivo com os caminhos das imagens negativas
def prepare_neg_env(path):
	os.system("ls {0}/* > bg.txt".format(path))

# Realiza o treinamento do OpenCV
def  train_opencv(pos_path):
	os.system("rm positives.vec")
	os.system("opencv_createsamples -info {0}info.txt -num {1} -w {2} -h {2} -vec positives.vec".format(pos_path, NUM_POS, FACTOR))
	if not os.path.exists('data'):
		os.makedirs('data')
	os.system("rm data/*")	
	os.system("opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos {0} -numNeg {1} -numStages {2} -w {3} -h {3}".format(NUM_POS, NUM_NEG, NUM_STAGES, FACTOR))

def main():
	# Recebe como argumento o caminho onde estao as imagens de treino e labels.txt
	path = str(sys.argv[1])
	
	# Converte as coordenadas normalizadas de label.txt para o formato do opencv
	convert_labels_to_train(path)

	# Prepara o ambiente das imagens negativas para o treino do opencv
	prepare_neg_env(NEG_PATH)

	# Com o ambiente preparado, treina o opencv
	train_opencv(path)

if __name__ == '__main__':
    main()

