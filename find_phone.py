#!/usr/bin/python
import numpy as np
import cv2
import sys

# Para utilizar um cascade ja treinado, descomente o 'cascades/phone_cascade.xml' e comente o outro.
# CASCADE_PATH = 'cascades/phone_cascade.xml'
CASCADE_PATH = 'data/cascade.xml'

def show_img_on_window(img, phones):
	for (x, y, w, h) in phones:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

		cv2.imshow('phone', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

def find_image(img_path, show_img = None):
	img = cv2.imread(img_path)
	if img is None:
		return 'Error: Nao foi possivel encontrar a imagem no diretorio!'
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	phone_cascade = cv2.CascadeClassifier(CASCADE_PATH)
	phones = phone_cascade.detectMultiScale(gray, 1.3, 5)

	if show_img:
		show_img_on_window(img, phones)

	if phones is None or len(phones) < 1:
		return 'Error: O telefone nao foi encontrado na imagem!'

	x, y, w, h = phones[0]
	x_n = round(float(float(2*x+w) / 2.0) / float(img.shape[1]), 4)
	y_n = round(float(float(2*y+h) / 2.0) / float(img.shape[0]), 4)

	return str(x_n) + ' ' + str(y_n)	

def main():
	# Recebe como parametro o caminho da imagem a ser buscada
	file_path = str(sys.argv[1])

	# Verifica se a opcao de exibir a imagem foi passada por parametro
	show_img = '--showimg' in sys.argv[1:]

	# Chama a funcao para encontrar a imagem, retorna as coordenadas normalizadas
	print(find_image(file_path, show_img))
 
if __name__ == '__main__':
    main()