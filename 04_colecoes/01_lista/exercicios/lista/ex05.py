# Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
valores = []
for i in range(1, 7):
    valores.append(int(input(f'Digite um valor na posição ({i}): ')))
print(f'Os valores da lista são: {valores}')

