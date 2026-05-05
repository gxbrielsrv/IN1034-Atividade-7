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

calculadora()