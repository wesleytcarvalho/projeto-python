"""
Decorators com diferentes assinaturas

# Vamos tentar examinar isso
# Vamos imagina que precisamos criar uma funcao principal que vai ser utilizadas por outras funcoes.
# 1 - Eu vou passar uma funcao como argumento
# 2 - Vou criar outra funcao dentro da funcao gritar
# 3 - Essa segunda funcao vai ter como argumento o nome
# 4 - Veja que eu vou retornar a funcao com um nome


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


# Exemplo 1
@gritar
def saudacao(nome):
    return f'Ola, eu sou o/a {nome}'


# Exemplo 2
@gritar
def odenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhando de {acompanhamento}, por favor.'

# Testando
# print(saudacao('Angelina'))

print(odenar('Picanha', 'Batara'))

# A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou (oa) {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Andre'))

print(ordenar('Picanha', 'Batata frinta'))

# OBS: vale lembrar que podemos utlizar paramentros nomeados
print(ordenar(principal='Batara frita', acompanhamento='Picanha'))


# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna



@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))

print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churraco'))
"""


















