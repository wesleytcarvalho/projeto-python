"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Previnindo
assim que programa pare de funcionar e o usuario receba a mensgens de erro insperados.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# soma() = veja este exemplo abaixo, estou querenso criar uma funcao, mas esta faltando o comando deff
# vai retorna o erro NameError, mas tome muito cuidado para nao automatizar o erro.
# Exemplo 1 - Tratando um erro generico

try:
    soma()
except:
    print('Deu algum erro, contacte o administrator')


# Falando em palavras mais claras o codigo acima esta falandoo seguinte:
Tente executar a funcao soma() Se der erro mostre a mensagem na tela

Obs: Tratar erro de forma generica não é a melhor forma de tratamento de erros
O ideial e SEMPRE tratar de forma específica.

# Exemplo 2 - tratando um erro especifico
try:
    len(4)
except TypeError:
    print('Voce esta utlizando uma funcao inexistente')

# Exemplo 3 - tratando um erro especifico
try:
    soma()
except NameError:
    print('Voce esta utlizando uma funcao inexistente')

# Exemplo 3 - tratando um erro especifico com detalhes do erro inserirndo o "as" e qualquer nome
try:
    len(3)
except TypeError as err:
    print(f'A aplicacao gerou o seguinte erro: {err}')

try:
   soma(x)
except TypeError as err:
    print(f'Erro conhecido: {err}')
except NameError as funcao:
    print(f'Erro em: {funcao}')
except:
    print('Erro generico')

# Agora como usar o try/except?
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Andre'}

print(pega_valor(dic, 'nome'))
"""

