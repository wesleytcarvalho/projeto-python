"""
Até agora nos estudamos built-in functions que são nativas do python, mas agora vamos estudar funções relevantes para e
ste curso.
- exercicios, Tuplas, Dicionarios

Módulo collections - Counter (Contador)
- Collections é conhecido como High-performace Container Datetypes
- Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collerctions Counter que é parecido
com um dicionário, contendo como chave o elemento da 01_lista passada como parâmetro e como valor a quantidade
de ocorrência desse elemento

# Realizando o import
from 06_collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma 01_lista
01_lista = [1, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizando o Counter
res = Counter(01_lista)
print(res)
print(type(res))
# Counter({1: 2, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})
# Veja que, para cada elemento da 01_lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencia

Exemplo 2
print(Counter('UdayTC Computacao'))
# Counter({'a': 3, 'C': 2, 'o': 2, 'U': 1, 'd': 1, 'y': 1, 'T': 1, ' ': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'c': 1})
# Veja que, para cada elemento da 01_lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencia

Exemplo 3
texto = 'O USS Massachusetts é um encouraçado da classe Indiana e o segundo navio da Marinha dos
Estados Unidos comparável aos navios de guerra estrangeiros de seu tempo. Autorizado em 1890 e comissionado
seis anos depois, era um encouraçado de pequeno porte, embora possuísse blindagem e artilharia pesados.
A classe de navios a que pertencia também foi pioneira no uso de uma bateria intermediária.
Ele foi projetado para defesa costeira e, como resultado, seus decks não estavam a salvo de ondas
altas em mar aberto.'

palavas = texto.split()

res = Counter(palavas)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))

"""
