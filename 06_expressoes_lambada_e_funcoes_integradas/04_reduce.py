"""
Reduce
Obs: A partir do python3 a função reduce() não é mais uma função integrada (built-in), Agora temos que importar e utlizar
esta função a partir do módulo 'functools'

Guido Van Rossum: Utlize a função reduce() se você realmente precisar dela, Em todo caso, 99% das vezes um loop for é
mais legível.

Para enteder o reduce()
# Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, .....,an]

# E você tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmtros: a função e o iterável.
reduce(funcao, dados)

A função reduce(), dunciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função do rescultado do passo1 mais o terceiro elemento e guarda o resultado.

    isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn

Ou seja, em cada passo ele aplica a função passando como primeiro argumento a ressultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ....), an)

# Funcionamento na prática
# Vamos utlizar a função reduce() para multiplicar todos os números de uma 01_lista

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Para utlizar o reduce() nós precisamos de uma função que recena dois parâmetros
mult = lambda x, y: x * y

res = reduce(mult, dados)
print(res)

# utlizando um loop normal FOR
res = 1
for n in dados:
    res = res * n
print(res)
"""
