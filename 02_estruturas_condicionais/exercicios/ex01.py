# Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior com número: {num1}')
elif num1 < num2:
    print(f'O segundo número é maior com o número: {num2}')
else:
    print(f'Não tem número maior/menor porque os números são iguais com {num1} e {num2}')
