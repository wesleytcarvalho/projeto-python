"""
Sorted
Obs: Não confuda, apesar do nome, com a função sort() que já estudamos em 01_lista. O sort() só funciona em Listas.

- Podemos utlizar o sorted() com qualquer iterável.
- Como o próprio nome já diz o sorted() serve para ordenar, mas na execução do sorted() ele sempre vai criar uma nova exercicios.
- O sorted, SEMPRE retorna uma 01_lista com os elementos do iterável ordenados

print('Exemplo com Listas')
numeros = [6, 1, 8, 2]
print(numeros)
# usando o Sorted
print(sorted(numeros))  # Ordena do menor para o maior
print(numeros)

print('Exemplo com Tuplas')
numeros = (6, 1, 8, 2)
print(numeros)
# usando o Sorted
print(sorted(numeros))  # Ordena do menor para o maior
print(numeros)
# OBS: mas veja que em tupla ele sempre vai retorna uma 01_lista e isso serve para o set também

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

# Adicioando parâmetros no sorted()
print(sorted(numeros, reverse=True))   # Ordenar do maior para menor

# Podemos utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu gosto de bolos", "Eu gosto de pizza"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Gosto de cachorro", "Vou sair hojw"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
# Username Ordenando pelo - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
"""

