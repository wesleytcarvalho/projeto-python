"""
PEP8 - Python Enhancement Proposal (São propostas de melhorias para a linguagem python)

(Você verifica o dilema do python)
import this

A ideia da PEP8 é que possamos escrever código Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculos, separados por underline para funções ou variaveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impart = 3


[3] - Utilize 4 espaços para identação!

if 'a' in ('banana'):
    print('tem')


[4] - Linhas em branco
- Seprar funções e definições de classe com duas linhas em branco;
- Métodos numa classe devem ser seprados com uma única linha em branco;

[5] - Imports
- import devem ser sempre feito em linhas separadas;

# import Errado
import sys, os

# Import Certo
import os
import sys

# Não há problemas em utlizar:
from types import StringType, ListType

# Caso tenha muito importe de um mesmo pacote recomenda-se fazer:

from types import (
    StringType
    ListType
    SetType
    OutroType
)

# Import devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e antes de
# constantes ou variaveis globais

[6] - Espaços em expressões e instrucões
# Não faça:
funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})
"""









