"""
Dictionary Comprehension

Pense no seguinte:
# Se quisermos criar uma 01_lista fazemos:
01_lista = [1, 2, 3, 4]
# Se quisermos criar uma tupla
tupla = (1, 2, 3, 4)
# Se quisermos criar um set(conjunto)
conjunto = {1, 2, 3, 4}
# Se quisermos criar um dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3}

### sintax ####
# Dicionario
{chave:valor for valor in interável}
# exercicios
{valor for valor in interável}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3}
quadrados = {chave : valor ** 2 for chave, valor in numeros.items()}
print(quadrados)

numeros = [1, 2, 3, 4]
print({valor: valor ** 2 for valor in numeros})

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(1, len(chaves))}
print(mistura)

numeros = [1, 2, 3, 4]
print({num: ('par' if num % 2 ==0 else 'impar') for num in numeros})
"""
