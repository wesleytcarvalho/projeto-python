"""
Módulo Random e o que são módulos?
- Em python, módulo nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números peseudo-aleatório

# OBS: Existem duas formas de se utilizar um módulo ou função
# Forma 1 - Importando todo o módulo (Não recomendado).

import random

# random() -> Gera um número real pseudoaleatório entre 0 e 1
# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponiveis (Ficarão em memória). Caso você saiba quais funções você precisa utlizar
# deste módulo, então esta não seria a forma ideal de utlização. Nós veremos uma forma melhor na Forma 2

print(random.random())

# Veja que para utlizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo (Forma recomendada)
from random import random
# No importa acima estamos falando: Do módulo random, importe somente a função random

for i in range(5):
    print(random())

# OBS: veja que quando eu importo somente a função específica eu não preciso passar o modulo, somente a função!

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform
for i in range(5):
    print(uniform(1, 7))  # o 7 não é incluído, somente 1.* até 6.*

# randint() -> Gerar um número inteiro pseudo-aleatório entre os valores estabelecidos.
from random import randint
# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=' ') # começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogo = ['papel', 'tesoura', 'pedra']

print(choice(jogo))

from random import shuffle
# shuffle() -> Tem a função de ambaralhar dados
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4']
print(cartas)
shuffle(cartas)
print(cartas)
"""
