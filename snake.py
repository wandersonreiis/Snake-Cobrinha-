import pygame
from pygame.locals import*
from sys import exit
from random import randint
 

pygame.init()

pygame.mixer.music.set_volume(0.25)
musica_fundo = pygame.mixer.music.load('music/CPU_Talk.wav')
pygame.mixer.music.play(-1)


colisao = pygame.mixer.Sound('music/smw_coin.wav') 
# colisao.set_volume(0)

largura = 640
altura = 480
x_cobra = largura/2
y_cobra = altura/2

velocidade = 10
x_controle = 20
y_controle = 0


x_maca = randint(40,600)
y_maca = randint(50,430)


pontos = 0
fonte = pygame.font.SysFont('arial', 25, bold=True, italic=True)


###    AREA DA TELA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("O Pai ta de Celta")
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial=5

morreu = False


def aumenta_cobra (lista_cobra):
    for XeY in lista_cobra:
        #XeY = [X,Y]
        #XeY[0] = X
        #XeY[1] = Y
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))


def startjogo():
         global pontos,comprimento_inicial,x_cobra,y_cobra,x_maca,y_maca,lista_cobra,lista_cabeca,morreu
         pontos = 0
         comprimento_inicial = 5
         x_cobra = int(largura/2)
         y_cobra = int(altura/2)
         lista_cabeca = []
         lista_cobra = []
         x_maca = randint(40,600)
         y_maca = randint(50,430)
         morreu = False

while True:

    relogio.tick(30)

    tela.fill((255,255,255))



    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))

    for event in pygame.event.get():
        if event.type ==QUIT:
                pygame.quit()
                exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                 x_controle = -velocidade
                 y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                 x_controle = velocidade
                 y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                 y_controle= -velocidade
                 x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                 y_controle  = velocidade
                 x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra+ y_controle

    # if pygame.key.get_pressed()[K_a]:
    #         x_cobra = x_cobra - 20
    # if pygame.key.get_pressed()[K_d]:
    #         x_cobra = x_cobra + 20
    # if pygame.key.get_pressed()[K_w]:
    #         y_cobra = y_cobra - 20
    # if pygame.key.get_pressed()[K_s]:
    #         y_cobra = y_cobra + 20

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))
    # pygame.draw.circle(tela,(0,0,255),(200,350),40)
    # pygame.draw.line(tela,(0,255,0),(390,0),(390,600),5)

    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos +=1
        colisao.play()
        comprimento_inicial +=1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()


        morreu = True
        while morreu:
                tela.fill((255,255,255))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN: 
                        if event.key == K_r:
                            startjogo()

                ret_texto.center = (largura//2, altura//2)  
                tela.blit(texto_formatado, ret_texto)

                pygame.display.update()



    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
        

    aumenta_cobra(lista_cobra)



    tela.blit(texto_formatado,(450,40))

    pygame.display.update()        