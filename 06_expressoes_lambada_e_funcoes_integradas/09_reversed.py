"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas Listas.
- A função reverse() só funciona em Listas.
- Já a função reversed() funciona em qualquer iterável. Sua função é inverter o iterável.

01_lista = [1, 3, 5, 6, 84, 0]
res = reversed(01_lista)
print(type(res))

# Podemos converter o elemento retornando para uma Listas, Tupla, Condunto(Set)
# Listas
print(list(reversed(01_lista)))

# Tupla
print(tuple(reversed(01_lista)))

# Conjunto(Set)
# Obs em conjuntos não definimos a ordem dos elementos
print(set(reversed(01_lista)))

# Podemos interar interar sobre o reversed
for letra in reversed('Uday Tecnologia'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Uday Academy'))))

# já vimos como fazer isso mais fácil com o slice de strings
print('Uday Univesity'[::-1])

# Podemos também utlizar o raversed() para fazer um loop for reverso
for n in reversed(range(1, 10)):
    print(n, end='')

# Apesar que também já vimos como fazer isso utlizando o prório range()
for n in range(9, -1, -1):
    print(n, end='')
"""
