# Atividade avaliativa para composição da A3
## Apresentação
### Objetivo do repositório
Este repositório está limitado a entrega das atividades propostas da UC de Computação Gráfica. Como relatado, estas irão compor 10 pontos de 40 pontos (25% do total) da avaliação final A3. Todavia, são 8 exercícios propostos pelo professor Vinicius Cassol e Vitor Leaes e que abragem conhecimentos da linguagem de programação Python utilizando os pacotes PyGame, PyOpenGL e Numpy.

### Colaboradores
Os colabores e mantenedores deste repositório são _Vitor Silva de Antoni_ e _Lucas Machado Weirich_. Ambos estudantes de Ciência da Computação na instituição **UniRitter - Campus Fapa** no turno noturno. A divisão de atividades entre os colaboradores foi baseada na atribuição de atividades de números ímpares ao Vitor e atividades de números pares ao Lucas.

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

![Ex01-a](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex01-a.png)

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

![Ex01-b](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex01-b.png)

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

![Ex01-c](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex01-c.png)

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

![Ex01-d](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex01-d.png)

***

### Atividade 2

![Ex02-a](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex02-a.png)
![Ex02-b](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex02-b.png)
![Ex02-c](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex02-c.png)
![Ex02-d](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex02-d.png)
Como solicitado na proposta da atividade, precisamos desenhar dois triângulos em uma mesma tela com interações, sendo elas: apenas polígono preenchido, apenas com contorno, apenas como pontos e todas as opções juntas.

Utilizamos o pygame para escrever o código completo, importando tudo do pygame.locals

Para criação da janela utilizamos como largura 800 e altura 600
screen_width = 800

screen_height = 600

As cores utilizadas foram: preto, vermelho, azul, ciano e amarelo.

As teclas definidas para cada modo foram: 1, 2, 3 e 4 sendo respectivamente polígono preenchido, contorno, pontos e todos juntos
running = True
```
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Altera o modo de desenho com as teclas 1, 2, 3 e 4
            if event.key == K_1:
                draw_mode = 1  # Preenchido
            elif event.key == K_2:
                draw_mode = 2  # Contorno
            elif event.key == K_3:
                draw_mode = 3  # Pontos
            elif event.key == K_4:
                draw_mode = 4  # Todas as formas juntas
```

***

### Atividade 3
Como solicitado na proposta da atividade, devemos desenhar um triângulo e definir 3 formas de interação com o desenho. Sendo elas a possibilidade de movê-lo, dimnuí-lo/aumentá-lo e rotacioná-lo. Portanto, segue a explicativa de cada código a abaixo e a legenda de comandos possíveis.

- Para movimentar o objeto: setas do teclado
- Para aumentar e diminuir o objeto: A (aumenta) e D (diminuí)
- Para rotacionar o objeto: Q (rotaciona sentido anti-horário) e E (rotaciona sentido horário)

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

draw_right_triangle()

