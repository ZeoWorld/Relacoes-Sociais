import pygame
from pygame import mixer
from random import randint

pygame.init()



x = 377         # max 530 min 190
y = 445
pos_x1 = 200
pos_y1 = randint(-300, -180)
pos_x2 = 370
pos_y2 = randint(-800, -300)
pos_x3 = 525
pos_y3 = randint(-1000, -800)
timer = 0
tempo_segundo = 0


velocidade = 10
velocidade1 = 15
velocidade2 = 22
velocidade3 = 9
mixer.music.load('Eu e Você  Sempre.mp3')
mixer.music.play(-1)
fundo = pygame.image.load('Fundo/Slide1.PNG')
moto =  pygame.image.load('moto.png')
carro_1 = pygame.image.load('carro1.png')
carro_2 = pygame.image.load('carro2.png')
carro_3 = pygame.image.load('carro3.png')

Aux = 1
font = pygame.font.SysFont('arial black', 30)
texto = font.render("Pontuação: ", True, (0,0,0), (255,255,255))
pos_texto = texto.get_rect()
pos_texto.center = 98,5

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projeto Relações sociais")
janela_aberta = True

def Restart_music():
    mixer.music.stop()
    pygame.time.delay(100)
    mixer.music.play(-1)



while janela_aberta :
    pygame.time.delay(50)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

# controle com as setas

    comandos = pygame.key.get_pressed()

    if Aux == 0:



        if comandos[pygame.K_SPACE]:
            Restart_music()
            Aux = 1
            pos_y1 = randint(-300, -180)
            pos_y2 = randint(-800, -300)
            pos_y3 = randint(-1000, -800)
            tempo_segundo = 0


    else:



        if (comandos[pygame.K_RIGHT] or comandos[pygame.K_d]) and x < 530:
            x += velocidade
        if (comandos[pygame.K_LEFT] or comandos[pygame.K_a]) and x > 190:
            x -= velocidade

    # Sistema de detecção de colisão

        if x + 70 > pos_x3 and y < pos_y3 + 189:
            mixer.music.stop()
            Aux = 0

        if x < pos_x1 +80 and y < pos_y1 + 182:
            mixer.music.stop()
            Aux = 0

        if ((x + 80 > pos_x2 and y <= pos_y2+ 152) and (x < pos_x2 + 97 and y <= pos_y2 + 152)):
            mixer.music.stop()
            Aux = 0

    #velocidade e reaparecimento aleatorio
        if pos_y1 >= 580:
            pos_y1 = randint(-1000, -500)
            velocidade1 = randint(5, 20)

        if pos_y2 >= 580:
            pos_y2 = randint(-499, -200)
            velocidade2 = randint(5, 15)

        if pos_y3 >= 580:
            pos_y3 = randint(-3000, -2200)
            velocidade3 = randint(5, 12)

    #marcador de tempo/pontuação
        if timer < 20:
            timer += 1
        else:
            tempo_segundo += 1
            texto = font.render("Pontuação: " + str(tempo_segundo), True, (0, 0, 0), (255, 255, 255))
            timer =0



        pos_y1 += velocidade1
        pos_y2 += velocidade2
        pos_y3 += velocidade3

        janela.blit(fundo,(0, 0))

    #Posicionamento dos objetos na janela

        janela.blit(moto, (x, y))
        janela.blit(carro_1, (pos_x1, pos_y1))
        janela.blit(carro_2, (pos_x2, pos_y2))
        janela.blit(carro_3, (pos_x3, pos_y3))
        janela.blit(texto, pos_texto)

        pygame.display.update()


pygame.quit()