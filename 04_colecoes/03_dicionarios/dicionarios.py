"""
Dicionários é inicial por chaves {}
Obs: Em algumas linguagens de programação os dicionários são conhecidos como MAPAS
dicionários são coleções do tipo chave/valor

dicionários sao representados por chaves {} equanto nos tinhamos o indece que poderia acessar através deles aqui
no 03_dicionarios e explicito porque temos a chave/valor

# Exemplo 1:
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}
print(paises)

# Acessando elementos
# Forma 1 - acessando via chave, da mesma forma que tupula/01_lista
print(paises['br'])

# Forma 2 - acessando via get, esta e a forma recomendada
print(paises.get('br'))
print(paises.get('ru'))
Obs: Se ele nao encontrasse o pais ele iria dar um erro, o uso do get e bom que nao dar um erro explicito somente NONE

# Podemos definir um valor padrao para caso nao encontramos objeto com a chave informada
pais = paises.get('ru', 'Nao encontrado')
print(pais)

# adicionando elemento no dicionário
paises['YO'] = 'Nova yourk'
print(paises)

# atualizar o dicionário adicionando elemento
novo_dado = {'maio': 500}
paises.update(novo_dado)
print(paises)

Conclusao: Dicionarios nao pode ter chaves repetidas

# Remover o elemento de um dicionário e mostra o que removeu
paises.pop('eua')
print(paises)

# Remove o elemento, mas não mostra o que removeu
del paises['br']
print(paises)

clear() = limpa o dicionário
novo = d.copy() = copiando um dicionário para outro
novo['d'] = 4 = adicionando o 4 no dicionário com a chave

# Caso o get não encontre o objeto com a chave informada sera retornado o valor NONE e nao
Sera gerado o (KeyError)
pais = paises.get('br')
if pais:
    print(f'Encontri o Pais {pais}')
else:
    print('Não entrei o pais')

# Podemos definir um valor padrão para caso nao encontremos o objeto com a chave informada
pais = paises.get('ru', 'Pais nao encontrado')
print(pais)

# Podemos verificar se determinado chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, bolean), inclusive lista, tuplas, dicionario, como chaves
# Tuplas sao bastante interessantes de serem utilizadas como chaves de dicionários, pois as mesmas
# sao imutaveis

localidades = {
    (35.6895, 39.6917): 'Escritorio em tokio',
    (40.7128, 39.434): 'Escritorio em Sao Paulo',
    (34.4568, 24.5678): 'Escritorio em Nove yourk',
}

print(localidades)
print(type(localidades))

# Adicionando elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 -  Mais comum
receita['abr'] = 232
print(receita)

# Forma 2
nova_receita = {'mai': 345}
receita.update(nova_receita)
print(receita)

# Forma 3
receita.update({'mai': 2})
print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário e a mesma.
# CONCLUSAO 2: Em dicionário, NAO podemos ter chaves repetidas


# Remover dados de uma dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - Mais COMUM
ret = receita.pop('mar')
print(ret)

print(receita)
# Obs1 : Aqui precisamos SEMPRE informar a chave, e caso nao encontre o elemento, um KeyError e retornado
# Obs1 : Ao removermos um objeto, o valor deste objeto e sempre retornado

# Forma 2
del receita['fev']
print(receita)

# Se a chave nao existir sera gerado um KeyError
# Obs: Neste caso o valor removido nao e retornado


# Voce deve esta se perguntando onde eu vou usar dicionario?
# Imagine que voce tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos produtos

Carrinho de produtos:
    produto 1:
        - nome
        - quantidade
        - preco
    produto 2:
     - nome
     - quantidade
     - preco

# Casos de uso
# 1 - Poderiamos utlizar Listas para isso? Sim
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God Of War 4', 1, 2300.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual e o indice de cada informacao no produto

# 2 - Poderiamos utilizar uma tupla para isso? Sim
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God Of War 4', 1, 2300.00)
carrinho = (produto1, produto2)
print(carrinho)
# mas nas 02_tuplas ainda sim precisaria saber o indice de cada elemento

# 3 - Poderiamos utlizar um Dicionário para isso? Sim
carrinho = []
produto1 = {'nome': 'Playstion 4', 'qta': 1, 'preco': 2300.00}
produto2 = {'nome': 'Playstion 4', 'qta': 1, 'preco': 2300.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Desta forma, facilment adicionamos ou removemos produto no carinho e em cada produto

# Metodos de 03_dicionarios
# Vamos utlizar outra forma de criar um dicionario, nao e muito usual, mas e importante conhecer
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Este metodo limpa o dicionário
d.clear()
print(d)

# Copiando dicionario para outro
# Forma 1 - deep copy
novo = d.copy()  #
print(novo)
novo['d'] = 4  #
print(novo)

# Forma 2 - Shellow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma nao usual de criacao de dicionário
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuarios = {}.fromkeys(['nome', 'pontas', 'email', 'profile'], 'desconhecido')
print(usuarios)
print(type(usuarios))
# O metodo fromKeys recebe dois paramentros: um interavel e um valor
# Ele vai gerar para cada valor do interavel uma chave e ira atribuir a esta chave o valor informado.
"""