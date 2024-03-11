# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
def raio(r):
    """ A formula do raio de um  círculo é 'raio = diâmetro / 2' """
    return math.pi * (r ** 2)

print(f'O raio é {raio(10)}')
