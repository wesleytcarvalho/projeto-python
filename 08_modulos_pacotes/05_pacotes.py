"""
Pacotes Python
- Módulos -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;
- Pacote -> É um diretório contendo uma coleção de módulos;

OBS:
- Nas versões 2.x do Python, um pacote Python deveria conter dentro dela um arquivo chamado __init__.py
- Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é
utilizado para manter compatibilidade.

Para criar um pacote você precisa escolher na estrutura do Pycharm na hora de criar um diretorio como "Novo -> Pacote Python"
você sabe quando é um pacote quando aparece o __init__.py dentro da estrutura, então basicamente vamos criar uma estrutura

# Vamos criar está estrutura

-Python Package (Uday)
--Python File (Uday1)
--Python File (Uday2)
---Python Package (Academy)
----Python File (Uday3)
----Python File (Uday4)

# Trabalhando com pacotes, funções e modulos
from Uday import (
    Uday1,
    Uday2,
)

from Uday.Academy import (
    Uday3,
    Uday4,
)

print(Uday1.pi)
print(Uday1.funcao1(12, 34))

print(Uday2.função2())
print(Uday2.curso)

print(Uday3.funcao3())
print(Uday4.funcao4())

# Importando somente a função específica
from Uday.Uday2 import função2
print(função2())
"""

