"""
Objetivo do cod: Programa desenvolvido para resolver contas matematicas.
Autor: Marcos Gregório
"""


import math
import time

print('***********Calculadora em Python***********')
n4 = 1
while n4 == 1:
    nome = input("Qual seu nome?")
    print(f'Seja bem vindo, {nome}')
    print('Selecione o número da operação desejada:\n' +
          '1 - Soma\n' +
          '2 - Subtração\n' +
          '3 - Multiplicação\n' +
          '4 - Divisão')
    n2 = int(input(f'Então, vamos realizar qual tipo de operação? (1, 2, 3 ou 4):'))
    # n3 = [n2]
    if n2 == 1:
        print("Ok, você digitou o nº1, então vamos iniciar a soma")
        Continuar = 's'
        while Continuar.lower() == 's':
            num1 = int(input('Primeiro informe um número: '))
            num2 = int(input('Agora, informe o segundo número: '))
            tot_1 = num1 + num2
            print('Calculando...')
            time.sleep(2)
            print('Só mais um momento...')
            time.sleep(2)
            print('Agrupando os dados...')
            time.sleep(2)
            print(f'Você informou os números, {num1} e {
                  num2}, e a soma dos valore é {tot_1}.')
            Continuar = str(
                input('Deseja fazer mais alguma operação de soma? Se sim digite S, se não N."'))
    elif n2 == 2:
        print("Ok, você digitou o nº2, então vamos iniciar a subtração")
        Continuar2 = 's'
        while Continuar2.lower() == 's':
            num1 = int(input('Primeiro informe um número: '))
            num2 = int(input('Agora, informe o segundo número: '))
            tot_2 = num1 - num2
            print('Calculando...')
            time.sleep(2)
            print('Só mais um momento...')
            time.sleep(2)
            print('Agrupando os dados...')
            time.sleep(2)
            print(f'Você informou os números, {num1} e {
                num2}, e a multiplicação dos valore é {tot_2}.')
            Continuar2 = str(
                input('Deseja fazer mais alguma operação de subtração? Se sim digite S, se não N."'))
    elif n2 == 3:
        print("Ok, você digitou o nº3, então vamos iniciar a multiplicação")
        Continuar3 = 's'
        while Continuar3 == 's':
            num1 = int(input('Informe o primeiro número: '))
            num2 = int(input('Informe o segundo número: '))
            tot_2 = num1 * num2
            print('Calculando...')
            time.sleep(2)
            print('Só mais um momento...')
            time.sleep(2)
            print('Agrupando os dados...')
            time.sleep(2)
            print(f'Você informou os números, {num1} e {
                num2}, e a Subtração dos valore é {tot_2}.')
            Continuar3 = str(
                input('Deseja fazer mais alguma operação de multiplicação? Se sim digite S, se não N."'))
    elif n2 == 4:
        print("Ok, você digitou o nº4, então vamos iniciar a divisão")
        Continuar4 = 's'
        while Continuar4 == 's':
            num1 = int(input('Informe o primeiro número: '))
            num2 = int(input('Informe o segundo número: '))
            tot_2 = num1 / num2
            print('Calculando...')
            time.sleep(2)
            print('Só mais um momento...')
            time.sleep(2)
            print('Agrupando os dados...')
            time.sleep(2)
            print(f'Você informou os números, {num1} e {
                  num2}, e a divisão dos valore é {tot_2}.')
            Continuar4 = str(
                input('Deseja fazer mais alguma operação de multiplicação? Se sim digite S, se não N."'))
    else:
        print("Ixi, infelizmente você digitou um numero inválido, tente novamente")
        n4 = int(input('Deseja fazer mais alguma operação?, Se sim - 1, Se não 2: '))
print('Muito obrigado, volte sempre')
