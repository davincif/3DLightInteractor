# 3D Light Interactor
This project is just a graduation degree project made with the only purpose of learning and hitting the needed in our university's classroom.

## License

As this project has absolutely no intention of being using by anybody else, it doesn't have a license, but if you want to use it for, whatever the reason is, ask me and I give it to you for free ^^'

## Getting Started

see file "passos" in the main directory

### Prerequisites

All for python3:

* [PyOpenGL](https://www.python.org/downloads/) for python3
* [Pygame](https://www.pygame.org/news) 

No need to say that you'll need [pip3](https://stackoverflow.com/questions/33906336/where-is-pip3-installing-modules) to install all those things right?

short advice: don't use windows! You're gonna get crazy!

### Requirements / Requisitos

**Tema:** Múltiplas fontes de luz

**Parte Geral:** Implementar o método de visualização de objetos triangulados, através do algoritmo de conversão por varredura, com métodos de interpolação de Phong, com a visibilidade garantida pelo algoritmo do “z-buffer”.

**Parte Específica:** Produzir visualização com múltiplas fontes de luz.

**Descrição:** O usuário, através de arquivos-texto ou interface gráfica, entra com dados do objeto (triangulado, com lista dos vértices e da conectividade, que determina os triângulos, de um arquivo-texto), atributos do objeto (ka, kd e ks, pontos flutuantes entre 0 e 1, n, ponto flutuante positivo e Od, tripla de pontos flutuantes entre 0 e 1,), atributos da cena (Ia, nL (qtde de fontes), para cada fonte: IL, triplas de ponto flutuante entre 0 e 255, e PL, tripla de ponto flutuante) e os atributos da câmera virtual (C, N e V, triplas de pontos flutuantes, d, hx, e hy, pontos flutuantes positivos). O seu sistema começa preparando a câmera, ortogonalizando V e gerando U, e depois os normalizando, fazer a mudança de coordenadas para o sistema de vista de todos os vértices do objeto e das posições das fontes de luz PL, gerar as normais dos triângulos e gerar as normais dos vértices (como recomendado em sala de aula). Para cada triângulo, calculam-se as projeções dos seus vértices e inicia-se a sua conversão por varredura. Para cada pixel (x, yscan), calculam-se suas coordenadas baricêntricas com relação aos vértices projetados, e multiplicam-se essas coordenadas pelos correspondentes vértices do triângulo 3D original para se obter uma aproximação para o ponto 3D original correspondente ao pixel atual. Após uma consulta ao z-buffer, se for o caso, calcula-se uma aproximação para a normal do ponto utilizando-se mesmas coordenadas baricêntricas multiplicadas pelas normais dos respectivos vértices originais. Calculam-se também os demais vetores (V e para cada fonte: L e R) e os substitui na equação do modelo de iluminação de Phong para múltiplas fontes de luz, produzindo a cor do pixel atual.

**PS.:** a meneira como as informações serão passadas está na pasta compartilhas pelo munitor em "matiral-de-projetos"

### Exemples to test
[files in pyc](https://people.sc.fsu.edu/~jburkardt/data/ply/ply.html)