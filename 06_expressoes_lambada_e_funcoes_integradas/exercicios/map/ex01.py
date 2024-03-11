def calcular_imposto(preco):
    return preco * 1.1

# Veja assim é muito simples o calculo, agora vamos imagina que é uma lista, como poderiamos fazer?
# print(calcular_imposto(12))


preco = [1204, 1000, 3004, 2424, 7768]

preco_com_importo = []

# Veja que fazendo assim tambem funciona, mas temos o map que pode interar com uma funcao, ou seja,
# ele recebe uma funcao e um iteravel
for p in preco:
    preco_com_importo.append(calcular_imposto(p))
print(preco_com_importo)


# agora usando o map
preco_imposto = map(calcular_imposto, preco)
print(list(preco_imposto))



