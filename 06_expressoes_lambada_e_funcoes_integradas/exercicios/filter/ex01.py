"""
estou criando esta funcão para dizer se x é menor que 18
- False = nao vai fazer nada
- True, ele vai mostrar os maiores numeros: [56, 23, 75, 19]
"""


def minha_funcao(x):
    if x <= 18:
        return False
    else:
        return True


idade = [1, 3, 56, 7, 4, 8, 23, 75, 18, 19]

idades = filter(minha_funcao, idade)

print(list(idades))