glPopMatrix()
```
- `glPushMatrix()` > Salva a matriz atual para que possam ser realizadas transformações temporárias na representação gráfica.
- `glTranslatef(triangle_pos_x, triangle_pos_y, 0)` > Comando utilizado para realizar a movimentação do triângulo no plano cartesiano.
- `glRotatef(triangle_rotation, 0, 0, 1)` > Realizar a rotação do triângulo.
- `glScalef(triangle_scale, triangle_scale, 1.0)` > Realizar o aumento e diminuição do tamanho do triângulo.
- `glPopMatrix()` > Restaura a matriz para o estado salvo mais recente.

***

```
def draw_right_triangle():
    vertices = (
        (1, 1, 0),
        (-1, 0, 0),
        (-1, 0, 0),
        (-1, 1, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()
```
- `vertices()` > Uma variável do tipo tupla que possuí outras tuplas aninhadas e que possuem as cordenadas de cada vértice do triângulo retângulo.
- `glBegin(GL_QUADS)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um quadrado, mas que com as cordenadas setadas anteriormente, na verdade será desenhado um triângulo retângulo.
- `for vertex in vertices` > Um laço FOR que itera a tupla da variável `vertices` e desenha o triângulo retângulo com base nos valores das tuplas aninhadas.
- `glEnd()` > Finaliza a execução do desenho.

![Ex03-a](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex03-a.png)
![Ex03-b](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex03-b.png)
![Ex03-c](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex03-c.png)
![Ex03-d](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex03-d.png)

***

### Atividade 4

![Ex04-a](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex04-a.png)
![Ex04-b](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex04-b.png)

Nessa atividade é pedido que seja feito um quadrado capaz de se movimentar pela página com as teclas WASD ou SETAS.

Para largura usamos 800 e altura 600.

screen_width = 800

screen_height = 600

Para cores utilizamos preto e branco, sendo branco para o quadrado

Definimos que o quadrado se movimenta com ambas as teclas WASD e SETAS.
```
   if keys[K_UP] or keys[K_w]:    # Cima
       square_y -= speed
   if keys[K_DOWN] or keys[K_s]:  # Baixo
       square_y += speed
   if keys[K_LEFT] or keys[K_a]:   # Esquerda
       square_x -= speed
   if keys[K_RIGHT] or keys[K_d]:  # Direita
       square_x += speed
```
       
***

### Atividade 5

Nesta atividade, precisamos criar 3 figuras geométricas (triângulo, círculo e quadrado). Além disto, precisamos criar reflexões destes objetos nos exios X e Y. Portanto, abaixo segue a explicação de execução.

#### **Triângulo**
```
def draw_triangle():
    # Desenha o triângulo
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, 1, 0)    # Ponto inferior direito
    glVertex3f(-2, 2, 0)    # Ponto superior
    glEnd()

    # Desenha o triângulo refletido
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, -1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, -1, 0)    # Ponto inferior direito
    glVertex3f(-2, -2, 0)    # Ponto superior
    glEnd()
```
- `glBegin(GL_TRIANGLES)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um triângulo.
- `glVertex3f()` > Define os vértices do triângulo a ser desenhado. Sendo eles, o primeiro vértice o ponto inferior esquerdo, o segundo vértice o ponto inferior direito e o último vértice o ponto superior.
- `glEnd()` > Finaliza a execução do desenho.
- Para fazer a reflexão do triângulo sob o eixo X, precisamos multiplicar as cordenadas Y de cada vértice por -1.

#### **Círculo**
```
def draw_circle():
    # Desenha a circunferência
    x_circulo = 6
    y_circulo = 4
    
    raio = 1
    segmento = 360

    glBegin(GL_TRIANGLE_FAN)
    for i in range(segmento):
        angle = 2 * math.pi * i / segmento
        x = raio * math.cos(angle)
        y = raio * math.sin(angle)
        glVertex3f(x + x_circulo, y + y_circulo, 0)
    glEnd()


    # Desenha a circunferência refletida
    x_circulo = -6
    y_circulo = 4
    
    raio = 1
    segmento = 360

    glBegin(GL_TRIANGLE_FAN)
    for i in range(segmento):
        angle = 2 * math.pi * i / segmento
        x = raio * math.cos(angle)
        y = raio * math.sin(angle)
        glVertex3f(x + x_circulo, y + y_circulo, 0)
    glEnd()
```
- `x_circulo e y_circulo` > As coordenadas do centro da circunferência.
- `raio` > O raio da circunferência.
- `segmento` > O número de divisões da circunferência, ou seja, quantos segmentos (ou fatias) vão compor o círculo. Neste caso, 360, o que significa que o círculo será aproximado por 360 vértices (um vértice para cada grau, o que garante uma forma suave).
- `glBegin(GL_TRIANGLE_FAN)` > Indica ao PyOpenGL que deve ser inicializado e que as figuras geométricas a serem desenhadas são triângulos conectados em um ponto central (o centro da circunferência).
- `for i in range(segmento):` > O loop percorre todos os 360 segmentos que formam a circunferência
- `angle` > Calcula o ângulo atual, em radianos, baseado no número de segmentos.
- `x e y` > Calcula as coordenadas (x, y) usando as funções trigonométricas cos e sin, multiplicando pelo raio para obter o ponto ao longo da circunferência.
- `x = raio * math.cos(angle)`> calcula a coordenada x para o vértice no ângulo atual.
- `y = raio * math.sin(angle)` > calcula a coordenada y correspondente.
- `glVertex3f(x + x_circulo, y + y_circulo, 0)` > Define o vértice no plano cartesiano.
- `glEnd()` > Finaliza a execução do desenho.
- Para fazer a reflexão do círculo sob o eixo Y, precisamos multiplicar a cordenada X do círculo por -1.

#### **Quadrado**
```
def draw_square():
    # Desenha o quadrado
    vertices = (
        (4, 3, 0),
        (4, 2, 0),
        (3, 2, 0),
        (3, 3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    # Desenha o quadrado refletido
    ## Reflexao eixo X
    vertices = (
        (4, -3, 0),
        (4, -2, 0),
        (3, -2, 0),
        (3, -3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    ## Reflexao eixo Y
    vertices = (
        (-4, 3, 0),
        (-4, 2, 0),
        (-3, 2, 0),
        (-3, 3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()
```
- `vertices()` > Uma variável do tipo tupla que possuí outras tuplas aninhadas e que possuem as cordenadas de cada vértice do quadrado.
- `glBegin(GL_QUADS)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um quadrado.
- `for vertex in vertices` > Um laço FOR que itera a tupla da variável `vertices` e desenha o quadrado com base nos valores das tuplas aninhadas.
- `glEnd()` > Finaliza a execução do desenho.
- Para fazer a reflexão do quadrado sob o eixo Y, precisamos multiplicar a cordenada X do círculo por -1. E para fazer a reflexão sob o eixo X, precisamos multiplicar as cordenadas Y de cada vértice por -1.

![Ex05](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex05.png)

***

### Atividade 6

![Ex06](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex06.png)

Nessa atividade devemos criar uma casa simples, utilizando um quadrado para o corpo, um triângulo para o telhado e dois círculos para as janelas

Para largura utilizamos 800 e para altura 600.

screen_width = 800

screen_height = 600

Definimos as cores a serem utilizadas: preto, branco, marrom, verde e azul.
```
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)  # Cor do corpo da casa
GREEN = (0, 128, 0)  # Cor do telhado
BLUE = (0, 0, 255)  # Cor das janelas

Para o tamanho de cada objeto utilizamos as coordenadas x e y

   window_radius = 20
   window_y = house_y + 50
   pygame.draw.circle(screen, BLUE, (house_x + 40, window_y + 40), window_radius)
   pygame.draw.circle(screen, BLUE, (house_x + 110, window_y + 40), window_radius)
```

***

### Atividade 7
Conforme solicitado na atividade, devemos montar um deseneho com as formas geométricas primitivas. Portanto, foi escolhido o deseneho de uma boneca, em que os braços são representados por linhas, o corpo por triângulo, as pernas por retângulos e a cabeça por círculo.

#### **Corpo (triângulo)**
```
def draw_body():
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(1, 1, 0)     # Ponto inferior direito
    glVertex3f(0, 3, 0)     # Ponto superior
    glEnd()
```
- `glBegin(GL_TRIANGLES)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um triângulo.
- `glVertex3f()` > Define os vértices do triângulo a ser desenhado. Sendo eles, o primeiro vértice o ponto inferior esquerdo, o segundo vértice o ponto inferior direito e o último vértice o ponto superior.
- `glEnd()` > Finaliza a execução do desenho.

#### **Cabeça (círculo)**
```
def draw_head():
    x_circulo = 0
    y_circulo = 4
    
    raio = 1
    segmento = 360

    glBegin(GL_TRIANGLE_FAN)
    for i in range(segmento):
        angle = 2 * math.pi * i / segmento
        x = raio * math.cos(angle)
        y = raio * math.sin(angle)
        glVertex3f(x + x_circulo, y + y_circulo, 0)
    glEnd()
```
- `x_circulo e y_circulo` > As coordenadas do centro da circunferência.
- `raio` > O raio da circunferência.
- `segmento` > O número de divisões da circunferência, ou seja, quantos segmentos (ou fatias) vão compor o círculo. Neste caso, 360, o que significa que o círculo será aproximado por 360 vértices (um vértice para cada grau, o que garante uma forma suave).
- `glBegin(GL_TRIANGLE_FAN)` > Indica ao PyOpenGL que deve ser inicializado e que as figuras geométricas a serem desenhadas são triângulos conectados em um ponto central (o centro da circunferência).
- `for i in range(segmento):` > O loop percorre todos os 360 segmentos que formam a circunferência
- `angle` > Calcula o ângulo atual, em radianos, baseado no número de segmentos.
- `x e y` > Calcula as coordenadas (x, y) usando as funções trigonométricas cos e sin, multiplicando pelo raio para obter o ponto ao longo da circunferência.
- `x = raio * math.cos(angle)`> calcula a coordenada x para o vértice no ângulo atual.
- `y = raio * math.sin(angle)` > calcula a coordenada y correspondente.
- `glVertex3f(x + x_circulo, y + y_circulo, 0)` > Define o vértice no plano cartesiano.
- `glEnd()` > Finaliza a execução do desenho.

#### **Pernas (retângulo)**
```
def draw_legs():
    # Perna direita
    vertices = (
        (0.4, 1, 0),
        (0.4, 0, 0),
        (0.2, 0, 0),
        (0.2, 1, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    # Perna esquerda
    vertices = (
        (-0.4, 1, 0),
        (-0.4, 0, 0),
        (-0.2, 0, 0),
        (-0.2, 1, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()
```
- `vertices()` > Uma variável do tipo tupla que possuí outras tuplas aninhadas e que possuem as cordenadas de cada vértice do retângulo.
- `glBegin(GL_QUADS)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é um quadrado. Embora que a figura geométrica a ser desenhada seja o retângulo, usamos a inicialização do desenho do Quadrado mas transformamos a figura em um retângulo a partir das cordenadas de cada vértice.
- `for vertex in vertices` > Um laço FOR que itera a tupla da variável `vertices` e desenha o retângulo com base nos valores das tuplas aninhadas.
- `glEnd()` > Finaliza a execução do desenho.

#### **Braços (linhas)**
```
def draw_arms():
    # Braço direito
    glBegin(GL_LINES)
    glVertex2i(0, 2)
    glVertex2i(2, 2)
    glEnd()

    # Braço esquerdo
    glBegin(GL_LINES)
    glVertex2i(0, 2)
    glVertex2i(-2, 2)
    glEnd()
```
- `glBegin(GL_LINES)` > Indica ao PyOpenGL que deve ser inicializado e que a figura geométrica a ser desenhada é uma linha.
- `glVertex2i()` > Define as cordenadas do primeiro ponto da reta.
- `glVertex2i()` > Define as cordenadas do segundo ponto da reta.
- `glEnd()` > Finaliza a execução do desenho.

![Ex07](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex07.png)

***

### Atividade 8

![Ex08-a](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex08.png)
![Ex08-b](https://github.com/vitor-antoni/avaliacao-a3-cg-2024/blob/main/img/Ex08-b.png)

Por fim a ultima questão propõe a criação de uma cena composta de quadrados distribuídos em grid conforme o exemplo

Para criação da página utilizamos largura 800 e altura 600.

screen_width = 800

screen_height = 600

Para o tamanho de cada quadrado foi definido tamanho 50. Também definimos que cols são as colunas e rows as linhas
```
grid_size = 50  # Tamanho de cada quadrado
cols = screen_width // grid_size  # Número de colunas
rows = screen_height // grid_size  # Número de linhas

Para geração de cores aleatórias nos quadrados definimos color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for row in range(rows):
       for col in range(cols):
           # Gera uma cor aleatória
           color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
           # Calcula a posição do quadrado
           x = col * grid_size
           y = row * grid_size
           # Desenha o quadrado
           pygame.draw.rect(screen, color, (x, y, grid_size, grid_size))
```

***

## Conclusão
Para concluírmos, gostaríamos de agradecer a atenção dedicada a análise das nossas resoluções.
