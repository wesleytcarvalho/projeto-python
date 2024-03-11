"""
Map - Com o map, fazemos mapeamento de valores para função

#Crinado um função normal
import math
def area(r):
    # Calcula a área de um círculo com raio 'r'.
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

# Forma comum
raio = [1, 43, 3.5, 24.5]
areas = []
for r in raio:
    areas.append(area(r))
print(areas)

# Forma 2  - utilizando MAP
# Map é uma função que recebe dois parâmetros: primeiro uma função e segundo um iterável
areas = map(area, raio)

print(areas)
print(type(areas))
print(list(areas))
print(tuple(areas))

# Foma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raio)))

#OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

# Para fixar - Map
# Temos os dados iteráveis
# dados: a1, a2,...an
# Temos uma função:
# função: f(x)
# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função
# O map object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo calculo em firenait
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19)]
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
"""
