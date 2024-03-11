""" https://www.programiz.com/python-programming/decorator

###### Função de maior grandeza - Higher Order Functions - HOF ####

O que isso siguinifica?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do
tipo de funções nos nossos programas.

Obs: Na seção de funções, nos utilizamos isso.

Em Python, as funções são Cidadões de primeira Classe - First Class Citixen

# Exemplo - Definindo as funções

def soma(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Veja que nesta função eu estou passando num1 = a num2 = b e depois eu vou colocar uma função,
# essa função vai saber que estamos querendo fazer algum coisa, neste caso ele leva junto o operador arithmetic
# e muda somente os valores.

# Testando as funcao
print(calcular(4, 3, soma))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicacao))

print(calcular(4, 3, dividir))

# Nested Functions - Funções aninhadas
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).

# Exemplo
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de Você! '))
    return humor() + pessoa

print(cumprimento('Andre'))
print(cumprimento('Raquel'))
print(cumprimento('Jose'))

# Retornando funções de outras função
def faz_me_rir():
    def rir():
        return choice(('hahahah', 'kkkkkk', 'yayaya'))
    return rir

# Testando
rindo = faz_me_rir()
print(rindo)

from random import choice
# Inner Functions (Funções internas / Nested Functions) podemos acessar o escopo de funcoes mais externas.

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkkkkk', 'ddddd', 'dddddd'))
        return f'{risada} {pessoa}'
    return dando_risada

risada = faz_me_rir_novamente('Andre')
print(risada())
print(risada())
"""
