"""
Zip
zip() -> Cria um iteravel (Zip Object) que agrega elemento de cada um soa iteráveis passados como entrada em pares

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

zip1 = zip(lista2, lista1)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma 01_lista, tupla, ou dicionario
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

# Exemplo mais complexo
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'Jose', 'carlos']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utlizar o map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
"""
