"""
Modulo Collections - Default Dict
Documentacao: https://docs.python.org/3/library/collections.html

# Recapitulando 03_dicionarios
03_dicionarios = {'Curso': 'Programacao em python: Essencial'}
print(03_dicionarios)
print(03_dicionarios['Curso'])
# Se colocarmos um valor que nao existe no dicionario ele da o erro (KeyError)

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor defaul
pode utilizar uma lambada pra isso. Este valor sera utilizado sempre que nao houver um valor
definido. Caso tentemos acessar uma chave que nao existe, essa chave sera criada e o valor
default sera atribuido.

Obs: Lambada sao funcoes sem nome, que podem ou nmao receber parametros de entrada e
retorna valores

# Fazendo import
from 06_collections import defaultdict
dicionario = defaultdict(lambda: 0)
print(dicionario)
dicionario['curso'] = 'Programacao em puthon: essencial'
print(dicionario)
print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui nao.
print(dicionario)
# Veja que quando estamos querendo ver outra chave ao inves de ele dar erro ele adiciona a chave no dicionario
# defaultdict(<function <lambda> at 0x10b4881f0>, {'curso': 'Programacao em puthon: essencial', 'outro': 0})
"""