"""
Filter - filter() serve para filtrar dados de uma determinada coleção (Listas, Tuplas, dicionário)

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))
print(media)
# Aqui é somente um exemplo da media de valores, mas neste caso poderiamos filtrar quais valores estão acima da média

# Biblioteca para trabalhar com dados estatísticas
import statistics

# Dados coletadas de algum sensor, por exemplo, tecnologia das coisas
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Media: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável

res = filter(lambda x: x > media, dados)

print(list(res))
print(type(res))
print(f'Novamente: {list(res)}')

OBS: Assim como na função map(), após serem utlizados os dados de filter() eles são exluídos da memória

Vamos entender está função lambda:
- veja que passamos um parâmetro que seria "X" como nos não passamos nada para o X, passar como argumentos os próprios
dados do interável, então como que se lê: Para cada valor em dados ele vai atribuir a X como entrada


# Usando None para tirar os espaços em branco com filter
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', '', 'Colombia']
print(paises)
res = filter(None, paises)
print(list(res))

# Usando lambda para tirar os espacos em branco
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', '', 'Colombia']
print(paises)
res = filter(lambda pais: len(pais) > 0, paises)

# A diferença entre map() e filter() é:
# map()  -> Recebe dois parâmetros, uma função e um iterável e rertona um objeto mapeando a função para elemento do iterável.
# filter -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrado apenas os elementos de acordo com a função

# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu gosto de bolos", "Eu gosto de pizza"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Gosto de cachorro", "Vou sair hojw"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter
# Forma 1
inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))
print(inativos)


# Forma 2
inativos = list(filter(lambda usuario: not usuario["tweets"], usuarios))
print(inativos)
"""
# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos 5 caratecres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

