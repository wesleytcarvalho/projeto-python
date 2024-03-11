# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = [float(input('Digite a primeira NOTA: ')),
         float(input('Digite a segunda NOTA: ')),
         float(input('Digite a terceira NOTA: ')),
         float(input('Digite a quarta NOTA: '))
         ]
soma = sum(notas)
print(f'A média é: {soma/2}')
