"""
Conjuntos conhecidos como Sets

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos da matemática.
- Aqui no python os conjuntos são chamados de conjuntos sets, Dito isso, da mesma forma da matemática:
- Sets (Conjuntos) não possuem valores duplicados;
- Sets (Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjunto não são indexados;
- Conjunto são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos na ordenação deles.
Quando não precisamos se preocupar com chaves e itens duplicados.
- Os conjuntos (sets) são referenciados em python com chaves {}


Diferença entre Conjuntos (conjuntos) e Mapas (Dicionario) em python.
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# sera ignorado sem gerar erros nao fara parte do conjunto

# Forma 2 - Mais comum
s = {1, 2, 4, 5, 5, 6, 7, 2}
print(s)
print(type(s))

# podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('Tem 3')
else:
    print('Nao tem o 3')

# Imporante lembrar que, além de não termos valores duplicados, nao temos ordem
# Lista aceitam valores duplicados, entao temos 8 elementos
lista = [99, 2, 6, 4, 12, 56, 38, 99]
print(f'exercicios: {lista} \nquantidade de elementos {len(lista)} \ntipo de elemento: {type(lista)}')
print()

# Tuplas aceitam valores duplicados, entao temos 8 elementos
tupla = 99, 2, 6, 4, 12, 56, 38, 99
print(f'Tupla: {tupla} \nquantidade de elementos {len(tupla)} \ntipo de elemento: {type(tupla)}')
print()

# Dicionario Nao aceitam chaves duplicadas, entao temos 7 elementos
dicionario = {}.fromkeys([99, 2, 6, 4, 12, 56, 38, 99], 'dict')
print(f'Dicionario: {dicionario} \nquantidade de elementos {len(dicionario)} \ntipo de elemento: {type(dicionario)}')
print()

# Conjunto nao aceitam valores duplicados, entao temos 7 elementos
conjunto = {99, 2, 6, 4, 12, 56, 38, 99}
print(f'Conjunto: {conjunto} \nquantidade de elementos {len(conjunto)} \ntipo de elemento: {type(conjunto)}')
print()

# Assim como toda outro conjunto em python podemos colocar tipos de dados misturados em conjuntos_sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine voce tem um formulario de pessoas que estao viajando no onibus e voce quer fazer uma lista
# de pessoa por cidade e nao pode ter repeticao

cidades = ['Sao Paulo', 'Cuiaba', 'Belo Horizonte', 'Cuiaba', 'Belo Horizonte', 'Sao Paulo']
print(cidades)

# Veja que na lista tem valores repetidos e eu preciso que nao tenho e mostre somente a quantidade
print(len(set(cidades)))

# Obs: Neste caso usamos o set para isso

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplidade nao gera erro, simplesmente e ignorado e nao e adicionando
print(s)

# Remover elementos em um consjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # NAO e indice! Informamos o valor a ser removido.
print(s)
# Obs: Caso o valor nao seja encontrado sera gerado o erro KeyError. Nenhum valor e retornado

# Forma 2
s.discard(2)
print(s)
# Obs: Se um valor nao for encontrado com discard, nenhum erro e gerado.

# Copiando um conjunto para outro
# Forma 1 - Deep Copy / Com o deep copy criamos dois objetos separados independente, se eu alterar um nao altera o outro
novo = s.copy()
print(novo)
novo.add(4)
print(novo)

# Forma 2 - Shellow Copy / Com o Shellow Copy sempre vamos ter os mesmos valores nas variaveis, ou seja, se eu alterar
um ele altera o outro

novo = s
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens em um conjunto
s.clear()
print(s)
--------------------------------------------------------------------------------
# Metodos matematicos de conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso python em um
# contendo do curso de java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Jose', 'Julia', 'Guilherme'}
estudantes_java = {'Guilherme', 'Patricia', 'Jose', 'Ellen', 'Jose', 'Julia', 'Marcos'}
# Veja que alguns alunos que estudam python tambem estudam java.
# Precisamos gerar um conjunto com nomes de estudantes unicos.

# Forma 1 - Utilizando union (uniao)
# unicos1 = estudantes_python.union(estudantes_java)
# # {'Jose', 'Patricia', 'Ellen', 'Marcos', 'Julia', 'Guilherme'}
# unicos2 = estudantes_java.union(estudantes_python)
# # {'Marcos', 'Jose', 'Patricia', 'Guilherme', 'Julia', 'Ellen'}
print(unicos2)

# Forma 2 - utlizando o caratere |
unicos3 = estudantes_python | estudantes_java
print(unicos3)

# Gerar um conjunto de estudantes que estao em ambos os curso
# Forma 1 - Utilizando intersention
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que nao estao no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, valor maximo, valor minimo, tamanho
# Se os valores forem inteiros ou reais

s = {1, 2, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""


