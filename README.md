# Atividade avaliativa para composição da A3
## Apresentação
### Objetivo do repositório
Este repositório está limitado a entrega das atividades propostas da UC de Computação Gráfica. Como relatado, estas irão compor 10 pontos de 40 pontos (25% do total) da avaliação final A3. Todavia, são 8 exercícios propostos pelo professor Vinicius Cassol e Vitor Leaes e que abragem conhecimentos da linguagem de programação Python utilizando os pacotes PyGame, PyOpenGL e Numpy.

### Colaboradores
Os colabores e mantenedores deste repositório são _Vitor Silva de Antoni_ e _Lucas Machado Weirich_. Ambos estudantes de Ciência da Computação na instituição **UniRitter - Campus Fapa**. A divisão de atividades entre os colaboradores foi baseada atividades de números ímpares ao Vitor e atividades de números pares ao Lucas.

## Descritivo técnico
### Softwares
Para que os códigos das atividades possam ser executados com êxito, é necessário garantir que o Python esteja instalado na máquina hospedeira. Para isto, podemos verificar se o mesmo está instalado usando os comandos a seguir dependendo do Sistema Operacional. 
- **Windows:** `py --version`
- **MAC/Linux:** `pyton3 --version`

### Pacotes e dependências
Como ressaltado anteriormente, para execução destas atividades, foi utilizado os pacotes PyGame, PyOpenGL e Numpy. Portanto, precisamos garantir que estes também estejam estados na máquina para garantir o êxito da execução.
Logo, os comandos necessários para baixá-los são estes:
- **Windows:** `py -m pip install pygame pyopengl numpy`
- **Mac/Linux:** `pip install pygame pyopengl numpy`

## Considerações de execução
### Atividade 1
> **OBSERVAÇÃO IMPORTANTE:** Para fins de organização e boa visualização deste README, as duas estruturas abaixo serão apresentadas apenas nas considerações do exercício 1, mas foram utilizdas para execução dos exercícios **1, 3, 5 e 7**.

Os comandos abaixo são para inicialização da tela do PyGame e configuração do PyOpenGL. Em que basicamente define o tamanho do display, cria uma tela com estas dimensões, usa as flags `pygame.OPENGL` para habilitar o uso de OpenGL na renderização gráfica e `pygame.DOUBLEBUF` para habilitar o uso de double buffering, que ajuda a evitar o "flickering" (tremulação) da tela durante a renderização. Além disto, aplica uma translação na cena, movendo a câmera 5 unidades para trás no eixo Z. Isso permite que objetos desenhados ao redor da origem (0, 0, 0) fiquem visíveis dentro do campo de visão da câmera.
```
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
gluPerspective(75, (display[0]/display[1]), 0.1, 80.0)
glTranslatef(0.0,0.0, -5)
```
Outra estrutura, é a estrutura que fornece um loop _**while**_ para apresentação das figuras geométricas na janela do PyGame. Em que podemos validar os eventos criados pelo usuário para que o código decida o que deve ser feito (exemplo: se o usuário fechar a janela do PyGame, o código finalizará a execução). Além disto, é definido a função `glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)` para limpar o o cache dos dados armazenados.
```
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
```

#### **Exercício 1-A**
O código principal a ser analisado é o código da função `draw_point()` que é responsável por desenhar o ponto na tela. Portanto, abaixo segue o código e a explicação dos parâmetros utilizados.
```
def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
```
- `glPointSize(size)` > Define o tamanho do ponto a ser desenhado.
- `glBegin(GL_POINTS)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um ponto.
- `glVertex2i(x, y)` > Define as cordenadas do ponto a ser desenhado.
- `glEnd()` > Finaliza a execução do desenho.

#### **Exercício 1-B**
Os trechos principais a serem analisados é o código que recebe os valores de X1 ,Y1 , X2 E Y2 através de input do usuário e o código da função `draw_line()` que é responsável por desenhar a linha na tela com base nos valores de input do usuário. Portanto, abaixo seguem os códigos e as explicações dos parâmetros utilizados.
```
x1 = int(input("Valor de X1: "))
y1 = int(input("Valor de Y1: "))
x2 = int(input("Valor de X2: "))
y2 = int(input("Valor de Y2: "))
```
- Define variáveis que receberão os input do usuário.

```
def draw_line(X1, Y1, X2, Y2):
    glBegin(GL_LINES)
    glVertex2i(X1, Y1)
    glVertex2i(X2, Y2)
    glEnd()
