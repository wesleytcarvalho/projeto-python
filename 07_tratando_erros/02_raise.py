"""
Levantando os próprios erros com raise

raise -> Lançando exceções

OBS: o raise não é uma função. É uma palavra reservada, assim como o def ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos criar as nossas próprias exceções e mensagens

A forma geral de utilização é:

raise TipoDoErro('Mensagem do erro')

Exemplo 1
raise ValueError('Valor incorreto')

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Precisa ser string')
    if type(cor) is not str:
        raise TypeError('Precisa ser string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Uday', 'Azul')

# Exemplo refatorado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'vermelho')
    if type(texto) is not str:
        raise TypeError('Precisa ser string')
    if type(cor) is not str:
        raise TypeError('Precisa ser string')
    if cor not in cores:
        raise TypeError('A cor não existe')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Uday', 'verde')


Obs: O raise, assim como o return, finaliza a função, ou seja, nada após o raise é executado.
Lembre-se ERRO É UMA execeção
"""