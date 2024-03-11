"""
4. Escreva um programa Python para classificar uma lista de dicionários usando Lambda.
Lista original de dicionários:
[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Mi Max', 'model': '2', 'color ': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Classificando a lista de dicionários:
[{'make': 'Nokia', 'model' : 216, 'cor': 'Preto'},
{'marca': 'Samsung', 'modelo': 7, 'cor': 'Azul'},
{'marca': 'Mi Max', 'modelo': '2', 'color': 'Gold'}]

# Uma boa estratégia para você trabalhar com lambda e verificando com ele saíria no FOR
for i in produto:
    for chave, valor in i.items():
        print(chave, valor)

"""
produto = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print('Lista de dicionario normal')
print(produto)

sorted_produto = sorted(produto, key=lambda x: x['color'])

print('\nLista de dicionário ordenado por "color"')
print(sorted_produto)
