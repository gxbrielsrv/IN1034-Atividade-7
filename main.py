import math
import random

#PEDRA, PAPEL E TESOURA
def pedra_papel_tesoura():
    pontosuser = 0
    pontosbot = 0
    while True:
    
        escolhas = ['pedra','papel','tesoura']
        escolha = input('Escolha sua jogada (pedra,papel ou tesoura): ')
        escolhabot = random.choice(escolhas)

        print(f'A escolha do bot é: {escolhabot}')

        if escolha == escolhabot:
            print('------EMPATE-----')
        elif escolha == 'papel' and escolhabot == 'pedra' or \
        escolha == 'pedra' and escolhabot == 'tesoura' or \
        escolha == 'tesoura' and escolhabot == 'papel':
            print('-----VOCÊ GANHOU!-----')
            pontosuser += 1
        else:
            print('-----VOCÊ PERDEU!-----')
            pontosbot += 1
        print('=' * 50)
        print('Pontuaçao final:')
        print(f'Pontos do bot: {pontosbot}')
        print(f'Pontos do usuario: {pontosuser}')
        print('=' * 50)
        continuar = input('Mais uma rodada(sim/nao)? ')
        if continuar == 'sim':
            print('Ok... Boa sorte!')
        else:
            print('Tudo bem! Até a proxima!')
            break 

#pedra_papel_tesoura()



#JOGO DA FORCA
def forca():
    palavras = ['arroz', 'batata', 'banana', 'lasanha', 'presunto']
    tema = 'Comidas'
    while True:
        palavra = random.choice(palavras)
        chute_correto = '_' * len(palavra)
        vidas = 6

        print('=== JOGO DA FORCA ===')
        print(f'==> Tema: {tema} ')
        while vidas > 0 and '_' in chute_correto:
            print('Palavra:', chute_correto)
            print('Vidas:', vidas)

            chute = input('Digite uma letra ou a palavra inteira: ')

            valido = True
            for letra in chute:
                if letra < 'a' or letra > 'z':
                    valido = False

            if valido == False:
                print('Digite apenas letras!')
                

            #chute de uma palavra
            if len(chute) > 1:
                if chute == palavra:
                    chute_correto = palavra
                    print('Você acertou a palavra. Parabéns!')
                    break
                else:
                    print('Errou o chute!')
                    vidas -= 1
                    

            # chute de uma letra 
            letra =  chute

            if letra in palavra:
                print('Acertou!')

                nova = ''
                cont = 0

                while cont < len(palavra):
                    if palavra[cont] == letra:
                        nova += letra
                    else:
                        nova += chute_correto[cont]
                    cont += 1

                chute_correto = nova
            else:
                print('Errou!')
                vidas -= 1

        if '_' in chute_correto:
            print('Você perdeu!')
            print('A palavra era:', palavra)
        else:
            print('Você ganhou!')
            print('Palavra:', palavra)

        jogar = input('Quer jogar de novo? (sim/nao): ')
        if jogar == 'nao':
            print('Tudo bem. Te vejo na proxima!!')
            break

#forca()

