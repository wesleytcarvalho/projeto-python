"""
2. Escreva um programa Python para criar uma função que receba um argumento, e esse argumento será multiplicado por um número desconhecido.
Exemplo de resultado:
Dobre o número de 15 = 30
Triplique o número de 15 = 45
Quádruple o número de 15 = 60
Quintuplique o número 15 = 75
"""

# dobro = lambda x: 2 * x
# print(f'Dobro: {dobro(15)}')

# triplique = lambda x: 3 * x
# print(f'Triplo: {triplique(15)}')

# quadruple = lambda x: 4 * x
# print(f'Quádruple: {quadruple(15)}')

# quintuplique = lambda x: 5 * x
# print(f'Quintuplique: {quintuplique(15)}')

# também pode ser feito assim
def func_completo(n):
    return lambda x: x * n

result = func_completo(2)
print(f'Duplicando o numero: {result(15)}')