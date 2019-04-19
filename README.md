# Find Phone Task

A tarefa consiste em criar um prototipo de detecção de objetos, onde o objetivo é achar um telefone no chão. Maiores detalhes sobre a tarefa pode ser visto no arquivo de descrição *find_phone_task_description.pdf*.

## Considerações iniciais

Este trabalho foi realizado utilizando o sistema operacional `ubuntu 18.04 bionic beaver`.
Portanto é recomendavel a utilização do mesmo para uma execução efetiva dos scripts.

## Dependencias

Para instalar o opencv é prciso instalar primeiro suas dependenciais:

Compilação
```
sudo apt-get install build-essential

```

Bibliotecas
```
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

```

Dependencias do python
```
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

Instalação do OpenCV
```
sudo apt-get install libopencv-dev
```

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

## Observações

Algumas considerações importantes sobre o script de treinamento são:
- As variaveis (logo no inicio do script) fazem parte da configuração do treinamento, podendo ser alterado para uma maior precisão.
- A pasta `neg/` possui cerca de 300 imagens para servir de negativos para o OpenCV, porem na configuração padrão do treinamento são utiliadas apenas 150.
- Se desejar utilizar outras imagens para servir de negativos para o treinamento, é necessario que coloca-las na pasta `neg/`.
- O script de treinamento leva em consideração apenas as imagens que possui suas coordenadas em *label.txt* para as imagens positivas.
- Foram utilizados apenas 15 etapas (*num stages*) para treinamento, podendo ser alterado para uma maior precisão.
- Na pasta *cascades* foi incluido um cascade chamando *phone_cascade.xml* que foi treinado de forma mais minuciosa, e que demorou muitas horas para ser treinado. Se desejar utiliza-lo para teste basta descomantar a variaval:
```
CASCADE_PATH = 'cascades/phone_cascade.xml'
```
e comentar
```
CASCADE_PATH = 'data/cascade.xml'
```

## Referências:
- [Training Haar Cascades](https://memememememememe.me/post/training-haar-cascades/)
- [Creating your own Haar Cascade OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
- [Cascade Classifier Training](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html#cascade-classifier-training)