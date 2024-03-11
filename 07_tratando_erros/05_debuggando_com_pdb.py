"""
Debuggnado com PDB
BUG -> siguinifica problema e como podemos resolver estes problemas.

# Exemplo 1 - Algumas pessoas debuga um codigo usando a função print(), mão não seria uma prática legal.
def dividir(a, b):
    print(f'a={a}, b={b} ')  # Esta linha estamos debugando a entrada de valores
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'

print(dividir(4, 2))

# Existem formas mais profissionais de se fazer esse 'debug' utlizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utlizando
# o PDB - Python Debugger uma biblioteca

# Exemplo 2 - PDB Python Debugger
# Para utlizar o Python Debugger, precisamos* importa a biblioteca pdb e então utlizar o função set_trace()

# Comandos básicos do PDB
# l (exercicios onde estamos no codigo)
# n (Próxima linha)
# p (Imprimir variável)
# c (continua a execução - finaliza o debugging )

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 3 - PDB Python Debugger
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utlizado durante o desenvolvimento. Custumamos realizar todos os imports de biblioteca
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo 4 - PDB Python Debugger
# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in(integrada) no python chamada breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utlizado durante o desenvolvimento. Custumamos realizar todos os imports de biblioteca
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# OBS: Cuidado com conflitos entre os nomes de variáveis e os comandos do pdb
# Exemplo: Vamos imagina que estmos criando uma função e você colocar como paramentro na função as letras
# l, n, p, c provavelmente na hora de executar o debugg vai dar conflito porque o PDB também usa estas letras

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 4, 6))
"""



