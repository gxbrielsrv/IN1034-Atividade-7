import pygame
import random

pygame.init()

# tamanho da tela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pedra Papel Tesoura")


cinza = (119, 125, 133)
preto = (0,0,0)
vermelho = (200,0,0)

fonte = pygame.font.SysFont(None, 40)

#imagens
pedra = pygame.image.load("pedra1.png")
papel = pygame.image.load("papel1.png")
tesoura = pygame.image.load("tesoura1.png")
pedra = pygame.transform.scale(pedra, (120,120))
papel = pygame.transform.scale(papel, (120,120))
tesoura = pygame.transform.scale(tesoura, (120,120))

#botoes
pedra_rect = pedra.get_rect(topleft=(100, 450))
papel_rect = papel.get_rect(topleft=(340, 450))
tesoura_rect = tesoura.get_rect(topleft=(580, 450))

final_rect = pygame.Rect(300, 350, 200, 50)

#variasveis
pontos_user = 0
pontos_bot = 0
escolha_user = ""
escolha_bot = ""
resultado_texto = ""
fim = False

while True:
    tela.fill(cinza)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and not fim:
            mouse = pygame.mouse.get_pos()

            if pedra_rect.collidepoint(mouse):
                escolha_user = "pedra"
            elif papel_rect.collidepoint(mouse):
                escolha_user = "papel"
            elif tesoura_rect.collidepoint(mouse):
                escolha_user = "tesoura"

            #regras
            if escolha_user != "":
                escolha_bot = random.choice(["pedra","papel","tesoura"])

                if escolha_user == escolha_bot:
                    resultado_texto = "EMPATE"
                elif (escolha_user == "pedra" and escolha_bot == "tesoura") or \
                     (escolha_user == "papel" and escolha_bot == "pedra") or \
                     (escolha_user == "tesoura" and escolha_bot == "papel"):
                    resultado_texto = "VOCÊ GANHOU"
                    pontos_user += 1
                else:
                    resultado_texto = "BOT GANHOU"
                    pontos_bot += 1

        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if final_rect.collidepoint(pygame.mouse.get_pos()):
                fim = True

    
    if escolha_user != "":
        texto_vs = fonte.render(f"{escolha_user}  VS  {escolha_bot}", True, preto)
        tela.blit(texto_vs, (250, 100))

        resultado = fonte.render(resultado_texto, True, vermelho)
        tela.blit(resultado, (300, 150))

    #placar
    placar = fonte.render(f"Você {pontos_user} x {pontos_bot} Bot", True, preto)
    tela.blit(placar, (270, 50))

    
    if not fim:
        tela.blit(pedra, pedra_rect)
        tela.blit(papel, papel_rect)
        tela.blit(tesoura, tesoura_rect)

        pygame.draw.rect(tela, vermelho, final_rect)
        texto_final = fonte.render("FINALIZAR", True, cinza)
        tela.blit(texto_final, (330, 360))

    #resultado
    if fim:
        if pontos_user > pontos_bot:
            vencedor = "VOCÊ VENCEU O JOGO!"
        elif pontos_bot > pontos_user:
            vencedor = "BOT VENCEU O JOGO!"
        else:
            vencedor = "EMPATE!"

        texto_fim = fonte.render(vencedor, True, preto)
        tela.blit(texto_fim, (250, 250))

    pygame.display.update()