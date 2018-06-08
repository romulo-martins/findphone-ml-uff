# Find Phone Task

A tarefa consiste em criar um prototipo de detecção de objetos, onde o objetivo é achar um telefone no chão. Maiores detalhes sobre a tarefa pode ser visto no arquivo de descrição *find_phone_task_description.pdf*.

## Detalhes de implementação

O projeto possui dois, scripts: um para treinamento e outro para realizar busca do telefone dado uma imagem.

O **script de treinamento** recebe como parametro apenas o caminho de onde se encontra as imagens para treinamento e o arquivo labels.txt que possui as coordenadas normalizadas de onde se encontra o telefone na foto.
Exemplo de execução:
```
> python train_phone_finder.py ~/find_phone
```

O **script de busca** utiliza o modelo criado pelo treinamento para exibir as coordenadas do telefone a ser buscado, dada uma imagem.
Exemplo de execução:
```
> python find_phone.py ~/find_phone_data/51.jpg
   0.2551​ 0.3129
```

Este script ainda possui a opção adicional de exibir a imagem passada por parametro, com um retangulo desenhado na foto ao redor do telefone encontrado.
Exemplo de execução:
```
> python find_phone.py ~/find_phone_data/51.jpg --showimg
```


## Referências:
- [Training Haar Cascades](https://memememememememe.me/post/training-haar-cascades/)
- [Creating your own Haar Cascade OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
- [Cascade Classifier Training](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html#cascade-classifier-training)