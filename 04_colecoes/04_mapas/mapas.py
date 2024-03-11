"""
Mapas -> conhecido em python como dicionários
- dicionários em python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

print(receita.items())

# Desempacotamento de 03_dicionarios
for chave, valor in receita.items():
    print(f'chave={chave}, valor={valor}')

# Soma, valor maximo, valor minimo, tamanho
# So podemos claro usar este metodo acima de se os valores forem inteiro ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)


