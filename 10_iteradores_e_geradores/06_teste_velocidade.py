"""
Teste de velocidade com expressões Geradoras

# Generators (Geradores)
def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1)  # Generator object

print(next(ge1))
print(next(ge1))
print(next(ge1))


# Generator Expression
ge2 = (num for num in range(1, 10))
print(ge2)  # Generator object

print(next(ge2))
print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade
import time

gen_inicio = time.time()  # Tempo que iniciou
print(sum(num for num in range(1000000000)))  # teste com range de 100 milhoes
gen_tempo = time.time() - gen_inicio  # Tempo que acabou

# List comprehension
gen_inicio = time.time()  # Tempo que iniciou
print(sum([num for num in range(1000000000)]))  # teste com range de 100 milhoes
list_tempo = time.time() - gen_inicio  # Tempo que acabou

print(f'Generator Expression levou {gen_tempo}')
print(f'List comprehension levou {list_tempo}')
"""
