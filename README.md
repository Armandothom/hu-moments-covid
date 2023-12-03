
# Reconhecimento de imagens através da técnica Hu Moments

Reconhecimento de imagens através de reconhecimento de formas (shapes) utilizando Hu Moments.



## Membros
Armando de Jesus Thomazini (RA: 2112639)

Felipe Loiola de Oliveira (RA: 1914499)

Lucas Moraes Camacho (RA: 1884905)

### Repositório
https://github.com/Armandothom/hu-moments-covid

### Vídeo
https://www.youtube.com/watch?v=IeicsstRytc&ab_channel=ArmandoThomazini


### Hu Moments
A técnica utilizada para reconhecimento de imagens envolve a aplicação do Hu Moments, um conjunto de sete momentos invariantes que desempenham um papel crucial na descrição da forma de objetos. Esses momentos são calculados a partir dos momentos de imagem, representando estatísticas que resumem a distribuição de intensidades dos pixels em uma imagem binária. É possível então, efetivamente reconhecer padrões geométricos em imagens, sendo particularmente útil em cenários onde a precisão na posição e orientação dos objetos é crucial para o sucesso do reconhecimento de padrões.

### Resultados
Os resultados utilizando este descritor foram bem homogêneos, uma possível explicação é que as imagens do dataset possuem o formato similar, trazendo assim uma amostragem com certa dificuldade de ser classificada utilizando Hu Moments. Os classificadores usados e seus respectivos resultados foram:

#### MLP
Das 9 imagens, foram classificadas 8 imagens com covid corretamente e 0 imagens normal corretamente. A acurácia foi de 88,8%.
![MLP_MATRIX](https://i.imgur.com/yYpJ3Z7.png "MLP")

#### RF
Das 9 imagens, foram classificadas 7 imagens com covid corretamente e 0 imagens normal corretamente. A acurácia foi de 77,7%.
![RF](https://i.imgur.com/lYHSK0U.png "RF")

#### SVM
Das 9 imagens, foram classificadas 8 imagens com covid corretamente e 0 imagens normal corretamente. A acurácia foi de 88,8%.
![SVM_MATRIX](https://i.imgur.com/iyZrcox.png "SVM")


## Passos de reprodução
1 - Fazer download do dataset

2 - Inserir o dataset dentro do folder **features_labels**, com seus respectivos subfolders **(test e train)**

3 - Executar data_splitting.py

4 - Renomear o folder **val** para **test**, em: **images_split/val**

5 - Executar huMoments_FeatureExtraction.py

6 - Executar run_all_classifiers.py


