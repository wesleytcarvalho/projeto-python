"""
Trabalhando com módulos builtin (módulos integrados, que vem instalado no Python), mas não vem carregado na memória
- Você pode achar a documentação direto na documentação do python chamado como (Python Module Index)
_________________________
|Python|Módulos builtins|
-------------------------
https://docs.python.org/3/py-modindex.html

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

# Utilizando alias (apelidos) para função
from random import randint as rdi
print(rdi(1, 3))

# Podemos importar todas as funções de um módulo com o "*"
from random import *
print(random())

# importando todo o módulo
import random
print(random.random())

# Podemos trabalhar com multiplos apelidos e funcoes
from random import randint as rdi, shuffle as emb
print(rdi(1, 3))

01_lista = ['Uday', 'TC']
emb(01_lista)
print(01_lista)

# Costumamos a utilização tuple para colocar múltiplos imports de um mesmo múdulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(1, 4))

01_lista = ['Uday', 'TC']
shuffle(01_lista)
print(01_lista)

print(choice('Academy'))
"""
