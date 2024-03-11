"""
Generetors Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple comprehension...porque elas se chamam Generators

# Este é um exemplo da aula passa usando ANY e List Comprehension
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))


# Exemplo de uso do generator
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(tuple(res))

# Qual é a utilizade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Andre' ocupa na memória. Quanto maior a string, mais espaço oculpa.
print(getsizeof('Andre'))
print(getsizeof('Andre Carvalho'))
print(getsizeof(9))
print(getsizeof(28))
print(getsizeof(900e000003))
print(getsizeof(True))

from sys import getsizeof

# Gerando uma 01_lista de números com List Comprehension
lista_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma 01_lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma 01_lista de números com Dictionary Comprehension
dic_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma 01_lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('===============================================')
print('Para fazer a mesma tarefa gastamos em memória: ')
print('===============================================')
print(f'List Comprehension: {lista_comp} bytes ')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator: {gen} bytes')

# Interando com generator expression
gen = (x * 10 for x in range(100))
print(gen)
print(type(gen))

for i in gen:
    print(i)
"""



