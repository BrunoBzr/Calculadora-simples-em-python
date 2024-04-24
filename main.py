import os

# \n - Tecla da barra invertida não funciona.

while True:
    os.system('clear')
    print('---------- CALCULADORA SIMPLES ----------')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')
    op = int(input('>> '))

    print(op)
