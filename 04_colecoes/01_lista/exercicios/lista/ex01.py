# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = []
for r in range(1, 6):
    vetor.append(int(input(f'Digite um número na posição {r}: ')))
print(f'Você digitou: {vetor}')