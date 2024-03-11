"""
Um otimo exemplo:
https://www.hashtagtreinamentos.com/all-e-any-no-python

Any e All

all() -> Retorna True se ordem dos elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplo 1 all()
print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros, qual será o resultado True ou False? Claro que é False
porque o 0 é False
print(all([1, 2, 3, 4])) # True
print(all([])) # True
print(all((1, 2, 3, 4)))# True
print(all(({0, 1, 2, 3, 4}))) # False

# Exemplo 2 all()
nomes = ['Carla', 'Camila', 'Carolina']
print(all([nome[0] == 'C' for nome in nomes]))

# Obs: Um iterável vazio convertido em boolean é False, mas o all() concidera como como TRUE
print(all(letra for letra in 'eio' if letra in 'aeiou'))

# any() -> Retorna True se qualquer elemento do interável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 3, 4])) # True
print(any([0, False, {}, ()])) # False

nomes = ['Carla', 'Camila', 'Carolina']
print(any([nome[0] == 'C' for nome in nomes]))
print(any([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
"""
