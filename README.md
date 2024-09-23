# Atividade avaliativa para composição da A3
## Apresentação
### Objetivo do repositório
Este repositório está limitado a entrega das atividades propostas da UC de Computação Gráfica. Como relatado, estas irão compor 10 pontos de 40 pontos (25% do total) da avaliação final A3. Todavia, são 8 exercícios propostos pelo professor Vinicius Cassol e Vitor Leaes e que abragem conhecimentos da linguagem de programação Python utilizando os pacotes PyGame, PyOpenGL e Numpy.

### Colaboradores
Os colabores e mantenedores deste repositório são _Vitor Silva de Antoni_ e _Lucas Machado Weirich_. Ambos estudantes de Ciência da Computação na instituição **UniRitter - Campus Fapa**. A divisão de atividades entre os colaboradores foi baseada na atribuição de atividades de números ímpares ao Vitor e atividades de números pares ao Lucas.

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

***

### Atividade 3
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

***

## Conclusão
Para concluírmos, gostaríamos de agradecer a atenção dedicada a análise das nossas resoluções.
