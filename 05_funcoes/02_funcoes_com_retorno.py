"""
Funções com Retorno

numero = [1, 2, 3]
ret_pop = numero.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numero)
print(f'Retorno de print: {ret_pr}')

Obs: Em python, quando uma função não retorna valor, o rotorno é None


def quadrado_de_7():
    return 7 * 7

Obs: Funções python que retornam valores, devem retornar estes valores com a palavra reservada return.
ele irá calcula 7 * 7 e entregar somente o valor 49.  


# Criamos uma variável para receber o retorno da função, mas veja que isso não é uma boa pratica, 
# somente com uma unica linha eu consegui fazer. 
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()+1}')

# Refatorando da primera função
def diz_oi():
    return 'oi'

print(diz_oi())

OBS: --- Sobre a palavra reservda return -----
1 - Ela finaliza a função, ou seja, ela sai da execução da função depois do retorn, se você inserir qualquer 
coisa abaixo, não vai ser executado;


# Exemplo 1
def diz_oi():
    print('Este é o print antes do retorn')
    return 'oi'
    print('Este print esta depois do retorn') 
print(diz_oi())


2 - Podemos ter, em uma função, diferente returns;


# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

    
print(nova_funcao())

3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores:

# Exemplo 3
import os

os.system('clear')
def outra_funcao():
    return 2, 3, 4 ,5

# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)
print(outra_funcao())

# Vamos criar uma função para jogar a moeda
from random import random

def jogo_moeda():
    # Gera um número número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa' 

print(jogo_moeda())


"""
# Erros comuns na utlização do retorno, que na verdade nem é erro, mas sim codificação desenecessária
def eh_impart():
    numero = 5
    if numero % 2 != 0:
        return True
    return False
    
    print(eh_impart())