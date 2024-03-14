"""
Entendendo o *args
- O *args é um parâmetro, como outro qualquer. Isso siguinifica que você poderá chamar de qualquer coisa,
desde que começe com asterisco.

Exemplos:
- Poderiamos chamar o parâmetro como *xis ou qualquer outro nome só precisar ter o asterisco na frete, mas por convensão
da comunidade para definir se chama *args

Mas o que é *args?
- O parâmetro *args é utilizado na função como parâmetro, coloca os valores extras informados como entrada em uma tupla.
Então lembre-se que tupla são imutáveis.


# Exemplo de função comum


def soma(num1, num2, num3):
    return num1 + num2 + num3


print(soma(23, 45, 67))
OBS: Se inserirmos 2 parametros sabemos que vamos ter typeError, porque ele espera 3 parametros

# Exemplo de *args


def soma(*args):
    return sum(args)


print(soma(1, 43, 564, 356, 3354,))

# Outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Uday' in args and 'Academy' in args:
        return 'Bem-vindo Uday!'
    return 'Eu não tenho certeza que é você ...'

print(verifica_info(True))
print(verifica_info(1,3,3))
print(verifica_info('Uday', 'Academy'))

# Outro exemplo
# Imagina que temos uma lista e queremos passar para a função soma, irá da TypeError

def soma(*args):
    return sum(args)


numero = [1, 2, 3, 4, 5, 6, 7, 8]


# print(soma(numero))


# Para resolver isso acima usamos o desempacotado
# fazendo assim:
# num1, num2, num3, num4, num5, num6, num7, num8 = numero
# print(soma(num1, num2, num3, num4, num5, num6, num7, num8))

# Mas para fazer o desempacotamento existe uma forma mais interessante
print(soma(*numero))

OBS: O asterisco serve para informarmos para o Python que estamos passando como argumento
uma coleção de dados. Desta forma, ele saberá que precisará antes desmpacotar os dados
"""

