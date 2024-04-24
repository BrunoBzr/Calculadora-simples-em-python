import os
import funcoes

# \n - Tecla da barra invertida não funciona.

while True:
    os.system('cls')
    print('---------- CALCULADORA SIMPLES ----------')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')
    op = int(input('>> '))

    if op == 0:
        break
    elif op == 1:
        os.system('cls')
        print('---------- ADIÇÃO ----------\n')
        numero1 = float(input('Informe o primeiro valor: '))
        numero2 = float(input('Informe o segundo valor: '))

        resultado = funcoes.somar(numero1, numero2)

        print(f'\nA soma de {numero1} + {numero2} é igual a {resultado}\n')
        os.system('pause')
    elif op == 2:
        os.system('cls')
        print('---------- SUBTRAÇÃO ----------\n')
        numero1 = float(input('Informe o primeiro valor: '))
        numero2 = float(input('Informe o segundo valor: '))

        resultado = funcoes.subtrair(numero1, numero2)

        print(f'\nA subtração de {numero1} - {numero2} é igual a {resultado}\n')
        os.system('pause')
    elif op == 3:
        os.system('cls')
        print('---------- MULTIPLICAÇÃO ----------\n')
        numero1 = float(input('Informe o primeiro valor: '))
        numero2 = float(input('Informe o segundo valor: '))

        resultado = funcoes.multiplicar(numero1, numero2)

        print(f'\nA multiplicação de {numero1} * {numero2} é igual a {resultado}\n')
        os.system('pause')
    elif op == 4:
        os.system('cls')
        print('---------- DIVISÃO ----------\n')
        numero1 = float(input('Informe o primeiro valor: '))
        numero2 = float(input('Informe o segundo valor: '))

        resultado = funcoes.dividir(numero1, numero2)

        print(f'\nA divisão de {numero1} / {numero2} é igual a {resultado}\n')
        os.system('pause')
    else:
        print('Opção invalida!')
