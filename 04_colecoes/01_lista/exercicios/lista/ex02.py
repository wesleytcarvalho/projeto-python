# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for reais in range(1, 10):
    lista.append(float(input(f'Digite um numero de 1 ate 10, você está na posição {reais} :')))
print(lista)
print(f'A lista inversa é: {lista.reverse()}')
