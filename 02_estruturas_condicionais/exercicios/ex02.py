# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número é Positivo com {num}')
else:
    print(f'O número é Negativo com {num}')