"""
1. Escreva um programa Python para criar uma função lambda que adicione 15 a um determinado número passado como argumento, crie também uma função lambda que multiplique o argumento x pelo argumento y e imprima o resultado.
Saída de amostra:
25
48

"""
lamb1 = lambda x: x + 15
print(lamb1(10))

lamb2 = lambda x, y: x * y
print(lamb2(12, 4))
