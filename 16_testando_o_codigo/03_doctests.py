"""
Doctests

Doctests são testes que colocamos na docsstring das funções/metodo Python

para rodar um test do doctest usamos o comando abaixo
# python -m doctest -v nome_do_modulo.py


# Saida

4
Trying:
    soma(1, 3)
Expecting:
    4
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Veja acima que podemos colocar varios testes.
# Podemos fazer varios tipos de tests


def soma(a, b):
    #soma os números a e b
    
    # >>> soma(4, 3)
    #7

    #>>> soma(10, 4)
    14
    
    #return a + b


print(soma(4, 3))
print(soma(10, 4))



# Outros exemplos, aplicando o TDD
def duplicar(valores):
    # duplicar os valores em uma lista
    
    # >>> duplicar([1, 2, 3, 4])
    # [2, 4, 6, 8]

    # >>> duplicar([])
    # []

    # >>> duplicar(['a', 'b', 'c',])
    # ['aa', 'bb', 'cc',]

    # >>> duplicar([True, None])
    # Traceback (most recent call last):
        ...
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    
    # return [2 * elemento for elemento in valores]



# Erro inesperado...

def fala_oi():
    # Fala oi
    
    # >>> fala_oi()
    # 'oi'
    # return "oi"

# Pelo fato de estarmos utilizando aspas duplas para documentar, vamos precisar inserir aspas
# simples em 'oi' no teste
"""


