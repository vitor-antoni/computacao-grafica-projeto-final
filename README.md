# Atividade avaliativa para composição da A3
## Apresentação
### Objetivo do repositório
Este repositório está limitado a entrega das atividades propostas da UC de Computação Gráfica. Como relatado, estas irão compor 10 pontos de 40 pontos (25% do total) da avaliação final A3. Todavia, são 8 exercícios propostos pelo professor Vinicius Cassol e Vitor Leaes e que abragem conhecimentos da linguagem de programação Python utilizando os pacotes PyGame, PyOpenGL e Numpy.

### Colaboradores
Os colabores e mantenedores deste repositório são _Vitor Silva de Antoni_ e _Lucas Machado Weirich_. Ambos estudantes de Ciência da Computação na instituição **UniRitter - Campus Fapa**.

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
### Exercício 1
**OBSERVAÇÃO IMPORTANTE:** Para fins de organização e boa visualização deste README, as duas estruturas abaixo serão apresentadas apenas nas considerações do exercício 1, mas foram utilizdas para execução dos exercícios **1, 3, 5 e 7**.

Os comandos abaixo são para inicialização da tela do PyGame e configuração do PyOpenGL. Em que basicamente define o tamanho do display, cria uma tela com estas dimensões, usa as flags `pygame.OPENGL` para habilitar o uso de OpenGL na renderização gráfica e `pygame.DOUBLEBUF` para habilitar o uso de double buffering, que ajuda a evitar o "flickering" (tremulação) da tela durante a renderização. Além disto, aplica uma translação na cena, movendo a câmera 5 unidades para trás no eixo Z. Isso permite que objetos desenhados ao redor da origem (0, 0, 0) fiquem visíveis dentro do campo de visão da câmera.
```
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
gluPerspective(75, (display[0]/display[1]), 0.1, 80.0)
glTranslatef(0.0,0.0, -5)
```
Outra estrutura, é a estrutura que fornece um loop _**while**_ para apresentação das figuras geométricas na janela do PyGame. Em que podemos validar os eventos criados pelo usuário para que o código decida o que deve ser feito. Exemplo: Se o usuário fechar a janela do PyGame, o código finalizará a execução.
```
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
```
### Exercício 3
### Exercício 5
### Exercício 7