```
- `glBegin(GL_LINES)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é uma linha.
- `glVertex2i(X1, Y1)` > Define as cordenadas do primeiro ponto da reta.
- `glVertex2i(X2, Y2)` > Define as cordenadas do segundo ponto da reta.
- `glEnd()` > Finaliza a execução do desenho.

#### **Exercício 1-C**
O trecho principal a ser analisado é o código que desenha o quadrado na tela, no caso a função `draw_square()`.
```
def draw_square():
    vertices = (
        (4, 3, 0),
        (4, 2, 0),
        (3, 2, 0),
        (3, 3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()
```
- `vertices()` > Uma variável do tipo tupla que possuí outras tuplas aninhadas e que possuem as cordenadas de cada vértice do quadrado.
- `glBegin(GL_QUADS)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um quadrado.
- `for vertex in vertices` > Um laço FOR que itera a tupla da variável `vertices` e desenha o quadrado com base nos valores das tuplas aninhadas.
- `glEnd()` > Finaliza a execução do desenho.

#### **Exercício 1-D**
O trecho principal a ser analisado é o código que desenha o triângulo na tela, no caso a função `def draw_triangle()`.
```
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, 1, 0)    # Ponto inferior direito
    glVertex3f(-2, 2, 0)    # Ponto superior
    glEnd()
```
- `glBegin(GL_TRIANGLES)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um triângulo.
- `glVertex3f()` > Define os vértices do triângulo a ser desenhado. Sendo eles, o primeiro vértice o ponto inferior esquerdo, o segundo vértice o ponto inferior direito e o último vértice o ponto superior.
- `glEnd()` > Finaliza a execução do desenho.

### Exercício 3
Como solicitado na proposta da atividade, devemos desenhar um triângulo e definir 3 formas de interação com o desenho. Sendo elas a possibilidade de movê-lo, dimnuí-lo/aumentá-lo e rotacioná-lo. Portanto, segue a explicativa de cada código a abaixo.
```
if keys[pygame.K_LEFT]:
    triangle_pos_x -= 0.05

elif keys[pygame.K_RIGHT]:
    triangle_pos_x += 0.05

elif keys[pygame.K_UP]:
    triangle_pos_y += 0.05

elif keys[pygame.K_DOWN]:
    triangle_pos_y -= 0.05
```
- Se pressionado as **setas** do teclado, o triângulo será movido de acordo com a direção da seta pressionada.

```
if keys[pygame.K_a]:
    triangle_scale += 0.01

# Diminuir o tamanho do triângulo (tecla D)
elif keys[pygame.K_d]:
    triangle_scale -= 0.01

    if triangle_scale < 0.1:
        triangle_scale = 0.1
```
- Se pressionado a tecla `A` o triângulo aumentará de tamanho. Se pressionado a tecla `D` o triângulo diminuirá de tamanho.

```
if keys[pygame.K_q]:
    triangle_rotation += 90

# Rotacionar o triângulo em sentido anti-horário (tecla E)
elif keys[pygame.K_e]:
    triangle_rotation -= 90
```
- Se pressionado a tecla `E` o triângulo rotacionará em sentido horário. Se pressionado a tecla `Q` o triângulo rotacionará em sentido anti-horário.

```
glPushMatrix()
glTranslatef(triangle_pos_x, triangle_pos_y, 0)
glRotatef(triangle_rotation, 0, 0, 1)
glScalef(triangle_scale, triangle_scale, 1.0)

draw_triangle()

glPopMatrix()
```
- `glPushMatrix()` > Salva a matriz atual para que possam ser realizadas transformações temporárias na representação gráfica.
- `glTranslatef(triangle_pos_x, triangle_pos_y, 0)` > Comando utilizado para realizar a movimentação do triângulo no plano cartesiano.
- `glRotatef(triangle_rotation, 0, 0, 1)` > Realizar a rotação do triângulo.
- `glScalef(triangle_scale, triangle_scale, 1.0)` > Realizar o aumento e diminuição do tamanho do triângulo.
- `glPopMatrix()` > Restaura a matriz para o estado salvo mais recente.

### Exercício 5
### Exercício 7
