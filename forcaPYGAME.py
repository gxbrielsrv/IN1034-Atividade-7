import pygame
import random

def forcaPYGAME():
    pygame.init()

    tela = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption("Forca")

    fonte = pygame.font.SysFont(None, 50)

    palavras = ['arroz', 'batata', 'banana', 'lasanha', 'presunto']


    palavra = random.choice(palavras)
    chute_correto = ['_'] * len(palavra)
    letras_erradas = []
    vidas = 6
    caracteres_digitados = ""
    fim = False

    def desenhar_forca(vidas):
        pygame.draw.line(tela, (255,255,255), (100,500), (300,500), 5)
        pygame.draw.line(tela, (255,255,255), (200,500), (200,100), 5)
        pygame.draw.line(tela, (255,255,255), (200,100), (400,100), 5)
        pygame.draw.line(tela, (255,255,255), (400,100), (400,150), 5)

        erros = 6 - vidas

        if erros >= 1:
            pygame.draw.circle(tela, (255,255,255), (400,180), 30, 3)
        if erros >= 2:
            pygame.draw.line(tela, (255,255,255), (400,210), (400,350), 3)
        if erros >= 3:
            pygame.draw.line(tela, (255,255,255), (400,250), (350,300), 3)
        if erros >= 4:
            pygame.draw.line(tela, (255,255,255), (400,250), (450,300), 3)
        if erros >= 5:
            pygame.draw.line(tela, (255,255,255), (400,350), (350,420), 3)
        if erros >= 6:
            pygame.draw.line(tela, (255,255,255), (400,350), (450,420), 3)

    rodando = True
    while rodando:
        tela.fill((3, 78, 89))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:

                # reinicio
                if evento.key == pygame.K_SPACE:
                    palavra = random.choice(palavras)
                    chute_correto = ['_'] * len(palavra)
                    letras_erradas = []
                    vidas = 6
                    caracteres_digitados = ""
                    fim = False

                if fim == False:

                    if evento.key == pygame.K_RETURN:
                        chute = caracteres_digitados

                        if chute != "":

                            # chute da palavra
                            if len(chute) > 1:
                                if chute == palavra:
                                    chute_correto = list(palavra)
                                else:
                                    vidas -= 1

                            #chute da letra
                            else:
                                if chute in palavra:
                                    cont = 0
                                    while cont < len(palavra):
                                        if palavra[cont] == chute:
                                            chute_correto[cont] = chute
                                        cont += 1
                                else:
                                    if chute not in letras_erradas:
                                        letras_erradas.append(chute)
                                        vidas -= 1

                        caracteres_digitados = ""

                    elif evento.key == pygame.K_BACKSPACE:
                        caracteres_digitados = caracteres_digitados[:-1]

                    else:
                        caracteres_digitados += evento.unicode

        

        
        mostrar = ''
        cont = 0
        while cont < len(chute_correto):
            mostrar += chute_correto[cont] + ' '
            cont += 1

        texto = fonte.render(mostrar, True, (255,255,255))
        tela.blit(texto, (50, 50))

        # mostrar os erros
        mostrar_erradas = ''
        cont = 0
        while cont < len(letras_erradas):
            mostrar_erradas += letras_erradas[cont] + ' '
            cont += 1

        erradas = fonte.render("Erradas: " + mostrar_erradas, True, (255,0,0))
        tela.blit(erradas, (500, 120))

        

        # oque foi digitado
        entrada = fonte.render("Digite: " + caracteres_digitados, True, (255,255,255))
        tela.blit(entrada, (50, 500))

        desenhar_forca(vidas)

        
        if vidas <= 0:
            reinicio = fonte.render("Perdeu! Aperte a tecla 'ESPAÇO' para reiniciar", True, (255,0,0))
            tela.blit(reinicio, (250, 600))
            fim = True

        if '_' not in chute_correto:
            reinicio = fonte.render("Ganhou! Aperte tecla 'ESPAÇO' para reiniciar", True, (0,255,0))
            tela.blit(reinicio, (250, 600))
            fim = True

        pygame.display.update()

    pygame.quit()

forcaPYGAME()