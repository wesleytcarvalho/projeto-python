"""
Teste de memoria com Generators

# Sequencia de Finomacci
1, 1, 2, 3, 5, 8, 13

# Funcao usando Listas, 449MB de memoria sendo utilizada

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1 -
for n in fib_lista(100000):
    print(n)

# Função usando generator
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 - Geradores nessa execução ele usou somente 3MB enquanto o teste 1 foi 449MB
for n in fib_gen(100000):
    print(n)

# Então, a utilização de Geradores não tem comparação ele economiza muita memória, Reveja e estude mais 
estas aulas.
"""


