import math

#PEDRA, PAPEL E TESOURA
import random

def PPT():
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

PPT()













#CALCULADORA
def calculadora():
    
    print('Operadores disponiveis: ')
    print('=' * 30)
    print('+ Adição')
    print('- Subtração')
    print('X Multiplicação')
    print('/ Divisão')
    print('=' * 30)

    a = float(input('Insira o valor do primeiro número: '))
    operador = input('Insira o operador desejado: ')
    b = float(input('Insira o valor do segundo número: '))

    if operador == '+':
        resultado = a+b
        print(f'{a} + {b} = {resultado}')
    elif operador == '-':
        resultado = a-b
        print(f'{a} - {b} = {resultado}')
    elif operador == 'X':
        resultado = a*b
        print(f'{a} X {b} = {resultado}')
    elif operador == '/':
        resultado = a/b
        print(f'{a} / {b} = {resultado}')
    else:
        print('Operação inválida')

    while True:

        entrada = input('Utilizar  o resultado da ultima operação? (sim/nao): ')

        if entrada != 'sim':
            print('Ok')
            resultado = a = float(input('Insira o valor de a: '))
            
        print('Operadores disponiveis: ')
        print('=' * 30)
        print('+ Adição')
        print('- Subtração')
        print('X Multiplicação')
        print('/ Divisão')
        print('=' * 30)

        novooperador = input('Insira o novo operador desejado: ')
        c = float(input('Insira o valor do segundo número: '))
        
        ultimaoperacao = resultado

        if novooperador == '+':
            resultado = ultimaoperacao + c
            print(f'{ultimaoperacao} + {c} = {resultado}')
        elif novooperador == '-':
            resultado = ultimaoperacao - c
            print(f'{ultimaoperacao} - {c} = {resultado}')
        elif novooperador == 'X':
            resultado = ultimaoperacao * c
            print(f'{ultimaoperacao} X {c} = {resultado}')
        elif novooperador == '/':
            resultado = ultimaoperacao/c
            print(f'{ultimaoperacao} / {c} = {resultado}')
        else:
            print('Operação inválida')

#calculadora()