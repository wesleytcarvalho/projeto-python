"""
Modulo Collections - Named Tuple

# Recaptulando tupla
tupla = (1, 2, 3)
print(tupla[2])

Named Tuple -> São 02_tuplas diferenciadas onde, especificamos um nome para a mesma e também parametros.

# Importando modulo
from 06_collections import namedtuple

# Precisamos definir o nome e parametro.
# Forma 1 - declaração NamedTuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - declaração NamedTuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - declaração NamedTuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='chow', nome='ray')
print(ray)

#Acessando os dado
# Forma 1
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)
"""



