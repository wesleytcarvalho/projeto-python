"""
Documentando uma função com Docstrings
Python docstrings são strings literais que aparecem logo após a definição de uma função, método, classe ou módulo.
Vamos dar um exemplo.

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

Veja que dentro desta função temos uma documentação:
'''Takes in a number n, returns the square of n'''

# Declarando uma nova função com uma documentação
def diz_oi():
    ''' Uma função simples que retorna a string 'Oi!' '''
    return 'Oi!'

print(diz_oi())

# Eu posso importar a função para poder ver o help dele se quiser
# Abra o terminal python e depois digite "from docstrings import diz_oi"
# help(diz_oi)
# Podemos também ter acesso a propriedade especial chamado __doc__ exemplo abaixo.
print.__doc__

def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado de 'numero' ou à 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial .
    :param potencia: potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorno o exponencial de 'numero' por 'potencia'
    '''
    return numero ** potencia

# Agora abra o terminal com o python e inserir os comandos abaixo, você precisa importar a função e depois usar o
# __doc__ para visualizar a documentação da função
from docstrings import exponencial
exponencial.__doc__
"""


