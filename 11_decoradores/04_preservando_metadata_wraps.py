""" 
Preservando meta datas com wraps

Metadata -> São dados intrínsecos em arquivo.

wraps -> São funções que envolvem elementos com diversas funcionalidades.

def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra
        print(f'Você está chamado a função {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números.
    return a + b

# print(soma(10, 30))

# Problema
print(soma.__name__)
print(soma.__doc__)


"""
# Resolução do problema
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamado a função {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


# print(soma(10, 30))


# Problema
print(soma.__name__)
print(soma.__doc__)