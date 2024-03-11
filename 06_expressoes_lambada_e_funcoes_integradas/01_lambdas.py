"""
Utilizando Lambdas
- Conhecidas por expressões Lambdas, ou simplesmente lambada, são funções sem nome, ou seja, funções anônimas.


# Funções normal em python
def soma(x):
    return 3 * x + 1
print(soma(2))
print(soma(5))


# Expressões Lambda
lambda x: 3 * x + 1

# como utilizar a expressões lambda?
# NOTA: esta não é a maneira correta de se utilizar lambda, mas é um exemplo
calc = lambda x: 3 * x + 1
print(calc(2))
print(calc(5))

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Andre ', ' CarvAlho '))
NOTA:
# - O strip() tira espaços do inicial e do fim se alguém coloca
# - title() deixa a primeira letra da frase em maiúsculo e deixo o resto como m


# Em funções Python podemos ter nenhuma ou várias entradas, em Lambdas também.
amar = lambda: 'Ola Python, como é bom aprender'
uma = lambda x: 3 * x * 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3/(1/x+1/y+1/z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Obs: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo
autores = ['Andre Tibucio', 'Lara Btera', 'Andre Soares', 'Jose Eduardo', 'Lindaura Carioca']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Funções Quadrática
# f(x) = a * x ** 2 + 1 x + c
# Definindo a função

def geradora_funcao_quadratica(a, b, c):
   '''Retornando a função # f(x) = a * x ** 2 + b * x + c'''
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
"""
