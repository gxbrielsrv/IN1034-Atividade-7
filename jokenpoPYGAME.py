import pygame
import random
def pedra_papel_tesouraPYGAME():
    pygame.init()

    tela = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption("Pedra Papel Tesoura")

    fonte = pygame.font.SysFont(None, 40)

    #imagens
    pedra = pygame.image.load("pedra1.png")
    papel = pygame.image.load("papel1.png")
    tesoura = pygame.image.load("tesoura1.png")
    pedra = pygame.transform.scale(pedra, (120,120))
    papel = pygame.transform.scale(papel, (120,120))
    tesoura = pygame.transform.scale(tesoura, (120,120))

    #botoes
    botao_pedra = pedra.get_rect(topleft=(100, 450))
    botao_papel = papel.get_rect(topleft=(340, 450))
    botao_tesoura = tesoura.get_rect(topleft=(580, 450))

    #variasveis
    pontos_usuario = 0
    pontos_bot = 0
    escolha_usuario = ""
    escolha_bot = ""
    resultado_texto = ""
    fim = False
    texto_finalizar = fonte.render("Aperte BACKSPACE para finalizar o jogo", True, (0,0,0))
    while True:
        tela.fill((119, 125, 133))
        tela.blit(texto_finalizar, (200, 800))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()                
            #reinicio
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pontos_usuario = 0
                    pontos_bot = 0
                    escolha_usuario = ""
                    escolha_bot = ""
                    resultado_texto = ""
                    fim = False

                #acabar o jogo
        
                if evento.key == pygame.K_BACKSPACE:
                    fim = True
            if evento.type == pygame.MOUSEBUTTONDOWN and not fim:
                mouse = pygame.mouse.get_pos()

                if botao_pedra.collidepoint(mouse):
                    escolha_usuario = "pedra"
                elif botao_papel.collidepoint(mouse):
                    escolha_usuario = "papel"
                elif botao_tesoura.collidepoint(mouse):
                    escolha_usuario = "tesoura"

                #regras
                if escolha_usuario != "":
                    escolha_bot = random.choice(["pedra","papel","tesoura"])

                    if escolha_usuario == escolha_bot:
                        resultado_texto = "EMPATE"
                    elif (escolha_usuario == "pedra" and escolha_bot == "tesoura") or \
                        (escolha_usuario == "papel" and escolha_bot == "pedra") or \
                        (escolha_usuario == "tesoura" and escolha_bot == "papel"):
                        resultado_texto = "VOCÊ GANHOU A RODADA"
                        pontos_usuario += 1
                    else:
                        resultado_texto = "BOT GANHOU A RODADA"
                        pontos_bot += 1

        if escolha_usuario != "":
            disputa = fonte.render(f"{escolha_usuario}  VS  {escolha_bot}", True, (0,0,0))
            tela.blit(disputa, (250, 100))

            resultado = fonte.render(resultado_texto, True, (200,0,0))
            tela.blit(resultado, (300, 150))

        #placar
        placar = fonte.render(f"Você {pontos_usuario} x {pontos_bot} Bot", True, (0,0,0))
        tela.blit(placar, (270, 50))

        if not fim:
            tela.blit(pedra, botao_pedra)
            tela.blit(papel, botao_papel)
            tela.blit(tesoura, botao_tesoura)

        #resultado 
        texto_reinicio = fonte.render("Aperte ESPAÇO para reiniciar", True, (0,0,0))
        if fim:
            tela.blit(texto_reinicio, (200, 600))

            if pontos_usuario > pontos_bot:
                vencedor = "VOCÊ VENCEU O JOGO!"
            elif pontos_bot > pontos_usuario:
                vencedor = "BOT VENCEU O JOGO!"
            else:
                vencedor = "EMPATE!"

            texto_fim = fonte.render(vencedor, True, (0,0,0))
            tela.blit(texto_fim, (250, 250))

        pygame.display.update()

pedra_papel_tesouraPYGAME()